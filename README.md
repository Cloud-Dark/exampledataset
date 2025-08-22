# Example Dataset Collection

Koleksi dataset contoh untuk berbagai domain yang dapat digunakan untuk pembelajaran, pengembangan aplikasi, dan analisis data. Dataset ini mencakup data terstruktur dan tidak terstruktur dalam berbagai format.

## 📋 Daftar Dataset

### 🏥 Healthcare & Medical
- **`eyessick.json`** - Dataset penyakit mata dengan gejala dan ciri visual
- **`healthcare_patients.json`** - Data pasien lengkap dengan diagnosa, obat, dan hasil lab

#### 🔬 Medical Physical Examination Datasets
> **Khusus untuk analisis penyakit berdasarkan ciri fisik dan pemeriksaan klinis**

[![Brain Diseases](https://img.shields.io/badge/🧠%20Brain%20Diseases-6%20penyakit-blue.svg)](#brain-diseases-dataset)
[![Eye Diseases](https://img.shields.io/badge/👁%20Eye%20Diseases-7%20penyakit-green.svg)](#eye-diseases-detailed-dataset)
[![Oral Diseases](https://img.shields.io/badge/👅%20Oral%20Diseases-7%20penyakit-orange.svg)](#tongue-oral-diseases-dataset)
[![Skin Diseases](https://img.shields.io/badge/🫱%20Skin%20Diseases-7%20penyakit-red.svg)](#skin-diseases-dataset)
[![General Diseases](https://img.shields.io/badge/⚕️%20General%20Diseases-7%20penyakit-purple.svg)](#general-physical-examination-dataset)

- **`brain_diseases.json`** - Penyakit neurologis dengan ciri fisik dan gejala neurologis
- **`tongue_oral_diseases.json`** - Penyakit mulut dan lidah dengan ciri visual spesifik  
- **`eye_diseases_detailed.json`** - Penyakit mata dengan pemeriksaan fisik detail
- **`skin_diseases.json`** - Penyakit kulit dengan manifestasi fisik dan lokasi predileksi
- **`general_physical_examination.json`** - Penyakit umum dengan temuan pemeriksaan fisik

### 💻 Information Technology  
- **`it_inventory.csv`** - Inventaris aset IT perusahaan (laptop, server, printer, dll)
- **`software_licenses.json`** - Data lisensi software dengan informasi compliance dan biaya

### 👥 Human Resources
- **`employee_reviews.txt`** - Review performa karyawan dalam format teks tidak terstruktur
- **`hr_attendance_log.txt`** - Log kehadiran karyawan dengan detail jam kerja dan keterlambatan

## 🗂️ Format Dataset

### JSON (Structured)
```json
{
  "id": "unique_identifier",
  "field1": "value",
  "field2": ["array", "values"],
  "nested_object": {
    "sub_field": "value"
  }
}
```

### CSV (Tabular)
```csv
column1,column2,column3
value1,value2,value3
value1,value2,value3
```

### TXT (Unstructured)
```
Plain text format with natural language content
Suitable for text processing and NLP tasks
```

## 🚀 Cara Penggunaan

### 1. Clone atau Download Repository
```bash
git clone https://github.com/your-repo/exampledataset.git
cd exampledataset
```

### 2. Membaca Dataset JSON dengan Python
```python
import json

# Membaca dataset penyakit mata
with open('healthcare/eyessick.json', 'r', encoding='utf-8') as f:
    eye_diseases = json.load(f)

# Menampilkan data penyakit pertama
print(eye_diseases[0]['nama_penyakit'])
print(eye_diseases[0]['gejala_pasien'])

# Membaca dataset penyakit otak
with open('healthcare/brain_diseases.json', 'r', encoding='utf-8') as f:
    brain_diseases = json.load(f)

# Analisis ciri fisik stroke
stroke = brain_diseases[0]  # stroke_iskemik
print(f"Penyakit: {stroke['nama_penyakit']}")
print("Ciri fisik wajah:")
for ciri in stroke['ciri_fisik_wajah']:
    print(f"- {ciri}")
    
# Membaca dataset penyakit kulit untuk deteksi melanoma
with open('healthcare/skin_diseases.json', 'r', encoding='utf-8') as f:
    skin_diseases = json.load(f)
    
melanoma = next(d for d in skin_diseases if d['nama_penyakit'] == 'melanoma_maligna')
print("Kriteria ABCDE untuk melanoma:")
for kriteria in melanoma['kriteria_ABCDE']:
    print(f"- {kriteria}")
```

### 3. Membaca Dataset CSV dengan Pandas
```python
import pandas as pd

# Membaca inventaris IT
it_inventory = pd.read_csv('it/it_inventory.csv')

# Menampilkan 5 baris pertama
print(it_inventory.head())

# Filter berdasarkan kategori
laptops = it_inventory[it_inventory['asset_type'] == 'Laptop']
```

### 4. Memproses Dataset Text
```python
# Membaca file text review karyawan
with open('hr/employee_reviews.txt', 'r', encoding='utf-8') as f:
    reviews = f.read()

# Split berdasarkan separator
employee_sections = reviews.split('=' * 80)

# Extract informasi tertentu
for section in employee_sections:
    if 'EMPLOYEE ID:' in section:
        print("Processing employee data...")
```

## 📊 Detail Dataset

### Healthcare Datasets

#### `eyessick.json` - Penyakit Mata
- **Format**: JSON Array
- **Jumlah Records**: 7 penyakit
- **Fields**: 
  - `id`: ID unik penyakit
  - `nama_penyakit`: Nama penyakit
  - `deskripsi_singkat`: Deskripsi medis
  - `gejala_pasien`: Array gejala yang dirasakan
  - `ciri_visual`: Array ciri visual yang terlihat
- **Use Cases**: Sistem diagnosa, aplikasi kesehatan, machine learning klasifikasi

#### `healthcare_patients.json` - Data Pasien
- **Format**: JSON Array  
- **Jumlah Records**: 5 pasien
- **Fields**:
  - `patient_id`: ID unik pasien
  - `nama`, `umur`, `jenis_kelamin`: Data demografis
  - `diagnosa`: Diagnosa medis
  - `gejala`: Array gejala
  - `obat_yang_diminum`: Array obat dengan dosis
  - `hasil_lab`: Object hasil laboratorium
- **Use Cases**: Sistem manajemen pasien, analisis epidemiologi, prediksi diagnosa

### Medical Physical Examination Datasets

#### Brain Diseases Dataset
**`brain_diseases.json`** - Penyakit Neurologis dengan Ciri Fisik
- **Format**: JSON Array
- **Jumlah Records**: 6 penyakit neurologis
- **Kategori**: Stroke, Parkinson, Alzheimer, Epilepsi, Migrain, Meningitis
- **Fields**:
  - `ciri_fisik_wajah`: Array ciri fisik pada wajah
  - `ciri_fisik_tubuh`: Array manifestasi fisik pada tubuh
  - `pemeriksaan_fisik`: Array tes dan pemeriksaan klinis
  - `gejala_neurologis`: Array gejala neurologis spesifik
- **Use Cases**: Sistem diagnosa neurologis, training AI medical, clinical decision support

#### Eye Diseases Detailed Dataset  
**`eye_diseases_detailed.json`** - Penyakit Mata dengan Pemeriksaan Detail
- **Format**: JSON Array
- **Jumlah Records**: 7 penyakit mata
- **Kategori**: Katarak kongenital, Glaukoma akut, Ablasi retina, Keratitis, dll
- **Fields**:
  - `ciri_fisik_mata`: Array tanda fisik pada mata
  - `ciri_fisik_wajah`: Array manifestasi pada wajah
  - `pemeriksaan_fisik`: Array pemeriksaan oftalmologi
  - `komplikasi_fisik`: Array komplikasi yang dapat terjadi
- **Use Cases**: Aplikasi telemedicine mata, screening otomatis, medical imaging AI

#### Tongue Oral Diseases Dataset
**`tongue_oral_diseases.json`** - Penyakit Mulut dan Lidah
- **Format**: JSON Array  
- **Jumlah Records**: 7 penyakit oral
- **Kategori**: Oral thrush, Geographic tongue, Leukoplakia, Sariawan, dll
- **Fields**:
  - `ciri_fisik_lidah`: Array ciri fisik spesifik pada lidah
  - `ciri_fisik_mulut`: Array manifestasi pada rongga mulut
  - `pemeriksaan_fisik`: Array tes dan pemeriksaan oral
  - `gejala_klinis`: Array gejala yang dirasakan pasien
- **Use Cases**: Aplikasi dental health, oral cancer screening, dental education

#### Skin Diseases Dataset
**`skin_diseases.json`** - Penyakit Kulit dengan Manifestasi Fisik
- **Format**: JSON Array
- **Jumlah Records**: 7 penyakit kulit
- **Kategori**: Psoriasis, Eczema, Melanoma, Impetigo, Vitiligo, dll  
- **Fields**:
  - `ciri_fisik_kulit`: Array karakteristik visual kulit
  - `lokasi_predileksi`: Array area tubuh yang sering terkena
  - `pemeriksaan_fisik`: Array tes dermatologi
  - `komplikasi_potensial`: Array komplikasi yang mungkin terjadi
- **Use Cases**: Dermatology AI, skin cancer detection, telemedicine kulit

#### General Physical Examination Dataset
**`general_physical_examination.json`** - Penyakit Umum dengan Temuan Fisik
- **Format**: JSON Array
- **Jumlah Records**: 7 penyakit sistemik
- **Kategori**: Pneumonia, Gagal jantung, Sirosis, Hipertiroid, Diabetes, dll
- **Fields**:
  - `ciri_fisik_umum`: Array tanda fisik umum
  - `pemeriksaan_sistemik`: Array temuan pemeriksaan organ
  - `tanda_vital`: Array parameter vital sign
  - `komplikasi_fisik`: Array komplikasi yang dapat terjadi
- **Use Cases**: Clinical decision support, medical education, diagnostic AI

### IT Datasets

#### `it_inventory.csv` - Inventaris IT
- **Format**: CSV
- **Jumlah Records**: 20 aset IT
- **Columns**: 
  - `asset_id`: ID unik aset
  - `asset_type`: Jenis aset (Laptop, Desktop, Server, dll)
  - `brand`, `model`: Merek dan model
  - `status`: Status aset (Active, Inactive)
  - `assigned_to`: Pengguna yang menggunakan
  - `cost`: Harga pembelian
- **Use Cases**: Sistem manajemen aset, analisis biaya IT, laporan inventaris

#### `software_licenses.json` - Lisensi Software
- **Format**: JSON Array
- **Jumlah Records**: 5 lisensi software
- **Fields**:
  - `license_id`: ID lisensi
  - `software_name`: Nama software
  - `license_type`: Tipe lisensi (Subscription, Perpetual)
  - `total_licenses`, `used_licenses`: Jumlah lisensi
  - `cost_per_license`: Biaya per lisensi
  - `compliance_status`: Status kepatuhan
- **Use Cases**: Manajemen lisensi software, analisis biaya, compliance tracking

### HR Datasets

#### `employee_reviews.txt` - Review Karyawan
- **Format**: Plain Text (Unstructured)
- **Content**: 5 review performa karyawan
- **Structure**:
  - Header informasi karyawan
  - Summary performa
  - Strengths dan areas for improvement
  - Goals untuk quarter berikutnya
  - Rating dan rekomendasi
- **Use Cases**: Analisis sentimen, NLP, sistem HR, performance analytics

#### `hr_attendance_log.txt` - Log Kehadiran
- **Format**: Plain Text (Semi-structured)
- **Content**: Data kehadiran 5 karyawan selama Januari 2024
- **Information**:
  - Jam kerja regular dan overtime
  - Keterlambatan dan pulang cepat
  - Cuti yang diambil
  - Summary departemen
- **Use Cases**: Analisis kehadiran, workforce analytics, payroll processing

## 🎯 Use Cases & Applications

### Data Science & Analytics
- **Exploratory Data Analysis (EDA)**: Analisis dataset untuk menemukan pattern
- **Machine Learning**: Training model untuk klasifikasi, prediksi, clustering
- **Statistical Analysis**: Analisis statistik deskriptif dan inferensial

### Application Development  
- **Database Seeding**: Mengisi database dengan data contoh
- **API Testing**: Data untuk testing endpoint API
- **UI/UX Mockup**: Data realistis untuk design mockup

### Educational Purposes
- **Learning SQL**: Practice query dengan data realistis
- **Data Processing**: Belajar manipulasi data dengan Python/R
- **Visualization**: Membuat chart dan dashboard

### Business Intelligence
- **Dashboard Creation**: Sumber data untuk BI dashboard
- **Report Generation**: Template laporan dengan data nyata
- **KPI Monitoring**: Contoh metrik untuk monitoring performa

## 🛠️ Tools & Technologies

### Programming Languages
- **Python**: pandas, json, matplotlib, seaborn
- **R**: readr, dplyr, ggplot2, jsonlite  
- **JavaScript**: D3.js, Chart.js untuk visualisasi
- **SQL**: Query data setelah import ke database

### Databases
- **MySQL/PostgreSQL**: Import CSV dan JSON data
- **MongoDB**: Store JSON documents
- **SQLite**: Lightweight database untuk prototyping

### Visualization Tools
- **Tableau**: Connect dan visualisasi data
- **Power BI**: Business intelligence dashboard
- **Google Data Studio**: Free dashboard tool
- **Excel**: Basic analysis dan charting

## 📝 Data Quality & Considerations

### Data Characteristics
- **Realistic**: Data dibuat menyerupai kondisi real-world
- **Complete**: Minimal missing values untuk kemudahan pembelajaran
- **Diverse**: Variasi data untuk berbagai skenario testing
- **Localized**: Menggunakan nama Indonesia dan konteks lokal

### Limitations
- **Sample Size**: Dataset berukuran kecil untuk tujuan pembelajaran
- **Synthetic**: Data dibuat buatan, bukan real production data
- **Privacy**: Tidak mengandung data personal atau sensitif nyata
- **Simplified**: Struktur data disederhanakan untuk kemudahan

## 🔒 Privacy & Ethics

- ✅ Tidak menggunakan data personal nyata
- ✅ Semua nama dan informasi adalah fiktif  
- ✅ Aman untuk pembelajaran dan development
- ✅ Tidak mengandung informasi sensitif atau rahasia
- ✅ Dapat dibagikan secara public

## 📄 License

Dataset ini tersedia untuk penggunaan edukasi dan development. Silakan digunakan untuk:
- ✅ Pembelajaran dan training
- ✅ Development dan testing aplikasi
- ✅ Research dan analisis data
- ✅ Portfolio projects
- ❌ Tidak untuk produksi komersial tanpa modifikasi

## 🤝 Contributing

Ingin menambah dataset baru? Silakan:
1. Fork repository ini
2. Tambahkan dataset dalam folder yang sesuai
3. Update README.md dengan dokumentasi
4. Submit pull request

Format dataset baru harus:
- Mengandung minimal 5-10 records
- Dokumentasi lengkap di README
- Contoh code untuk membaca data
- Data realistis tapi fiktif

## 📞 Contact & Support

Jika ada pertanyaan atau saran:
- Create GitHub Issue untuk bug report atau feature request
- Gunakan Discussion tab untuk pertanyaan umum
- Email: apipedia22@gmail.com untuk pertanyaan khusus
- GitHub Repository: https://github.com/Cloud-Dark/exampledataset
- Disediakan oleh apipedia.id

---

**Happy Coding & Data Exploring! 🚀📊**