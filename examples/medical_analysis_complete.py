#!/usr/bin/env python3
"""
Complete Medical Analysis Examples
Contoh analisis lengkap untuk semua dataset medis dengan fokus pada ciri fisik
"""

import json
from collections import Counter, defaultdict
import re

def analyze_brain_diseases():
    """Analisis dataset penyakit otak/neurologis"""
    print("=== ANALISIS PENYAKIT NEUROLOGIS ===")
    
    with open('../healthcare/brain_diseases.json', 'r', encoding='utf-8') as f:
        diseases = json.load(f)
    
    print(f"Total penyakit neurologis: {len(diseases)}")
    
    # Analisis kategori penyakit
    categories = Counter([d['kategori'] for d in diseases])
    print("\nKategori penyakit neurologis:")
    for cat, count in categories.items():
        print(f"- {cat}: {count} penyakit")
    
    # Ciri fisik wajah yang paling umum
    facial_signs = []
    for disease in diseases:
        facial_signs.extend(disease['ciri_fisik_wajah'])
    
    common_facial = Counter(facial_signs).most_common(5)
    print("\nCiri fisik wajah yang paling umum:")
    for sign, count in common_facial:
        print(f"- {sign}: {count} penyakit")
    
    # Penyakit dengan ciri fisik tubuh terbanyak
    body_signs_count = {d['nama_penyakit']: len(d['ciri_fisik_tubuh']) for d in diseases}
    max_disease = max(body_signs_count, key=body_signs_count.get)
    print(f"\nPenyakit dengan ciri fisik tubuh terbanyak: {max_disease} ({body_signs_count[max_disease]} ciri)")

def analyze_eye_diseases():
    """Analisis dataset penyakit mata detail"""
    print("\n=== ANALISIS PENYAKIT MATA DETAIL ===")
    
    with open('../healthcare/eye_diseases_detailed.json', 'r', encoding='utf-8') as f:
        diseases = json.load(f)
    
    print(f"Total penyakit mata: {len(diseases)}")
    
    # Kategori penyakit mata
    categories = Counter([d['kategori'] for d in diseases])
    print("\nKategori penyakit mata:")
    for cat, count in categories.items():
        print(f"- {cat}: {count} penyakit")
    
    # Ciri fisik mata yang mengancam penglihatan
    emergency_signs = []
    for disease in diseases:
        if any(word in disease['deskripsi_singkat'].lower() 
               for word in ['akut', 'mendadak', 'emergensi', 'kebutaan']):
            emergency_signs.append(disease['nama_penyakit'])
    
    print(f"\nPenyakit mata yang memerlukan penanganan darurat: {len(emergency_signs)}")
    for disease in emergency_signs:
        print(f"- {disease}")

def analyze_oral_diseases():
    """Analisis dataset penyakit mulut dan lidah"""
    print("\n=== ANALISIS PENYAKIT MULUT DAN LIDAH ===")
    
    with open('../healthcare/tongue_oral_diseases.json', 'r', encoding='utf-8') as f:
        diseases = json.load(f)
    
    print(f"Total penyakit oral: {len(diseases)}")
    
    # Ciri fisik lidah yang spesifik
    tongue_signs = []
    for disease in diseases:
        tongue_signs.extend(disease['ciri_fisik_lidah'])
    
    # Analisis perubahan warna lidah
    color_changes = []
    for sign in tongue_signs:
        if any(color in sign.lower() for color in ['putih', 'merah', 'hitam', 'kuning', 'coklat']):
            color_changes.append(sign)
    
    print(f"\nPerubahan warna pada lidah: {len(color_changes)} manifestasi")
    color_counter = Counter(color_changes).most_common(3)
    for change, count in color_counter:
        print(f"- {change}")
    
    # Penyakit dengan risiko keganasan
    malignant_risk = []
    for disease in diseases:
        if any(word in disease['deskripsi_singkat'].lower() 
               for word in ['prakanker', 'kanker', 'ganas', 'keganasan']):
            malignant_risk.append(disease['nama_penyakit'])
    
    if malignant_risk:
        print(f"\nPenyakit dengan risiko keganasan:")
        for disease in malignant_risk:
            print(f"- {disease}")

def analyze_skin_diseases():
    """Analisis dataset penyakit kulit"""
    print("\n=== ANALISIS PENYAKIT KULIT ===")
    
    with open('../healthcare/skin_diseases.json', 'r', encoding='utf-8') as f:
        diseases = json.load(f)
    
    print(f"Total penyakit kulit: {len(diseases)}")
    
    # Lokasi predileksi paling umum
    all_locations = []
    for disease in diseases:
        if 'lokasi_predileksi' in disease:
            all_locations.extend(disease['lokasi_predileksi'])
    
    common_locations = Counter(all_locations).most_common(5)
    print("\nLokasi predileksi paling umum:")
    for location, count in common_locations:
        print(f"- {location}: {count} penyakit")
    
    # Penyakit kulit menular vs non-menular
    infectious = []
    non_infectious = []
    
    for disease in diseases:
        if any(word in disease['kategori'].lower() or word in disease['deskripsi_singkat'].lower()
               for word in ['infeksi', 'bakteri', 'virus', 'jamur', 'menular']):
            infectious.append(disease['nama_penyakit'])
        else:
            non_infectious.append(disease['nama_penyakit'])
    
    print(f"\nPenyakit kulit menular: {len(infectious)}")
    for disease in infectious:
        print(f"- {disease}")
    
    print(f"\nPenyakit kulit non-menular: {len(non_infectious)}")
    for disease in non_infectious:
        print(f"- {disease}")

def analyze_general_diseases():
    """Analisis dataset penyakit umum"""
    print("\n=== ANALISIS PENYAKIT UMUM ===")
    
    with open('../healthcare/general_physical_examination.json', 'r', encoding='utf-8') as f:
        diseases = json.load(f)
    
    print(f"Total penyakit sistemik: {len(diseases)}")
    
    # Sistem organ yang terlibat
    organ_systems = Counter([d['kategori'] for d in diseases])
    print("\nSistem organ yang terlibat:")
    for system, count in organ_systems.items():
        print(f"- {system}: {count} penyakit")
    
    # Penyakit dengan komplikasi terbanyak
    complications = {}
    for disease in diseases:
        if 'komplikasi_fisik' in disease:
            complications[disease['nama_penyakit']] = len(disease['komplikasi_fisik'])
        elif 'komplikasi_serius' in disease:
            complications[disease['nama_penyakit']] = len(disease['komplikasi_serius'])
    
    if complications:
        max_complications = max(complications, key=complications.get)
        print(f"\nPenyakit dengan komplikasi terbanyak: {max_complications} ({complications[max_complications]} komplikasi)")

def generate_diagnostic_patterns():
    """Generate pola diagnostik berdasarkan ciri fisik"""
    print("\n=== POLA DIAGNOSTIK BERDASARKAN CIRI FISIK ===")
    
    # Load semua dataset
    datasets = {
        'brain': '../healthcare/brain_diseases.json',
        'eye': '../healthcare/eye_diseases_detailed.json', 
        'oral': '../healthcare/tongue_oral_diseases.json',
        'skin': '../healthcare/skin_diseases.json',
        'general': '../healthcare/general_physical_examination.json'
    }
    
    # Kumpulkan semua ciri fisik
    physical_signs = defaultdict(list)
    
    for category, file_path in datasets.items():
        with open(file_path, 'r', encoding='utf-8') as f:
            diseases = json.load(f)
            
        for disease in diseases:
            disease_name = disease['nama_penyakit']
            
            # Kumpulkan ciri fisik dari berbagai field
            for field in disease:
                if 'ciri_fisik' in field or 'physical' in field:
                    if isinstance(disease[field], list):
                        for sign in disease[field]:
                            physical_signs[sign].append(f"{category}:{disease_name}")
    
    # Ciri fisik yang muncul di multiple penyakit
    common_signs = {sign: diseases for sign, diseases in physical_signs.items() 
                   if len(diseases) > 1}
    
    print(f"Ciri fisik yang muncul pada multiple penyakit: {len(common_signs)}")
    
    # Tampilkan beberapa contoh
    for sign, diseases in list(common_signs.items())[:5]:
        print(f"\n'{sign}' muncul pada:")
        for disease in diseases[:3]:  # Tampilkan max 3
            category, name = disease.split(':', 1)
            print(f"  - [{category}] {name}")

def create_differential_diagnosis_helper():
    """Buat helper untuk diagnosis banding berdasarkan ciri fisik"""
    print("\n=== DIFFERENTIAL DIAGNOSIS HELPER ===")
    
    # Contoh: mata merah
    red_eye_diseases = []
    
    # Cek penyakit mata
    with open('../healthcare/eye_diseases_detailed.json', 'r', encoding='utf-8') as f:
        eye_diseases = json.load(f)
    
    for disease in eye_diseases:
        for sign in disease.get('ciri_fisik_mata', []):
            if 'merah' in sign.lower():
                red_eye_diseases.append({
                    'penyakit': disease['nama_penyakit'],
                    'kategori': disease['kategori'], 
                    'ciri': sign
                })
    
    if red_eye_diseases:
        print("Differential diagnosis untuk 'mata merah':")
        for item in red_eye_diseases:
            print(f"- {item['penyakit']} ({item['kategori']}): {item['ciri']}")

def medical_ai_training_data():
    """Generate summary untuk training AI medis"""
    print("\n=== SUMMARY UNTUK TRAINING AI MEDIS ===")
    
    total_diseases = 0
    total_physical_signs = 0
    categories = set()
    
    datasets = [
        '../healthcare/brain_diseases.json',
        '../healthcare/eye_diseases_detailed.json',
        '../healthcare/tongue_oral_diseases.json', 
        '../healthcare/skin_diseases.json',
        '../healthcare/general_physical_examination.json'
    ]
    
    for dataset in datasets:
        with open(dataset, 'r', encoding='utf-8') as f:
            diseases = json.load(f)
            total_diseases += len(diseases)
            
        for disease in diseases:
            categories.add(disease['kategori'])
            
            # Hitung total ciri fisik
            for field, value in disease.items():
                if 'ciri' in field and isinstance(value, list):
                    total_physical_signs += len(value)
    
    print(f"Total dataset untuk AI training:")
    print(f"- Jumlah penyakit: {total_diseases}")
    print(f"- Jumlah ciri fisik: {total_physical_signs}")
    print(f"- Jumlah kategori: {len(categories)}")
    print(f"- Kategori: {', '.join(sorted(categories))}")
    
    print(f"\nRata-rata ciri fisik per penyakit: {total_physical_signs/total_diseases:.1f}")

if __name__ == "__main__":
    # Jalankan semua analisis
    analyze_brain_diseases()
    analyze_eye_diseases() 
    analyze_oral_diseases()
    analyze_skin_diseases()
    analyze_general_diseases()
    generate_diagnostic_patterns()
    create_differential_diagnosis_helper()
    medical_ai_training_data()
    
    print("\n=== ANALISIS MEDIS SELESAI ===")
    print("\nDataset ini cocok untuk:")
    print("- Training AI diagnostic tools")
    print("- Medical decision support systems") 
    print("- Clinical education applications")
    print("- Telemedicine platforms")
    print("- Medical imaging analysis")
    print("- Symptom checker applications")