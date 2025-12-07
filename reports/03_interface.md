<details>
  <summary>TÜRKÇE</summary>

# 03 – Arayüz Geliştirme ve Sistem Entegrasyonu Raporu

Bu rapor, **Grup 15** tarafından geliştirilen "Yapay Zeka Tabanlı Maaş Tahmin Sistemi"nin son kullanıcı arayüzünü (Web UI), sistem mimarisini ve entegrasyon süreçlerini belgelemektedir. Projenin bu aşamasında, temizlenen veri seti ve eğitilen model, etkileşimli bir web uygulamasına dönüştürülmüştür.

Uygulama, Python tabanlı **Streamlit** framework'ü kullanılarak geliştirilmiş olup, gerçek zamanlı tahmin ve veri görselleştirme yeteneklerine sahiptir.

---

# 📌 Sistem Mimarisi ve Teknik Altyapı

---

## 1. Teknoloji Yığını (Tech Stack)

Arayüz ve backend mantığı tek bir bütünleşik yapı içinde kurgulanmıştır:

- **Frontend/Backend:** Streamlit (Python)
- **Veri İşleme:** Pandas, NumPy
- **Model Yükleme:** Joblib
- **Görselleştirme:** Altair (İnteraktif Grafikler)

Bu mimari, kurulum gerektirmeyen (Web-based) ve platform bağımsız bir yapı sunarak Milestone Raporunda belirtilen hedefleri karşılamaktadır.

---

## 2. Model ve Encoder Entegrasyonu

Eğitilen **Random Forest Regressor** modeli ve yardımcı dosyalar sisteme dinamik olarak entegre edilmiştir. `@st.cache_resource` kullanılarak şu varlıklar hafızaya yüklenir:

1.  **salary_model_target_encoded.pkl**: Ana tahmin modeli.
2.  **job_title_means.pkl**: Kategorik meslek verilerini sayısal değerlere dönüştüren Target Encoding haritası.
3.  **main_salary_dataset.csv**: Karşılaştırmalı analiz için kullanılan veri seti.

Bu ön yükleme stratejisi (Caching), sistemin **milisaniyeler içinde** yanıt vermesini sağlar.

---

## 3. Kullanıcı Arayüzü (UI) Tasarımı

Kullanıcı deneyimini (UX) artırmak için özel tasarımlar uygulanmıştır:

- **Ghost Mode (Hayalet Modu):** Varsayılan menüler ve alt bilgiler CSS ile gizlenmiş, kurumsal bir görünüm elde edilmiştir.
- **Form Tabanlı Giriş:** Kullanıcı verileri `st.form` yapısı içinde toplanır. Sadece "HESAPLA" butonuna basıldığında işlem yapılır, bu da performansı artırır.
- **Sonuç Kartları:** Sonuçlar, özelleştirilmiş HTML/CSS kartları içinde sunulur.

---

# ⚙️ Algoritma ve İş Mantığı

Sistem, hibrit bir karar mekanizması işletir.

---

## 1. Girdi İşleme (Preprocessing)

Kullanıcı verileri modele uygun hale getirilir:

- **Eğitim:** Ordinal Encoding (`Unknown:0` ... `PhD:4`).
- **Kıdem:** Binary Encoding (`Junior:0`, `Senior:1`).
- **Meslek:** Target Encoding. Seçilen mesleğin veri setindeki ortalama maaş değeri modele verilir.

---

## 2. Maaş Tahmin Motoru

Hazırlanan girdi vektörü `[Age, Experience, Education, Seniority, Job_Code]` Random Forest modeline gönderilir ve **Tahmini Maaş** hesaplanır. Ayrıca **±%10** güven aralığı sunulur.

---

## 3. Gerçek Veri Eşleştirme (Real Data Matching)

Sistem, yapay zeka tahminini kanıtlamak için şu algoritmayı kullanır:

1.  Seçilen mesleğe (`job_title`) ait tüm kayıtlar filtrelenir.
2.  Kullanıcının **deneyim yılına** en yakın olan gerçek kişi bulunur.
3.  Bulunan "En Yakın Emsal" profilinin gerçek maaşı ekrana getirilir.

---

# 📊 Görselleştirme

Sonuç ekranı iki ana görsel içerir:

### A) Piyasa Dağılım Grafiği
**Altair** ile çizilen interaktif grafik:
- **Mavi Noktalar:** Gerçek çalışanlar.
- **Kırmızı Nokta (YOU):** Kullanıcının tahmin edilen konumu.

### B) Akıllı Metrik Kartları
Tahmini maaş, maaş aralığı ve gerçek veri kıyaslaması kartlar halinde sunulur.

---

# 📈 Sonuç

Milestone Raporunda hedeflenen "Güvenilir bir makine öğrenmesi modeli ve basit bir web arayüzü" hedefine ulaşılmıştır.

- **Veri:** Ham veri temizliği sonrası elde edilen **~1.500 adet nitelikli kayıt** entegre edildi.
- **Model:** Random Forest algoritması başarıyla canlıya alındı.
- **Arayüz:** Gazi Üniversitesi kurumsal kimliğine uygun profesyonel bir arayüz geliştirildi.
</details>

<details>
  <summary>ENGLISH</summary>

# 03 – Interface Development and System Integration Report

This report documents the final user interface (Web UI), system architecture, and integration processes of the "AI-Based Salary Estimation and Recommendation System" developed by **Group 15**. In this phase of the project, the previously cleaned dataset and the trained Machine Learning model have been transformed into an interactive and user-friendly web application.

The application is built using the Python-based **Streamlit** framework, featuring real-time prediction, data visualization, and comparative analysis capabilities.

---

# 📌 System Architecture and Technical Infrastructure

---

## 1. Tech Stack

The interface and backend logic are orchestrated within a unified structure to ensure portability and ease of use:

- **Frontend/Backend Framework:** Streamlit (Python)
- **Data Processing:** Pandas, NumPy
- **Model Loading:** Joblib
- **Visualization:** Altair (Interactive Charts)

This architecture provides a web-based, platform-independent solution, meeting the "Access for Individuals and Employers" objective outlined in the Milestone Report.

---

## 2. Model and Encoder Integration

The trained **Random Forest Regressor** and auxiliary files are dynamically integrated into the system. Upon application startup, the `@st.cache_resource` decorator loads the following assets into memory to optimize performance:

1.  **salary_model_target_encoded.pkl**: The primary prediction model trained on the processed dataset.
2.  **job_title_means.pkl**: A dictionary map used for **Target Encoding**, converting categorical job titles into numerical values based on mean salaries.
3.  **main_salary_dataset.csv**: The unified dataset used for comparative analysis (Real Data Matching).

This caching strategy prevents reloading the heavy model files for every user query, ensuring the system responds in **milliseconds**.

---

## 3. User Interface (UI) Design and Experience

To maximize User Experience (UX), "Ghost Mode" and "Clean UI" principles were applied via custom CSS injection.

### Design Features:
- **Ghost Mode:** Streamlit’s default menus, "Deploy" buttons, and watermarks are hidden to achieve a fully custom application look.
- **Form-Based Input:** User inputs are collected within an `st.form` structure. This prevents page reruns on every selection, triggering execution only when the "CALCULATE" button is pressed. This structure increased system stability significantly.
- **Responsive Cards:** Results are presented in HTML/CSS customized "Result Cards" and "Metric Cards" for better readability.

---

# ⚙️ Algorithm and Business Logic

The system does not merely output a raw prediction; it operates a hybrid decision mechanism to ensure accuracy and relevance.

---

## 1. Input Processing and Encoding Pipeline

Raw inputs collected from the user (e.g., "Master's Degree", "Senior") are converted into numerical vectors understood by the model:

- **Education:** Ordinal Encoding applied (`Unknown:0` ... `PhD:4`).
- **Seniority:** Binary Encoding applied (`Junior:0`, `Senior:1`).
- **Job Title:** Target Encoding applied. The average salary of the selected job in the training set is passed as input. A `GLOBAL_MEAN_SALARY` fallback is used for unknown titles.

---

## 2. Salary Prediction Engine

The prepared input vector `[Age, Experience, Education_Score, Seniority_Score, Job_Code]` is fed into the Random Forest model.

- The model output constitutes the **Estimated Salary**.
- A Confidence Interval is calculated as a **±10%** band around the prediction to reflect market variance.

---

## 3. Real Data Matching Algorithm (The "Proof" System)

The system includes a verification feature called "Real Data Proof":

1.  **Filtering:** The system filters the dataset for the user's selected `job_title`.
2.  **Matching:** It finds the record with the closest **years_experience** to the user by minimizing the difference (`diff`).
3.  **Display:** The actual salary, education level, and experience of this "Closest Peer" are displayed.
4.  **Analysis:** The Delta between the AI prediction and real data is calculated to provide "Above/Below Market" insights.

---

# 📊 Visualization and Analytical Outputs

The result screen consists of two main visual components:

### A) Market Distribution Chart
An interactive Scatter Plot is rendered using **Altair**:
- **Blue Dots:** Represent real employees in the dataset. Tooltips show details (Experience, Salary).
- **Red Dot (YOU):** Represents the user's predicted position.

This chart visually proves the user's position within the general market (identifying if they are an outlier).

### B) Smart Metric Cards
- **Estimated Salary:** Main result shown in large typography.
- **Range:** Lower and upper salary bounds.
- **Real Data:** The actual salary of the most similar real person from the database for validation.

---

# 📈 Project Conclusion

The goal of creating a "reliable machine learning model and a simple web interface" set in the Milestone Report has been successfully achieved.

- **Data:** **~1,500 high-quality, cleaned and verified records** successfully integrated.
- **Model:** Random Forest algorithm successfully deployed with Target Encoding.
- **Interface:** A professional interface consistent with Gazi University's corporate identity was developed via CSS customizations.

The system has achieved a data-driven and transparent structure that enables both individual career planning and employer salary policy definition.
</details>