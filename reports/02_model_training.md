<details>
  <summary>TÜRKÇE</summary>

# 02 – Model Eğitimi ve Performans Analizi Raporu

Bu rapor, temizlenmiş ve işlenmiş maaş veri seti (`data/processed/main_salary_dataset.csv`) kullanılarak geliştirilen Makine Öğrenmesi (Machine Learning) modelinin eğitim sürecini, kullanılan algoritmaları, özellik mühendisliği (feature engineering) adımlarını ve elde edilen performans sonuçlarını belgelemektedir.

Amaç, çalışanların demografik ve mesleki özelliklerine (yaş, deneyim, eğitim, unvan vb.) dayanarak piyasa maaş beklentisini yüksek doğrulukla tahmin eden bir regresyon modeli oluşturmaktır. Eğitilen nihai model ve yardımcı kodlayıcılar `models/` klasörü altına kaydedilmiştir.

---

# 📌 Modelleme Sürecinin Ayrıntıları

---

## 1. Veri Hazırlığı ve Özellik Mühendisliği (Feature Engineering)

Modelin sayısal verilerle çalışabilmesi için kategorik değişkenler makine diline çevrilmiştir. Bu aşamada veri setinin doğasına uygun "Encoding" stratejileri uygulanmıştır.

### Uygulanan Dönüşümler:

1.  **Ordinal Encoding (Sıralı Kodlama):**
    * Hiyerarşik bir sıraya sahip olan veriler, büyüklük küçüklük ilişkisine göre sayıya çevrilmiştir.
    * **Eğitim Seviyesi (`education_level`):**
        * Unknown → 0
        * High School → 1
        * Bachelor → 2
        * Master → 3
        * PhD → 4
    * **Kıdem Seviyesi (`seniority_level`):**
        * Junior → 0
        * Senior → 1

2.  **Label Encoding (Etiket Kodlama):**
    * **İş Unvanı (`job_title`):** 100'den fazla farklı meslek grubu olduğu için ve Random Forest algoritması ağaç tabanlı olduğu için, her mesleğe benzersiz bir sayısal kimlik (ID) atanmıştır. Bu işlem için `sklearn.preprocessing.LabelEncoder` kullanılmıştır.

---

## 2. Model Seçimi ve Konfigürasyonu

Problemin bir regresyon (sayısal tahmin) problemi olması ve veri setindeki ilişkilerin doğrusal olmayabileceği (non-linear) varsayımıyla **Random Forest Regressor** algoritması tercih edilmiştir.

### Neden Random Forest?
* Aykırı değerlere ve gürültülü verilere karşı dirençlidir.
* Overfitting (aşırı öğrenme) riskini tekil karar ağaçlarına göre daha iyi yönetir.
* Özelliklerin önem düzeylerini (Feature Importance) yorumlamaya olanak tanır.

### Hiperparametreler:
* **n_estimators:** 100 (100 adet karar ağacı kullanıldı)
* **random_state:** 42 (Sonuçların tekrarlanabilir olması için sabitlendi)
* **Test Split:** Verinin %20'si test, %80'i eğitim için ayrıldı.

---

## 3. Performans Değerlendirmesi

Modelin başarısı, test verisi üzerinde yapılan tahminlerin gerçek değerlerle karşılaştırılmasıyla ölçülmüştür.

### Metrikler ve Sonuçlar:

| Metrik | Değer | Anlamı |
|--------|-------|--------|
| **R² Score** | **0.8745** | Model, maaş değişimlerinin **%87.5'ini** doğru açıklayabilmektedir. Oldukça yüksek bir başarı oranıdır. |
| **MAE (Mean Absolute Error)** | **~12,509 $** | Modelin tahminleri gerçek maaştan ortalama **12.5 bin dolar** sapma gösterebilir. |

Bu sonuçlar, modelin genel piyasa eğilimlerini çok iyi yakaladığını, ancak nadir görülen bazı uç maaş senaryolarında küçük sapmalar yapabileceğini göstermektedir.

---

## 4. Özellik Önem Düzeyleri (Feature Importance)

Modelin karar verirken hangi özelliklere ne kadar dikkat ettiği analiz edilmiştir.

| Özellik (Feature) | Önem Düzeyi (%) | Yorum |
|-------------------|-----------------|-------|
| **Years of Experience** | **%78.1** | Maaşı belirleyen en baskın faktördür. Deneyim arttıkça maaş doğrudan etkilenmektedir. |
| **Job Title** | **%11.0** | Yapılan işin niteliği ikinci en önemli faktördür. |
| **Age** | **%6.7** | Yaş faktörü deneyimle korele olsa da tek başına etkisi daha düşüktür. |
| **Education Level** | **%3.0** | Eğitim seviyesi maaş üzerinde marjinal bir etkiye sahiptir. |
| **Seniority Level** | **%0.9** | Deneyim yılı zaten baskın olduğu için, bu etiket model için daha az ayırt edici olmuştur. |

---

## 5. Çıktılar ve Kayıt

Eğitim süreci tamamlandıktan sonra, tekrar kullanıma hazır hale getirmek için model ve kodlayıcı disk üzerine kaydedilmiştir.

* **Model Dosyası:** `models/salary_model_random_forest.pkl`
* **Encoder Dosyası:** `models/job_title_encoder.pkl` (Yeni gelen meslek isimlerini kodlamak için gereklidir)

</details>

<details>
  <summary>ENGLISH</summary>

# 02 – Model Training and Performance Analysis Report

This report documents the training process, algorithms used, feature engineering steps, and performance results of the Machine Learning model developed using the cleaned and processed salary dataset (`data/processed/main_salary_dataset.csv`).

The objective is to create a regression model that predicts market salary expectations with high accuracy based on employees' demographic and professional characteristics (age, experience, education, job title, etc.). The final trained model and auxiliary encoders have been saved under the `models/` directory.

---

# 📌 Details of the Modeling Process

---

## 1. Data Preparation and Feature Engineering

Categorical variables were converted into machine-readable numerical formats. Appropriate "Encoding" strategies were applied based on the nature of the data.

### Transformations Applied:

1.  **Ordinal Encoding:**
    * Data with a hierarchical order was converted to numbers respecting their rank.
    * **Education Level (`education_level`):**
        * Unknown → 0
        * High School → 1
        * Bachelor → 2
        * Master → 3
        * PhD → 4
    * **Seniority Level (`seniority_level`):**
        * Junior → 0
        * Senior → 1

2.  **Label Encoding:**
    * **Job Title (`job_title`):** Since there are over 100 unique job titles and Random Forest is a tree-based algorithm, a unique numerical ID was assigned to each profession using `sklearn.preprocessing.LabelEncoder`.

---

## 2. Model Selection and Configuration

The **Random Forest Regressor** algorithm was chosen as this is a regression problem and the relationships within the dataset may be non-linear.

### Why Random Forest?
* Resistant to outliers and noisy data.
* Manages the risk of overfitting better than single decision trees.
* Allows for interpretation of Feature Importance.

### Hyperparameters:
* **n_estimators:** 100 (100 decision trees used)
* **random_state:** 42 (Fixed for reproducibility)
* **Test Split:** 20% of data reserved for testing, 80% for training.

---

## 3. Performance Evaluation

The model's success was measured by comparing predictions on the test data against actual values.

### Metrics and Results:

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **R² Score** | **0.8745** | The model explains **87.5%** of the variance in salaries. This indicates a high success rate. |
| **MAE (Mean Absolute Error)** | **~$12,509** | On average, the model's predictions deviate by about **$12.5k** from the actual salary. |

These results indicate that the model captures general market trends very well, though it may have minor deviations in rare salary scenarios.

---

## 4. Feature Importance Analysis

An analysis was conducted to determine which features the model prioritizes when making decisions.

| Feature | Importance (%) | Comment |
|---------|----------------|---------|
| **Years of Experience** | **78.1%** | The most dominant factor determining salary. Salary is directly affected as experience increases. |
| **Job Title** | **11.0%** | The nature of the job is the second most important factor. |
| **Age** | **6.7%** | While age correlates with experience, its standalone effect is lower. |
| **Education Level** | **3.0%** | Education level has a marginal effect on salary prediction. |
| **Seniority Level** | **0.9%** | Since years of experience is already dominant, this label was less distinctive for the model. |

---

## 5. Outputs and Saving

After the training process was completed, the model and encoder were saved to disk for re-use.

* **Model File:** `models/salary_model_random_forest.pkl`
* **Encoder File:** `models/job_title_encoder.pkl` (Required to encode incoming job titles)

</details>
