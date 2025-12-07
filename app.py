import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import os
import altair as alt

#Sayfa ayarları
st.set_page_config(
    page_title="Salary AI | Group 15",
    page_icon="gazi_logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    header {visibility: hidden;}
    .stAppHeader {display: none;}
    footer {visibility: hidden;}
    .main { background-color: #f8f9fa; }
    
    .stButton>button { 
        width: 100%; border-radius: 25px; height: 55px; font-size: 18px; font-weight: 600;
        background: linear-gradient(90deg, #2E86C1 0%, #1B4F72 100%); color: white; border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 7px 10px rgba(0,0,0,0.2); }
    
    .result-card {
        background-color: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08); text-align: center; margin-top: 25px; border: 1px solid #e1e4e8;
    }
    
    .metric-card {
        background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #2E86C1;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-top: 10px; text-align: left; color: #000000 !important;
    }
    .metric-card b, .metric-card span, .metric-card div { color: #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

# Grafik gösterimi için verilerin çekilmesi
@st.cache_data(ttl=3600)
def load_dataset(uploaded_file=None):
    default_path = os.path.join('data', 'processed', 'main_salary_dataset.csv')
    df = None
    try:
        source = uploaded_file if uploaded_file else default_path
        if uploaded_file or os.path.exists(default_path):
            df = pd.read_csv(source, sep=',', quoting=3, on_bad_lines='skip', engine='python')
            df.columns = [c.strip().lower().replace(' ', '_').replace('"', '') for c in df.columns]
            for col in ['salary', 'years_experience', 'age']:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')
            if 'job_title' in df.columns:
                df['job_title'] = df['job_title'].astype(str).str.strip().str.lower()
            df = df.dropna(subset=['job_title', 'salary'])
    except: pass
    return df

@st.cache_resource
def load_models():
    model_path = os.path.join('models', 'salary_model_target_encoded.pkl')
    means_path = os.path.join('models', 'job_title_means.pkl')
    
    model = None
    job_means = {}
    is_active = False
    
    if os.path.exists(model_path) and os.path.exists(means_path):
        try:
            model = joblib.load(model_path)
            raw_means = joblib.load(means_path)
            
            if isinstance(raw_means, pd.Series):
                job_means = raw_means.to_dict()
            elif isinstance(raw_means, dict):
                job_means = raw_means
            else:
                job_means = {}
            
            is_active = True
        except Exception as e:
            st.error(f"Model yüklenemedi: {e}")
            pass

    return model, job_means, is_active

# Yükleme
uploaded_csv = st.sidebar.file_uploader("Veri Yükle (CSV)", type="csv")
df_salary = load_dataset(uploaded_csv)
model, job_means, model_active = load_models()

GLOBAL_MEAN_SALARY = 50000 
if df_salary is not None and 'salary' in df_salary.columns:
    GLOBAL_MEAN_SALARY = df_salary['salary'].mean()

# Arayüz kısmı
col_spacer1, col_center, col_spacer2 = st.columns([3, 4, 3])
with col_center:
    try: st.image("gazi_logo.png", width=150)
    except: pass

    st.markdown("""
        <div style="text-align: center;">
            <h1 style="color: #1f2937; font-family: sans-serif; font-size: 32px; margin-bottom: 5px;">
                AI-Based Salary Prediction System
            </h1>
            <p style="color: #6b7280; font-size: 16px;">
                Gazi University - Group 15
            </p>
        </div>
        <hr style="margin: 15px 0 25px 0;">
    """, unsafe_allow_html=True)

# Girdi kısmı 
with st.form("salary_form"):
    left, form_area, right = st.columns([1, 2, 1])
    with form_area:
        st.markdown("### Career Details")
        
        # Meslek Listesi
        job_list = []
        if df_salary is not None:
            job_list = sorted([j.title() for j in df_salary['job_title'].unique()])
        elif job_means:
            job_list = sorted([str(j).title() for j in job_means.keys()])
        
        s_job = st.selectbox("Job Title", job_list, index=None, placeholder="Select a Role...")
        
        c1, c2 = st.columns(2)
        with c1:
            s_edu = st.selectbox("Education", ["Unknown", "High School", "Bachelor's Degree", "Master's Degree", "PhD"])
            s_age = st.number_input("Age", 18, 70, 25)
        with c2:
            s_lvl = st.selectbox("Seniority", ["Junior", "Senior"])
            s_exp = st.number_input("Experience (Years)", 0, 40, 2)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("CALCULATE & COMPARE")

#Hesap kısmı
if submitted:
    if not s_job or not s_edu or not s_lvl:
        st.error("⚠️ Please fill all fields!")
    else:
        with st.spinner("Processing..."):
            time.sleep(0.4)
            
            job_clean = s_job.lower()
            
            edu_map = {
                "Unknown": 0, 
                "High School": 1, 
                "Bachelor's Degree": 2, 
                "Master's Degree": 3, 
                "PhD": 4
            }
            edu_score = edu_map.get(s_edu, 0) # Varsayılan 0
            
            lvl_score = 0 if s_lvl == "Junior" else 1
            
            # Model tahmin
            job_code = GLOBAL_MEAN_SALARY
            if job_means:
                job_code = job_means.get(job_clean, GLOBAL_MEAN_SALARY)
            
            pred = 0
            if model_active:
                try:
                    # Sıra: [age, years_experience, education, seniority, job_code]
                    input_data = [[s_age, s_exp, edu_score, lvl_score, job_code]]
                    pred = model.predict(input_data)[0]
                except: pass

            # Gerçek veri kontrolü
            matched_row = None
            real_sal = 0
            matches = pd.DataFrame()

            if df_salary is not None:
                matches = df_salary[df_salary['job_title'] == job_clean]
                if not matches.empty:
                    matches = matches.copy()
                    matches['diff'] = (matches['years_experience'] - s_exp).abs()
                    matched_row = matches.sort_values('diff').iloc[0]
                    real_sal = matched_row['salary']
                    
                    if pred == 0: pred = real_sal

            # Sonuç ve grafik gösterimi
            st.markdown(f"""
            <div class="result-card">
                <h3 style="color:#2E86C1; margin:0; font-size:18px;">Estimated Salary</h3>
                <h1 style="color:#1f2937; font-size:48px; margin:5px 0;">${pred:,.0f}</h1>
                <span style="color:#2e7d32; background:#f1f8e9; padding:5px 10px; border-radius:5px; font-weight:bold;">
                    Range: ${pred*0.9:,.0f} - ${pred*1.1:,.0f}
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            col_info, col_chart = st.columns([1, 2])
            
            with col_info:
                st.markdown("### Real Data")
                if matched_row is not None:
                    deg = str(matched_row.get('education_level', '-')).title()
                    st.markdown(f"""
                    <div class="metric-card">
                        <b>👤 Closest Peer Found:</b><br>
                        <span>Role: {s_job}</span><br>
                        <span>Exp: {int(matched_row['years_experience'])} Years</span><br>
                        <span>Degree: {deg}</span>
                        <hr style="margin: 8px 0; border-top: 1px solid #ccc;">
                        <b>Actual Salary:</b> <br>
                        <span style="font-size: 22px; color: #d32f2f !important; font-weight:bold;">${real_sal:,.0f}</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
            with col_chart:
                st.markdown("### Market Distribution")
                if not matches.empty:
                    chart_df = matches[['years_experience', 'salary']]
                    
                    base = alt.Chart(chart_df).mark_circle(size=100, opacity=0.5, color='#2E86C1').encode(
                        x=alt.X('years_experience', title='Experience (Years)'),
                        y=alt.Y('salary', title='Salary ($)'),
                        tooltip=[
                            alt.Tooltip('years_experience', title='Experience (Years)'),
                            alt.Tooltip('salary', title='Salary ($)', format=',.0f')
                        ]
                    )
                    
                    you_data = pd.DataFrame({'years_experience':[s_exp], 'salary':[pred]})
                    you = alt.Chart(you_data).mark_circle(color='red', size=300, opacity=1).encode(
                        x='years_experience', 
                        y='salary', 
                        tooltip=[
                            alt.Tooltip('years_experience', title='Your Experience'),
                            alt.Tooltip('salary', title='Predicted Salary', format=',.0f')
                        ]
                    )
                    
                    st.altair_chart((base+you).interactive(), use_container_width=True)
                else:
                    st.warning("Not enough data to display distribution chart.")

st.markdown("<br><br>", unsafe_allow_html=True)