<details>
  <summary>TÜRKÇE</summary>

# Raw Veri Klasörü (`data/raw`)

Bu klasör, projede kullanılan **ham (raw) veri setlerinin** yerleştirileceği yerdir.  
Telif ve lisans koşulları nedeniyle Kaggle’dan indirilen orijinal CSV dosyaları **repoya eklenmemiştir**.

Bu repo yalnızca:
- işlenmiş / birleştirilmiş veri setini (`data/processed/main_salary_dataset.csv`)  
- ve bu işleme adımlarını anlatan notebook ve raporları içerir.

---

## Kullanılan Ham Veri Setleri (Kaggle)

Projede kullanılan ham veri setleri:

1. **Salary Data** – by *Mohith Sai Ram Reddy*  
   Kaggle link:  
   https://www.kaggle.com/datasets/mohithsairamreddy/salary-data  

   Bu projede önerilen yerel dosya adı:  
   `salary_data.csv`

2. **Salary by Job Title and Country** – by *Amirmahdi Abbootalebi*  
   Kaggle link:  
   https://www.kaggle.com/datasets/amirmahdiabbootalebi/salary-by-job-title-and-country  

   Bu projede önerilen yerel dosya adı:  
   `salary_by_jobtitle_country.csv`

---

## Ham Veriyi Nasıl İndirip Yerleştirebilirsiniz?

1. Yukarıdaki Kaggle linklerine gidin.
2. Giriş yaptıktan sonra ilgili veri setlerini **CSV formatında** indirin.
3. Bu klasör yapısını oluşturun (yoksa `raw` klasörünü siz oluşturun):

   ```text
   data/
     raw/
       salary_data.csv
       salary_by_jobtitle_country.csv
     processed/
       main_salary_dataset.csv

4. Notebooklar ve veri işleme pipeline’ı bu dosya adlarını kullanarak ham veriyi okuyacaktır (özellikle notebooks/01_data_preprocessing.ipynb).

## İşlenmiş Veri ile İlişkisi

- Ham veri setleri yukarıdaki iki Kaggle kaynağından alınır.
- Veri temizleme, birleştirme ve özellik standardizasyonu adımları sonucunda,
  **birleşik ve temiz ana veri seti** şu dosyaya kaydedilmiştir:

  data/processed/main_salary_dataset.csv

Bu sürecin ayrıntılı açıklaması için:
- notebooks/01_data_preprocessing.ipynb
- reports/01_data_processing.md

dosyalarına bakabilirsiniz.

---

## Lisans ve Kullanım Notu

- Ham veri setlerinin tüm hakları, ilgili Kaggle veri seti sahiplerine aittir.
- Bu repo **eğitim ve akademik kullanım** için hazırlanmıştır.
- Herhangi bir yayında veya projede bu verileri kullanırken lütfen:
  - Kaggle veri seti sayfalarında belirtilen lisans koşullarına uyun.
  - Orijinal veri seti sahiplerine atıf verin.


<details>
  <summary>ENGLISH</summary>

# Raw Data Folder (`data/raw`)

This folder is intended to store the **raw datasets** used in the project.  
Due to copyright and licensing restrictions, the original CSV files downloaded from Kaggle are **not included** in this repository.

This repo only contains:
- the processed / merged dataset (`data/processed/main_salary_dataset.csv`)
- and the notebooks and reports describing all preprocessing steps.

---

## Raw Datasets Used (Kaggle)

The project uses the following raw datasets:

1. **Salary Data** – by *Mohith Sai Ram Reddy*  
   Kaggle link:  
   https://www.kaggle.com/datasets/mohithsairamreddy/salary-data  

   Suggested local filename:  
   `salary_data.csv`

2. **Salary by Job Title and Country** – by *Amirmahdi Abbootalebi*  
   Kaggle link:  
   https://www.kaggle.com/datasets/amirmahdiabbootalebi/salary-by-job-title-and-country  

   Suggested local filename:  
   `salary_by_jobtitle_country.csv`

---

## How to Download and Place the Raw Data

1. Visit the Kaggle links listed above.
2. After logging in, download the datasets in **CSV format**.
3. Create the folder structure below (create the `raw` folder manually if it does not already exist):

   data/
     raw/
       salary_data.csv
       salary_by_jobtitle_country.csv
     processed/
       main_salary_dataset.csv

4. The notebooks and preprocessing pipeline will read the raw data using these filenames  
   (especially notebooks/01_data_preprocessing.ipynb).

---

## Relation to the Processed Data

- The raw datasets come from the two Kaggle sources listed above.
- After cleaning, merging, and feature standardization steps,
  the **unified and cleaned main dataset** is saved here:

  data/processed/main_salary_dataset.csv

For a detailed explanation of this process, see:
- notebooks/01_data_preprocessing.ipynb
- reports/01_data_processing.md

---

## License and Usage Notice

- All rights for the raw data belong to the respective Kaggle dataset authors.
- This repository is intended for **educational and academic** use.
- When using these datasets in any project or publication, please:
  - Follow the licensing terms stated on the corresponding Kaggle dataset pages.
  - Provide proper attribution to the original dataset creators.

</details>

