<details>
  <summary>TÜRKÇE</summary>

# 02 – Model Eğitimi ve Performans Analizi Raporu

Bu rapor, temizlenmiş ve işlenmiş maaş veri seti (`data/processed/main_salary_dataset.csv`) kullanılarak geliştirilen Makine Öğrenmesi (Machine Learning) modelinin eğitim sürecini, kullanılan algoritmaları, özellik mühendisliği (feature engineering) adımlarını ve elde edilen performans sonuçlarını belgelemektedir.

Amaç, çalışanların demografik ve mesleki özelliklerine (yaş, deneyim, eğitim, unvan vb.) dayanarak piyasa maaş beklentisini yüksek doğrulukla tahmin eden bir regresyon modeli oluşturmaktır. Modelin son versiyonunda, mesleklerin maaş üzerindeki etkisini daha iyi yansıtmak adına **Target Encoding** tekniği kullanılmıştır.

---

# 📌 Modelleme Sürecinin Ayrıntıları

---

## 1. Veri Hazırlığı ve Özellik Mühendisliği (Feature Engineering)

Modelin sayısal verilerle çalışabilmesi için kategorik değişkenler makine diline çevrilmiştir. Önceki iterasyonlarda kullanılan Label Encoding yerine, modelin başarısını artırmak için meslek grubunda Target Encoding tercih edilmiştir.

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

2.  **Target Encoding (Hedef Kodlama):**
    * **İş Unvanı (`job_title`):** Meslek isimlerine rastgele sayılar (ID) atamak yerine, her mesleğin eğitim veri setindeki **ortalama maaş değeri** hesaplanarak bu değerle kodlama yapılmıştır.
    * Bu yöntem, modelin "Yazılım Mühendisi" ile "Satış Danışmanı" arasındaki ekonomik değer farkını daha net anlamasını sağlamıştır.
    * *Not:* Data Leakage (Veri Sızıntısı) riskini önlemek için ortalamalar sadece eğitim (train) seti üzerinden hesaplanmıştır.

---

## 2. Model Seçimi ve Konfigürasyonu

Problemin bir regresyon problemi olması ve veri setindeki ilişkilerin doğrusal olmayabileceği (non-linear) varsayımıyla **Random Forest Regressor** algoritması tercih edilmiştir.

### Neden Random Forest?
* Target Encoding ile üretilen sürekli değişkenleri ve hiyerarşik yapıları iyi modeller.
* Overfitting (aşırı öğrenme) riskini yönetebilir.
* Hangi özelliğin maaş üzerinde ne kadar etkili olduğunu (Feature Importance) gösterir.

### Hiperparametreler:
* **n_estimators:** 100
* **random_state:** 42
* **Test Split:** %20 Test, %80 Eğitim.

---

## 3. Performans Değerlendirmesi

Modelin başarısı, test verisi üzerinde yapılan tahminlerin gerçek değerlerle karşılaştırılmasıyla ölçülmüştür. Elde edilen son sonuçlar modelin yüksek bir genelleme kapasitesine ulaştığını göstermektedir.

### Metrikler ve Sonuçlar:

| Metrik | Değer | Anlamı |
|--------|-------|--------|
| **R² Score** | **0.8904** | Model, maaş değişimlerinin **%89'unu** doğru açıklayabilmektedir. Bu, çok yüksek bir başarı oranıdır. |
| **MAE (Mean Absolute Error)** | **11,546.42 $** | Modelin tahminleri gerçek maaştan ortalama **11.5 bin dolar** sapma gösterebilir. |

Target Encoding geçişiyle birlikte R² skoru artmış ve hata payı düşmüştür.

---

## 4. Özellik Önem Düzeyleri (Feature Importance)

Target Encoding sonrası modelin karar mekanizmasındaki ağırlıklar değişmiş, iş unvanının önemi artmıştır.

| Özellik (Feature) | Önem Düzeyi (Yaklaşık) | Yorum |
|-------------------|------------------------|-------|
| **Years of Experience** | **0.7406 (%74.1)** | Halen en baskın faktördür. Deneyim arttıkça maaş ciddi oranda artmaktadır. |
| **Job Title** | **0.1853 (%18.5)** | **Kritik Değişim:** Model artık mesleğin kendisine yaklaşık %18.5 oranında önem vermektedir. |
| **Age** | **0.0484 (%4.8)** | Yaş faktörünün etkisi ikincil planda kalmıştır. |
| **Education Level** | **0.0177 (%1.8)** | Eğitim seviyesi maaş üzerinde marjinal bir etkiye sahiptir. |
| **Seniority Level** | **0.0081 (%0.8)** | Deneyim yılı zaten baskın olduğu için, bu etiket model için daha az ayırt edicidir. |

---

## 5. Çıktılar ve Kayıt

Eğitim süreci tamamlandıktan sonra, tekrar kullanıma hazır hale getirmek için model ve gerekli sözlükler kaydedilmiştir.

* **Model Dosyası:** `models/salary_model_target_encoded.pkl`
* **Meslek Ortalamaları:** `models/job_title_means.pkl` (Tahmin sırasında meslek kodlamak için)
* **Genel Ortalama:** `models/global_mean_salary.pkl` (Bilinmeyen meslekler için yedek değer)

</details>


<details>
  <summary>ENGLISH</summary>

# 02 – Model Training and Performance Analysis Report

This report documents the training process, algorithms used, feature engineering steps, and performance results of the Machine Learning model developed using the cleaned and processed salary dataset (`data/processed/main_salary_dataset.csv`).

The objective is to create a regression model that predicts market salary expectations with high accuracy. In this final iteration, **Target Encoding** was implemented for job titles to better capture the economic weight of different professions.

---

# 📌 Details of the Modeling Process

---

## 1. Data Preparation and Feature Engineering

Categorical variables were transformed into numerical formats suitable for machine learning. To improve model interpretability and performance, Target Encoding was chosen over Label Encoding for the job title feature.

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

2.  **Target Encoding:**
    * **Job Title (`job_title`):** Instead of assigning arbitrary IDs, each job title was encoded using the **mean salary** of that title derived from the training set.
    * This allows the model to understand the specific economic value associated with roles like "Software Engineer" vs. "Sales Associate".
    * *Note:* Means were calculated on the training set only to prevent data leakage.

---

## 2. Model Selection and Configuration

The **Random Forest Regressor** algorithm was selected due to its robustness and ability to handle non-linear relationships.

### Why Random Forest?
* Handles the continuous features generated by Target Encoding effectively.
* Robust against overfitting compared to single decision trees.
* Provides clear insights into Feature Importance.

### Hyperparameters:
* **n_estimators:** 100
* **random_state:** 42
* **Test Split:** 20% Test, 80% Train.

---

## 3. Performance Evaluation

Success was measured by comparing predictions on the test set against actual values. The final results demonstrate high predictive capability.

### Metrics and Results:

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **R² Score** | **0.8904** | The model explains **89%** of the variance in salaries, indicating a very strong fit. |
| **MAE (Mean Absolute Error)** | **$11,546.42** | On average, predictions deviate by about **$11.5k** from actual salaries. |

With the transition to Target Encoding, the R² score has improved, and the error rate has decreased.

---

## 4. Feature Importance Analysis

With Target Encoding, the weight distribution of features shifted, giving more importance to the job title.

| Feature | Importance (Approx) | Comment |
|---------|---------------------|---------|
| **Years of Experience** | **0.7406 (74.1%)** | Remains the most dominant factor determining salary. |
| **Job Title** | **0.1853 (18.5%)** | **Significant Role:** The model now assigns ~18.5% importance to the specific job role. |
| **Age** | **0.0484 (4.8%)** | Age has a secondary impact. |
| **Education Level** | **0.0177 (1.8%)** | Education level has a marginal effect. |
| **Seniority Level** | **0.0081 (0.8%)** | Since years of experience covers seniority, this label is less distinctive. |

---

## 5. Outputs and Saving

The trained model and necessary artifacts were saved for deployment.

* **Model File:** `models/salary_model_target_encoded.pkl`
* **Job Means Dictionary:** `models/job_title_means.pkl` (For encoding inputs during prediction)
* **Global Mean:** `models/global_mean_salary.pkl` (Fallback for unknown job titles)

</details>