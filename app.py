import streamlit as st

st.set_page_config(
    page_title="FairHire · AI Bias Detection Suite",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Epilogue:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0d0d0d;
    color: #e2e0d8;
    font-family: 'Epilogue', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: #0d0d0d;
    min-height: 100vh;
}

#MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stDecoration"] {
    visibility: hidden; display: none;
}

/* ── NOISE OVERLAY ── */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.4;
}

.main-wrap {
    max-width: 1100px;
    margin: 0 auto;
    padding: 4rem 2rem 6rem;
    position: relative;
    z-index: 1;
}

/* ── HEADER ── */
.site-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}
.logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #e2e0d8;
    letter-spacing: -0.01em;
}
.logo span { color: #c9a84c; }
.header-tag {
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #5a5a5a;
}

/* ── HERO SECTION ── */
.hero-section {
    margin-bottom: 5rem;
}
.hero-eyebrow {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #c9a84c;
    margin-bottom: 1.2rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 6vw, 5.5rem);
    font-weight: 900;
    line-height: 1.0;
    letter-spacing: -0.03em;
    color: #f0ede4;
    margin-bottom: 1.5rem;
    max-width: 720px;
}
.hero-title em {
    font-style: italic;
    color: #c9a84c;
}
.hero-subtitle {
    font-size: 1.05rem;
    color: #6b6960;
    max-width: 500px;
    line-height: 1.75;
    font-weight: 400;
}

/* ── SECTION LABEL ── */
.section-label {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #4a4a4a;
    margin-bottom: 1.5rem;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}

/* ── MODULE CARDS ── */
.modules-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 2px;
    overflow: hidden;
    margin-bottom: 4rem;
}
.module-card {
    background: #0d0d0d;
    padding: 2.5rem;
    position: relative;
    cursor: pointer;
    transition: background 0.25s ease;
    text-decoration: none;
    display: block;
}
.module-card:hover {
    background: #141414;
}
.module-card::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(201,168,76,0), transparent);
    transition: background 0.3s;
}
.module-card:hover::after {
    background: linear-gradient(90deg, transparent, rgba(201,168,76,0.5), transparent);
}
.module-number {
    font-family: 'Playfair Display', serif;
    font-size: 0.75rem;
    font-weight: 400;
    color: #3a3a3a;
    letter-spacing: 0.1em;
    margin-bottom: 1.2rem;
}
.module-icon {
    font-size: 1.8rem;
    margin-bottom: 1rem;
    display: block;
}
.module-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #e2e0d8;
    margin-bottom: 0.6rem;
    line-height: 1.2;
}
.module-desc {
    font-size: 0.85rem;
    color: #5a5855;
    line-height: 1.65;
    margin-bottom: 1.5rem;
}
.module-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 1.5rem;
}
.module-tag {
    font-size: 0.68rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.25rem 0.6rem;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 2px;
    color: #5a5855;
}
.module-cta {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #c9a84c;
}
.module-cta-arrow {
    transition: transform 0.2s;
}
.module-card:hover .module-cta-arrow {
    transform: translateX(4px);
}
.module-card.coming-soon {
    opacity: 0.4;
    cursor: not-allowed;
}
.module-card.coming-soon:hover { background: #0d0d0d; }
.coming-soon-badge {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #5a5855;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 0.2rem 0.6rem;
    border-radius: 2px;
    display: inline-block;
    margin-top: 1rem;
}

/* ── STATS ROW ── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0;
    border: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 4rem;
}
.stat-item {
    padding: 2rem;
    border-right: 1px solid rgba(255,255,255,0.06);
    text-align: center;
}
.stat-item:last-child { border-right: none; }
.stat-number {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 900;
    color: #c9a84c;
    display: block;
}
.stat-label {
    font-size: 0.75rem;
    color: #4a4a4a;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-top: 0.3rem;
}

/* ── FOOTER ── */
.site-footer {
    border-top: 1px solid rgba(255,255,255,0.06);
    padding-top: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}
.footer-text {
    font-size: 0.75rem;
    color: #3a3a3a;
    letter-spacing: 0.05em;
}
.footer-link {
    font-size: 0.75rem;
    color: #5a5855;
    text-decoration: none;
    letter-spacing: 0.05em;
    border-bottom: 1px solid #3a3a3a;
    padding-bottom: 1px;
}

/* Streamlit button override */
.stButton > button {
    background: transparent !important;
    border: 1px solid rgba(201,168,76,0.4) !important;
    color: #c9a84c !important;
    font-family: 'Epilogue', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    padding: 0.8rem 2.5rem !important;
    border-radius: 2px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: rgba(201,168,76,0.08) !important;
    border-color: rgba(201,168,76,0.7) !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

# Header
st.markdown("""
<div class="site-header">
    <div class="logo">Fair<span>Hire</span> · Suite</div>
    <div class="header-tag">AI Bias Detection · 2026</div>
</div>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero-section">
    <div class="hero-eyebrow">Algorithmic Fairness Intelligence</div>
    <h1 class="hero-title">Where does<br><em>bias</em> hide<br>in your data?</h1>
    <p class="hero-subtitle">Three specialized modules to detect, expose, and explain automated discrimination — in hiring, lending, and insurance.</p>
</div>
""", unsafe_allow_html=True)

# Stats
st.markdown("""
<div class="stats-row">
    <div class="stat-item">
        <span class="stat-number">67%</span>
        <div class="stat-label">of ATS systems show measurable bias</div>
    </div>
    <div class="stat-item">
        <span class="stat-number">50%</span>
        <div class="stat-label">fewer callbacks for ethnic-sounding names</div>
    </div>
    <div class="stat-item">
        <span class="stat-number">3×</span>
        <div class="stat-label">loan rejection rate disparity by zip code</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Modules
st.markdown('<div class="section-label">Select a module to begin</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="small")

with col1:
    st.markdown("""
    <div class="module-card">
        <div class="module-number">Module 01</div>
        <span class="module-icon">💼</span>
        <div class="module-title">Job Hiring Bias</div>
        <div class="module-desc">Upload your resume and a job description. Our AI detects ATS discrimination patterns, flags bias triggers, and maps them directly onto your resume with an interactive heatmap.</div>
        <div class="module-tags">
            <span class="module-tag">Resume Analysis</span>
            <span class="module-tag">ATS Simulation</span>
            <span class="module-tag">Bias Heatmap</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Module →", key="btn_job"):
        st.switch_page("pages/1_Job_Hiring_Bias.py")

with col2:
    st.markdown("""
    <div class="module-card">
        <div class="module-number">Module 02</div>
        <span class="module-icon">🏦</span>
        <div class="module-title">Loan Approval Bias</div>
        <div class="module-desc">Enter your loan application details. Detect if your name, region, or income pattern unfairly triggered automated rejection — with real-world disparity statistics.</div>
        <div class="module-tags">
            <span class="module-tag">Name Analysis</span>
            <span class="module-tag">Regional Bias</span>
            <span class="module-tag">Income Patterns</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Module →", key="btn_loan"):
        st.switch_page("pages/2_Loan_Approval_Bias.py")

with col3:
    st.markdown("""
    <div class="module-card">
        <div class="module-number">Module 03</div>
        <span class="module-icon">🛡️</span>
        <div class="module-title">Insurance Claim Bias</div>
        <div class="module-desc">Analyze your insurance claim for discriminatory patterns. Identify if automated systems unfairly flagged your claim based on protected characteristics.</div>
        <div class="module-tags">
            <span class="module-tag">Claim Analysis</span>
            <span class="module-tag">Fair Decisions</span>
            <span class="module-tag">Pattern Detection</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Module →", key="btn_ins"):
        st.switch_page("pages/3_Insurance_Claim_Bias.py")

# Footer
st.markdown("""
<div class="site-footer">
    <div class="footer-text">FairHire Suite · Built for Hack2Skill · Unbiased AI Challenge 2026</div>
    <a href="https://github.com/shreyamokshanatha-hue/fairhire-bias-detector" target="_blank" class="footer-link">View Source on GitHub ↗</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
