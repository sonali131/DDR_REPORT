# 🏗️ Automated DDR (Detailed Diagnostic Report) Generator

### Transforming Raw Site Data into Intelligent, Client-Ready Reports

An AI-powered **multimodal reporting system** that converts raw inspection documents and thermal reports into structured, insightful, and visually aligned diagnostic reports—reducing manual effort and eliminating human error.

---

## 🚀 Live Demo & Walkthrough

* 🔗 **Live Application:** https://ddrreport-edtqymab8enywh4zz2rxap.streamlit.app/
* 🎥 **Video Explanation:** *https://drive.google.com/drive/folders/1juWVqIxLeLL2Y5_u5baV4pfAAWgUL4JJ?usp=drive_link*

---

## 🛠️ Problem Statement

Generating professional diagnostic reports from site inspections is:

* ⏳ Time-consuming
* ❌ Error-prone
* 🔗 Difficult to correlate across multiple data sources

### This project solves:

* **🔄 Intelligent Data Merging**
  Seamlessly connects **visual observations** with **thermal anomalies** for accurate insights.

* **🖼️ Context-Aware Image Placement**
  Automatically embeds site images **exactly where they belong**, instead of dumping them in a gallery.

* **🛡️ Data Integrity & Reliability**
  Detects missing or conflicting inputs and clearly marks them (e.g., *"Not Available"*), ensuring transparency.

---

## 🧠 System Architecture & Workflow

### 1. 📄 Extraction Engine

* Built using **PyMuPDF (fitz)** with spatial coordinate analysis
* Filters out noise like logos, headers, and dividers
* Extracts only **relevant text + high-quality site images**

### 2. 🏷️ Contextual Indexing

* Tags images with nearby textual content
* Creates **semantic linkage** between visuals and observations

### 3. 🤖 AI Reasoning Layer

* Powered by **Llama-3.3-70B (via Groq Cloud)**
* Performs:

  * Root cause analysis
  * Severity detection
  * Cross-document reasoning

### 4. 🧾 Dynamic Report Renderer

* Regex-based parser
* Injects images directly under corresponding observations
* Outputs a **clean, structured Markdown report**

---

## 💻 Tech Stack

| Category           | Technology                        |
| ------------------ | --------------------------------- |
| **Language**       | Python 3.10+                      |
| **LLM**            | Llama-3.3-70B (Groq Cloud)        |
| **Frontend**       | Streamlit                         |
| **PDF Processing** | PyMuPDF (fitz), Pillow            |
| **Data Handling**  | Regex, Dotenv, Multimodal Mapping |

---

## ✨ Key Features

* ✅ **Smart Noise Filtering**
  Ignores logos, headers, and irrelevant artifacts automatically

* 🔗 **Multimodal Correlation**
  Aligns visual issues (e.g., dampness) with thermal data (e.g., cold spots)

* ⚖️ **Rule-Based Reliability**
  Handles incomplete or conflicting data explicitly

* 📥 **Export-Ready Reports**
  Generates professional, client-ready Markdown outputs

---

## ⚙️ Local Setup

```bash
# Clone the repository
git clone https://github.com/sonali131/DDR_REPORT.git

# Install dependencies
pip install -r requirements.txt

# Add your Groq API Key
echo "GROQ_API_KEY=your_key_here" > .env

# Run the app
streamlit run app.py
```

---

## 🚧 Limitations & Future Improvements

### ⚠️ Current Limitation

* Groq Free Tier token limits require truncation for very large PDFs

### 🚀 Future Enhancements

* 🧠 Integrate **Vision-Language Models (VLMs)** (e.g., LLaVA, GPT-4o) for direct image understanding
* 🗂️ Add **Vector Database (RAG)** for long-term site history analysis
* 📊 Advanced analytics dashboards for trend detection

---

## 👩‍💻 Candidate Profile

**Sonali Mishra**
🎯 *AI Generalist | Applied AI Builder*

* Expertise in **AI-powered applications, LLMs, and full-stack development**
* Passionate about building **real-world, scalable AI solutions**

---

## 💡 Why This Project Stands Out

This isn’t just a report generator—it’s a **decision-support system** that:

* Thinks across multiple data modalities
* Maintains data integrity
* Produces actionable, structured insights

👉 Designed with **real industry challenges in mind**, making it highly relevant for applied AI roles.

---
