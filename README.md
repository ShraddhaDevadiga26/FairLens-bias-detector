# FairLens-bias-detector
AI-powered bias detection suite for hiring, loans &amp; insurance with voice assistant, camera scan &amp; helpline

# FairLens — AI Bias Detection Suite

> **Where does bias hide in your data?**  
> FairLens is an AI-powered platform that detects algorithmic discrimination across hiring, loans, and insurance — with voice assistant, camera scan, and a 24/7 helpline.

##  Built for Hack2Skill · Unbiased AI Challenge 2026

##  Features

###  Module 01 — Job Hiring Bias
- Upload your resume and a job description
- AI detects ATS discrimination patterns
- Flags bias triggers with an interactive heatmap
- Identifies gender, name, and regional bias in job screening

### Module 02 — Loan Approval Bias
- Enter your loan application details
- Detects if your name, region, or income pattern triggered unfair rejection
- Shows real-world disparity statistics

### Module 03 — Insurance Claim Bias
- Analyze your insurance claim for discriminatory patterns
- Identifies if automated systems flagged your claim based on protected characteristics

###  AI Assistant
- Chat with an AI assistant about bias, fairness, and your results
- Voice-enabled — speak your query, hear the response
- Powered by Claude (Anthropic)

### Camera Scan
- Quick document scan directly from the sidebar
- Capture and analyze documents on the go

###  Helpline
- 24/7 bias reporting support
- Direct contact via email and WhatsApp

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Google Gemini API  |
| Voice | gTTS (Google Text-to-Speech) |
| Language | Python 3.11 |
| Styling | Custom CSS + Google Fonts |


### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
fairlens/
├── app.py                  
├── pages/
│   ├── Job_Hiring_Bias.py   
│   ├── Loan_Approval_Bias.py 
│   ├── Insurance_Claim_Bias.py 
│   └── AI_Assistant.py      # Voice + Chat AI
├── requirements.txt
└── README.md

<img width="1842" height="868" alt="Screenshot 2026-04-27 233646" src="https://github.com/user-attachments/assets/220a938e-1922-4725-841f-29c7134a3a07" />
