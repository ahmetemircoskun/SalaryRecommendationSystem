# AI-Based Salary Prediction System / Yapay Zeka Tabanlı Maaş Tahmin Sistemi

**Gazi University - Group 15**

![Project Banner](https://img.shields.io/badge/Status-Active-success?style=flat-square) ![Python](https://img.shields.io/badge/Language-Python-blue?style=flat-square) ![Machine Learning](https://img.shields.io/badge/Focus-Machine%20Learning-orange?style=flat-square)

## 📖 Table of Contents / İçindekiler
1. [Project Description (Proje Açıklaması)](#project-description--proje-açıklaması)
2. [Key Features (Temel Özellikler)](#key-features--temel-özellikler)
3. [System Architecture (Sistem Mimarisi)](#system-architecture--sistem-mimarisi)
4. [Screenshots (Ekran Görüntüleri)](#screenshots--ekran-görüntüleri)
5. [Installation & Usage (Kurulum ve Kullanım)](#installation--usage--kurulum-ve-kullanım)
6. [Contact (İletişim)](#contact--iletişim)

---

## 1. Project Description / Proje Açıklaması

### 🇬🇧 English
This project is an **Artificial Intelligence-supported web application** designed to estimate fair salary ranges for employees based on their professional profiles. By leveraging machine learning algorithms trained on extensive market data, the system analyzes key variables such as **Job Title, Education Level, Seniority, Age, and Years of Experience**.

Beyond simple prediction, the system offers a comparative analysis tool. It visualizes the user's position within the current market distribution and identifies the "Closest Peer" from the dataset to provide a realistic benchmark. This tool aims to assist HR professionals and job seekers in making data-driven financial decisions.

### 🇹🇷 Türkçe
Bu proje, çalışanların profesyonel profillerine dayanarak adil maaş aralıklarını tahmin etmek için tasarlanmış **Yapay Zeka destekli bir web uygulamasıdır**. Sistem, geniş piyasa verileri üzerinde eğitilmiş makine öğrenmesi algoritmalarını kullanarak **İş Ünvanı, Eğitim Seviyesi, Kıdem, Yaş ve Deneyim Yılı** gibi temel değişkenleri analiz eder.

Sistem sadece basit bir tahmin sunmakla kalmaz, aynı zamanda karşılaştırmalı bir analiz aracı olarak çalışır. Kullanıcının mevcut piyasa dağılımındaki konumunu görselleştirir ve veri setinden "En Yakın Eşleşen Profili" (Closest Peer) bularak gerçekçi bir referans noktası sunar. Bu araç, İK uzmanlarının ve iş arayanların veriye dayalı finansal kararlar almasına yardımcı olmayı amaçlamaktadır.

---

## 2. Key Features / Temel Özellikler

| Feature (Özellik) | Description (Açıklama) |
| :--- | :--- |
| **Dynamic Data Input** | User-friendly interface for entering detailed career metrics (Title, Degree, etc.). <br> *Detaylı kariyer metriklerinin girildiği kullanıcı dostu arayüz.* |
| **ML-Powered Prediction** | Instant salary estimation with a calculated confidence interval (Min-Max Range). <br> *Hesaplanmış güven aralığı ile anlık maaş tahmini.* |
| **Market Distribution Analysis** | A scatter plot visualization showing where the user stands compared to industry peers. <br> *Kullanıcının sektördeki diğer kişilere göre konumunu gösteren saçılım grafiği.* |
| **Peer Comparison** | Identifies the most similar real-world profile from the dataset for validation. <br> *Doğrulama için veri setinden en benzer gerçek dünya profilini tanımlar.* |

---

## 3. System Architecture / Sistem Mimarisi

The project is built using a robust tech stack designed for data science applications:
* **Core:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (Regression Models)
* **Visualization:** Matplotlib, Seaborn
* **Interface:** Streamlit (assumed based on layout)

---

## 4. Screenshots / Ekran Görüntüleri

### 🔹 Interface & Data Entry (Arayüz ve Veri Girişi)
*Users select their professional details such as Job Title (e.g., Digital Marketing Specialist, UX Designer) and Education level.*
*Kullanıcılar İş Ünvanı ve Eğitim seviyesi gibi profesyonel detaylarını seçerler.*
    ![forms](docs/forms.jpeg)
    ![jobs](docs/jobs.jpeg)


### 🔹 Prediction Results & Analysis (Tahmin Sonuçları ve Analiz)
*The system displays the **Estimated Salary**, a recommended range, and comparative graphs. The red dot represents the user's estimated position.*
*Sistem, **Tahmini Maaşı**, önerilen aralığı ve karşılaştırmalı grafikleri görüntüler. Kırmızı nokta, kullanıcının tahmini konumunu temsil eder.*

  ![grafik](docs/graphic.jpeg)
  ![all](docs/forms.jpeg)
## 5. Installation & Usage / Kurulum ve Kullanım

### Prerequisites (Gereksinimler)
* Python 3.8+
* Git

### Step-by-Step Guide (Adım Adım Rehber)

1.  **Clone the Repository (Repoyu Klonlayın):**
    ```bash
    git clone [https://github.com/ahmetemircoskun/SalaryRecommendationSystem.git](https://github.com/ahmetemircoskun/SalaryRecommendationSystem.git)
    cd SalaryRecommendationSystem
    ```

2.  **Install Dependencies (Bağımlılıkları Yükleyin):**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application (Uygulamayı Çalıştırın):**
    ```bash
    # If using Streamlit / Streamlit kullanılıyorsa:
    streamlit run main.py
    
    # If using standard Python / Standart Python ise:
    python main.py
    ```

---

## 6. Contact / İletişim

**Project Maintainer:** Ahmet Emir Coşkun
**Gazi University - Computer Engineering Department**

For any inquiries or contributions, please open an issue or contact via GitHub.
*Herhangi bir soru veya katkı için lütfen bir 'issue' açın veya GitHub üzerinden iletişime geçin.*
