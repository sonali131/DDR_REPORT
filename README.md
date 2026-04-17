# DDR_REPORT
AI+Streamlit+image
# 🏗️ Automated DDR (Detailed Diagnostic Report) Generator

An AI-powered multimodal workflow that converts raw technical site inspection documents and thermal reports into structured, client-ready diagnostic reports.

## 🚀 Live Demo & Video
- **Live Link:** [View App](https://ddrreport-edtqymab8enywh4zz2rxap.streamlit.app/)
- **Loom Video Explanation:** [Watch Video Link Here]

## 🛠️ The Challenge
Converting raw site data into professional reports is time-consuming and prone to human error. This project solves:
1. **Logical Merging:** Automatically connecting visual observations with thermal temperature anomalies.
2. **Contextual Image Placement:** Mapping specific site photos to the correct textual observation instead of just providing a gallery.
3. **Data Integrity:** Handling missing information and conflicting data between different report sources.

## 🧠 System Architecture & Workflow
1. **Extraction Engine:** Uses `PyMuPDF` with spatial coordinate analysis to extract text and evidence photos. It implements a geometric filter to skip document artifacts (logos, divider lines) and capture only high-resolution site evidence.
2. **Indexing & Tagging:** Extracted images are indexed with surrounding text context. 
3. **AI Reasoning (LLM):** Powered by `Groq Llama-3.3-70B`. The system analyzes the merged context of Inspection and Thermal reports to identify root causes and severity.
4. **Dynamic Renderer:** A custom regex-based parser that injects site photos directly under the relevant observations in the final Markdown report.

## 💻 Tech Stack
- **Language:** Python 3.10+
- **LLM:** Llama-3.3-70B-Versatile (via Groq Cloud)
- **Framework:** Streamlit (Frontend/UI)
- **PDF Processing:** PyMuPDF (fitz) & Pillow
- **Data Handling:** Regex, Dotenv, Multimodal Context Mapping

## ✨ Key Features
- **Smart Filtering:** Automatically ignores company logos and header/footer elements.
- **Multimodal Merging:** Syncs visual findings (Dampness) with thermal readings (Cold spots/Temperatures).
- **Rule-Based Reliability:** Explicitly handles missing data with "Not Available" tags and highlights data conflicts.
- **Downloadable Reports:** Generates professional Markdown deliverables.

## ⚙️ Local Setup
1. Clone the repo: `git clone https://github.com/sonali131/DDR_REPORT.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Groq API Key in a `.env` file: `GROQ_API_KEY=your_key_here`
4. Run the app: `streamlit run app.py`

## 🚧 Limitations & Improvements
- **Current Limitation:** Token limits of the Groq Free Tier require text truncation for very large PDFs.
- **Future Scope:** Integrating a **Vision-Language Model (VLM)** like LLaVA or GPT-4o for direct image-to-text analysis and using a **Vector Database (RAG)** for processing year-long site history.

---
**Candidate:** Sonali Mishra  
**Role:** AI Generalist / Applied AI Builder Assignment
