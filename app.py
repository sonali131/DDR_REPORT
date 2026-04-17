import streamlit as st
import os
import re
from dotenv import load_dotenv
from groq import Groq
from utils import process_pdf

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI DDR Generator", layout="wide")
st.title("🏗️ Professional DDR Report Generator")

def limit_text(text, max_chars=8000):
    return text[:max_chars] + "\n... [Truncated]" if len(text) > max_chars else text

col1, col2 = st.columns(2)
with col1:
    inspect_pdf = st.file_uploader("Upload Inspection Report", type="pdf")
with col2:
    thermal_pdf = st.file_uploader("Upload Thermal Report", type="pdf")

if st.button("Generate Final DDR Report") and inspect_pdf and thermal_pdf:
    with st.spinner("Analyzing Site Evidence..."):
        # Save temp files
        with open("temp_i.pdf", "wb") as f: f.write(inspect_pdf.getbuffer())
        with open("temp_t.pdf", "wb") as f: f.write(thermal_pdf.getbuffer())

        # Process
        i_text, i_imgs = process_pdf("temp_i.pdf", "inspect")
        t_text, t_imgs = process_pdf("temp_t.pdf", "thermal")
        all_imgs = i_imgs + t_imgs

        # Increase limit to 20 images so AI sees more choices beyond logos
        img_list_for_ai = ""
        for idx, img in enumerate(all_imgs[:20]):
            img_list_for_ai += f"ID:{idx} | Nearby Text: {img['context'][:100]}\n"

        prompt = f"""
        Role: Senior Building Surveyor. Task: Generate a professional DDR.
        
        INSPECTION DATA: {limit_text(i_text)}
        THERMAL DATA: {limit_text(t_text)}
        IMAGES: {img_list_for_ai}

        STRICT RULES:
        1. You MUST find temperature values (e.g., 28.8°C, 24.5°C) from the THERMAL DATA.
        2. Combine these temperatures with the visual findings in 'Area-wise Observations'. 
           DO NOT write "Not Available" for temperature if it exists in the data.
        3. Insert exactly ONE [IMG_ID] tag per area.
        4. If Inspection says dry but Thermal says cold (temp drop), highlight as a CONFLICT.
        
        STRUCTURE:
        1. Property Issue Summary
        2. Area-wise Observations (Combine Text + Temp + [IMG_ID])
        3. Probable Root Cause
        4. Severity Assessment
        5. Recommended Actions
        6. Missing Information (Use 'Not Available' ONLY if data is truly missing)
        """
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.1
            )
            report_text = response.choices[0].message.content

            st.markdown("---")
            st.header("📋 Final Detailed Diagnostic Report")

            # --- SMART RENDERER ---
            parts = re.split(r'(\[IMG_ID:\d+\]|\[IMG_\d+\])', report_text)
            
            for part in parts:
                img_tag_match = re.search(r'\d+', part)
                if img_tag_match and (part.startswith("[IMG_") or part.startswith("[IMG_ID:")):
                    img_id = int(img_tag_match.group())
                    if img_id < len(all_imgs):
                        st.image(all_imgs[img_id]['path'], 
                                 caption=f"Evidence Photo ID: {img_id}", 
                                 use_container_width=True)
                else:
                    st.markdown(part)

            st.success("✅ DDR Finalized (Logo-Filtered & Context-Mapped)")
            st.download_button("Download Report (.md)", report_text, "DDR_Final_Report.md")

        except Exception as e:
            st.error(f"Error: {e}")