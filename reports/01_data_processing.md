# 01 – Veri İşleme ve Temizlik Süreci (Data Processing Report)

Bu rapor, Introduction to Data Science projesi kapsamında kullanılan iki farklı maaş veri setinin (Salary Data ve Salary by Job Title and Country) sistematik biçimde birleştirilmesi, temizlenmesi, normalleştirilmesi ve modellemeye hazır hale getirilmesi için uygulanan tüm yöntemleri ayrıntılı şekilde açıklamaktadır. Süreç boyunca Python, Pandas ve veri ön işleme teknikleri kullanılmış, tüm adımlar notebook ortamında tekrarlanabilir bir pipeline hâline getirilmiştir.

Amaç, farklı kaynaklardan gelen verileri tutarlı, eksiksiz, duplicate içermeyen, uç değerlerden arındırılmış ve istatistiksel olarak güvenilir tek bir ana veri setine dönüştürmektir. Nihai veri seti `data/processed/main_salary_dataset.csv` olarak kaydedilmiştir.

---

# 📌 Veri İşleme Adımlarının Ayrıntılı Açıklaması (Türkçe)

---

## 1. Veri Setlerinin Seçilmesi, Yüklenmesi ve İlk İncelemesi

İki farklı Kaggle veri seti kullanıldı:

1. **salary_data.csv**  
2. **salary_by_jobtitle_country.csv**

Her iki veri seti de yaş, eğitim seviyesi, iş unvanı, deneyim süresi ve maaş gibi modelde kullanacağımız ortak çekirdek özellikleri içeriyordu. Pandas ile dosyalar okunarak:

- toplam satır sayıları,
- kolon isimleri,
- veri tipleri,
- eksik değerlerin dağılımı,
- kategorik değer çeşitliliği

incelenmiştir.

Bu inceleme, kolon isimlerindeki uyumsuzlukları, farklı formatları ve eksik veri yapılarını tespit etmemizi sağlamıştır.

---

## 2. Ortak Şemanın Oluşturulması

Verilerin iki kaynaktan geliyor olması kolon adlarını standartlaştırmayı gerektirmiştir. Modelleme aşamasında Python fonksiyonlarıyla uyumlu olması için bir “uniform schema” belirledik.

Uygulanan dönüşümler:

- Age → age  
- Job Title → job_title  
- Education Level → education_level  
- Years of Experience → years_experience  
- Salary → salary  

Ayrıca tüm veri setlerinde bulunmayan bir field olan **seniority_level** (kıdem seviyesi) kolonunu veri yapısına ekledik ve sonraki adımlarda bu değeri hesapladık.

Bu adım sayesinde iki veri seti aynı kolon yapısına sahip olmuş, birleşmeye hazır hâle gelmiştir.

---

## 3. Seniority Bilgisinin Tekilleştirilmesi ve Tutarlı Bir Kıdeme Dönüştürülmesi

Kıdem bilgisi veri setlerinde tutarlı bir şekilde sunulmuyordu:

- Bir veri setinde `Senior` adıyla 0/1 formatında bulunuyordu.
- Diğer veri setinde iş unvanı içerisinde “Senior …” veya “Junior …” şeklinde geçiyordu.
- Bazı kayıtlarda kıdem bilgisi hiç belirtilmemişti.

Bu nedenle veri bilimsel bir karar mekanizması oluşturduk:

### Kullanılan Yöntemler:
- Text mining: job_title içinde kelime arama  
- Boolean mapping: Senior kolonundan ikili mapping  
- Median salary karşılaştırması: Neutral kayıtların maaş seviyesine bakarak kıdem sınıfı tahmini  

### Kural Seti:
- Senior = 1 → **senior**
- job_title içinde “senior” geçiyorsa → **senior**
- job_title içinde “junior” geçiyorsa → **junior**
- Bilgi yoksa → **junior**

Bu seçimin doğruluğu median maaş analiziyle teyit edildi:

| Seviye | Median maaş |
|--------|-------------|
| Junior | 100,000 |
| Neutral (seviye belirtilmemiş) | 110,000 |
| Senior | 140,000 |

Neutral median maaşının junior’a yakın olması nedeniyle bu grubun “junior” olarak etiketlenmesi **istatistiksel olarak en doğru karar**dır.

---

## 4. Job Title Temizleme, Normalizasyon ve Anlamsal Birleştirme

Data Quality Report aşamasında iş unvanlarında:

- yazım hataları (ör. “juniour”),
- varyasyonlar (ör. “back end developer” vs “backend developer”),
- anlamca aynı fakat farklı yazılmış pozisyonlar,
- eksik veya yanlış girişler,

tespit edilmiştir.

Bu nedenle gelişmiş bir “job title normalization pipeline” geliştirilmiştir.

### Uygulanan Temizlik Adımları:
#### **A) Yazım hatası düzeltme (typo correction)**
Örnekler:
- “juniour hr coordinator” → “junior hr coordinator”
- “social media man” → “social media manager”

#### **B) Varyasyonları tekilleştirme**
- “customer service rep” → “customer service representative”
- “front end developer” → “frontend developer”
- “back end developer” → “backend developer”
- “full stack engineer” → “fullstack engineer”

#### **C) Anlamdaş pozisyon birleştirmeleri**
- “developer” → “software developer”
- “scientist” → “research scientist”
- “it project manager” → “project manager”

Bu işlemler sonucunda benzersiz unvan sayısı **125 → 118**’e düşmüş, veri çok daha tutarlı hâle gelmiştir.

---

## 5. Education Level Normalizasyonu

Veri setlerindeki eğitim seviyeleri farklı formatlarda olduğundan tek bir standarda çevrilmiştir:

high_school, bachelor, master, phd, unknown


Eksik değerler `"unknown"` etiketiyle doldurulmuştur.

---

## 6. Sayısal Kolonların Temizlenmesi ve Tür Dönüşümleri

age, years_experience ve salary kolonlarında:

- sayısal olmayan karakterler temizlenmiş,
- tüm değerler sayıya dönüştürülmüş,
- dönüştürülemeyenler NaN yapılmıştır.

Eksik sayısal değerler median ile doldurulmuştur.

Bu adım veri setindeki istatistiksel tutarlılığı artırmıştır.

---

## 7. Mantık Kontrolleri ve Aykırı Değerlerin Filtrelenmesi

Aşağıdaki kurallarla mantık dışı kayıtlar çıkarılmıştır:

- age ∉ [18, 70] → silindi
- years_experience ∉ [0, 50] → silindi
- salary ≤ 0 → silindi
- salary üst %1 dilim → **uç değer olarak çıkarıldı**  
  (Ham veri 99. persentil: 210,000 → düzenlenmiş: 200,000)

Bu adım modelde uç değerlerin yarattığı dengesizlikleri önlemek için gereklidir.

---

## 8. Eksik Değer Yönetimi

- Salary eksik olan kayıtlar → tamamen çıkarıldı  
- Kategorik eksikler → “unknown”  
- Sayısal eksikler → median  

Bu strateji hem bilgi kaybını azaltmış hem de modelin stabil çalışmasını sağlamıştır.

---

## 9. Veri Birleştirme ve Duplicate Temizliği

İki veri seti concat ile birleştirildi.

Duplicate kontrolü şu kolonlarla yapıldı:

age, job_title, education_level, years_experience, salary, seniority_level

Sonuçlar:

- Duplicate (before): **9991**
- Duplicate (after): **0**

Bu adım dataset'in güvenilirliğini büyük ölçüde artırmıştır.

---

## 10. Nihai Veri Seti ve Kalite Özeti

Temizlenmiş veri seti kaydedildi:

data/processed/main_salary_dataset.csv

---

# 📊 Veri Kalitesi ve Çeşitlilik Özeti

### age  
- Benzersiz: 41  
- Ortalama: 35.27  

### job_title  
- Benzersiz: 118  

### education_level  
- bachelor, high_school, master, phd, unknown  

### years_experience  
- Benzersiz: 37  

### salary  
- Benzersiz: 437  
- Ortalama: 112,905  

### seniority_level  
- junior, senior  

---

## 📝 Revizyon Notu

Data Quality Report aşamasında tespit edilen job title tutarsızlıkları düzeltilmiş; typo correction, string normalization ve semantic merging adımları uygulanarak nihai veri seti tekrar oluşturulmuştur.

---

# 01 – Data Processing Report (English Version)

This report documents the full preprocessing pipeline applied to the two salary datasets used in the project. All steps were implemented in Python using Pandas, ensuring a reproducible and structured workflow. The goal is to produce a unified, consistent, clean, duplicate-free, and statistically reliable dataset stored as `data/processed/main_salary_dataset.csv`.

---

## 📌 Detailed Summary of Data Processing Steps (English)

---

### 1. Dataset Loading and Initial Exploration

Two Kaggle datasets were used:

- salary_data.csv  
- salary_by_jobtitle_country.csv  

We inspected:

- column names and data types  
- missing values  
- categorical distributions  
- sample rows  
- schema differences  

This guided the standardization decisions that followed.

---

## 2. Schema Standardization

Columns were aligned to a unified schema:

- Age → age  
- Job Title → job_title  
- Education Level → education_level  
- Years of Experience → years_experience  
- Salary → salary  

We also introduced a new field, **seniority_level**, to harmonize inconsistent seniority information.

Final schema:

age, job_title, education_level, years_experience, salary, seniority_level


---

## 3. Seniority Harmonization

Seniority appeared in two incompatible formats:

- As a binary field (`Senior = 0/1`)  
- Embedded inside job titles (“Senior …”, “Junior …”)  

We unified this into a single seniority_level field using:

### Methods Applied:
- Keyword scanning in job titles  
- Boolean mapping from Senior column  
- Median salary comparison for neutral records  

### Final Rules:
- Senior = 1 → senior  
- job_title contains “senior” → senior  
- job_title contains “junior” → junior  
- no seniority info → junior  

Median salary analysis validated this mapping:

| Level | Median Salary |
|-------|---------------|
| Junior | 100,000 |
| Neutral | 110,000 |
| Senior | 140,000 |

Neutral values were statistically closer to junior, so they were labeled as junior.

---

## 4. Job Title Normalization (Advanced Text Cleaning)

The Data Quality Report revealed multiple issues:

- typos  
- inconsistent spacing  
- semantic duplicates  
- incomplete role names  

We implemented a multi-phase normalization pipeline:

### **A) Typo Correction**
- “juniour hr coordinator” → “junior hr coordinator”
- “social media man” → “social media manager”

### **B) Variation Merging**
- “customer service rep” → “customer service representative”
- “front end developer” → “frontend developer”
- “back end developer” → “backend developer”
- “full stack engineer” → “fullstack engineer”

### **C) Semantic Standardization**
- “developer” → “software developer”
- “scientist” → “research scientist”
- “it project manager” → “project manager”

Unique job titles reduced from **125 → 118**, improving dataset consistency significantly.

---

## 5. Education Level Mapping

Mapped into four unified categories:

high_school, bachelor, master, phd


Missing values were filled as `"unknown"`.

---

## 6. Numeric Cleaning and Type Conversion

`age`, `years_experience`, and `salary` were converted to numeric using coercion.  
Invalid values became NaN and were imputed using the **median**.

---

## 7. Logical Filters and Outlier Removal

We applied domain-specific constraints:

- Age must be between 18–70  
- Years of experience must be 0–50  
- Salary must be greater than 0  
- Top 1% salary outliers removed (210k → 200k)

This improves model robustness by preventing extreme values from skewing distributions.

---

## 8. Handling Missing Data

- Rows missing salary were removed  
- Categorical missing values → “unknown”  
- Numeric missing values → median  

This preserves data volume while ensuring statistical stability.

---

## 9. Dataset Merging and Duplicate Removal

The two datasets were concatenated, then duplicates removed using:

age, job_title, education_level, years_experience, salary, seniority_level


Results:

- Before cleaning: **9991 duplicates**
- After cleaning: **0 duplicates**

This ensures each observation represents a unique sample.

---

## 10. Final Dataset and Quality Summary

The cleaned dataset was saved to:

data/processed/main_salary_dataset.csv


---

# 📊 Data Quality and Feature Diversity Summary

### age  
- Unique: 41  
- Mean: 35.27  
- Range: 21–62  

### job_title  
- Unique: 118  
- Representative titles:  
  backend developer, customer service representative, data scientist, software engineer, fullstack engineer  

### education_level  
bachelor, high_school, master, phd, unknown  

### years_experience  
- Unique: 37  
- Mean: 9.24  

### salary  
- Unique: 437  
- Mean: 112,905  
- Median: 110,000  
- Max (cleaned): 200,000  

### seniority_level  
junior, senior  

---

## 📝 Revision Notes

After reviewing the Data Quality Report, additional normalization and typo correction were applied to job_title values. The dataset was regenerated to reflect these improvements, ensuring maximum consistency and modeling readiness.

