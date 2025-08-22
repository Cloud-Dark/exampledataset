#!/usr/bin/env python3
"""
Healthcare Dataset Analysis Examples
Contoh analisis data untuk dataset kesehatan
"""

import json
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def analyze_eye_diseases():
    """Analisis dataset penyakit mata"""
    print("=== ANALISIS PENYAKIT MATA ===")
    
    # Load data penyakit mata
    with open('../healthcare/eyessick.json', 'r', encoding='utf-8') as f:
        diseases = json.load(f)
    
    print(f"Total penyakit: {len(diseases)}")
    
    # Analisis jumlah gejala per penyakit
    symptoms_count = {d['nama_penyakit']: len(d['gejala_pasien']) for d in diseases}
    print("\nJumlah gejala per penyakit:")
    for disease, count in symptoms_count.items():
        print(f"- {disease}: {count} gejala")
    
    # Gejala yang paling sering muncul
    all_symptoms = []
    for disease in diseases:
        all_symptoms.extend(disease['gejala_pasien'])
    
    common_symptoms = Counter(all_symptoms).most_common(5)
    print("\nGejala yang paling umum:")
    for symptom, count in common_symptoms:
        print(f"- {symptom}: {count} penyakit")
    
    return diseases

def analyze_patients():
    """Analisis data pasien"""
    print("\n=== ANALISIS DATA PASIEN ===")
    
    # Load data pasien
    with open('../healthcare/healthcare_patients.json', 'r', encoding='utf-8') as f:
        patients = json.load(f)
    
    # Konversi ke DataFrame untuk analisis
    df = pd.DataFrame(patients)
    
    print(f"Total pasien: {len(patients)}")
    
    # Distribusi umur
    print(f"\nUmur rata-rata: {df['umur'].mean():.1f} tahun")
    print(f"Umur termuda: {df['umur'].min()} tahun")
    print(f"Umur tertua: {df['umur'].max()} tahun")
    
    # Distribusi jenis kelamin
    gender_dist = df['jenis_kelamin'].value_counts()
    print("\nDistribusi jenis kelamin:")
    for gender, count in gender_dist.items():
        print(f"- {'Perempuan' if gender == 'F' else 'Laki-laki'}: {count} pasien")
    
    # Diagnosa yang paling umum
    diagnosis_count = Counter(df['diagnosa'])
    print("\nDiagnosa yang paling umum:")
    for diagnosis, count in diagnosis_count.items():
        print(f"- {diagnosis}: {count} kasus")
    
    return patients

def medication_analysis():
    """Analisis obat yang dikonsumsi pasien"""
    print("\n=== ANALISIS OBAT PASIEN ===")
    
    with open('../healthcare/healthcare_patients.json', 'r', encoding='utf-8') as f:
        patients = json.load(f)
    
    # Kumpulkan semua obat
    all_medications = []
    for patient in patients:
        for med in patient['obat_yang_diminum']:
            all_medications.append(med['nama_obat'])
    
    # Obat yang paling sering diresepkan
    med_counter = Counter(all_medications)
    print("Obat yang paling sering diresepkan:")
    for med, count in med_counter.most_common():
        print(f"- {med}: {count} pasien")

def create_visualization():
    """Membuat visualisasi data kesehatan"""
    print("\n=== MEMBUAT VISUALISASI ===")
    
    # Data untuk visualisasi
    with open('../healthcare/healthcare_patients.json', 'r', encoding='utf-8') as f:
        patients = json.load(f)
    
    df = pd.DataFrame(patients)
    
    # Buat plot distribusi umur
    plt.figure(figsize=(10, 6))
    
    plt.subplot(1, 2, 1)
    plt.hist(df['umur'], bins=5, edgecolor='black', alpha=0.7)
    plt.title('Distribusi Umur Pasien')
    plt.xlabel('Umur')
    plt.ylabel('Jumlah Pasien')
    
    plt.subplot(1, 2, 2)
    gender_counts = df['jenis_kelamin'].value_counts()
    labels = ['Laki-laki' if x == 'M' else 'Perempuan' for x in gender_counts.index]
    plt.pie(gender_counts.values, labels=labels, autopct='%1.1f%%')
    plt.title('Distribusi Jenis Kelamin')
    
    plt.tight_layout()
    plt.savefig('healthcare_analysis.png', dpi=300, bbox_inches='tight')
    print("Visualisasi disimpan sebagai 'healthcare_analysis.png'")

if __name__ == "__main__":
    # Jalankan semua analisis
    analyze_eye_diseases()
    analyze_patients()
    medication_analysis()
    
    # Uncomment untuk membuat visualisasi (requires matplotlib)
    # create_visualization()
    
    print("\n=== ANALISIS SELESAI ===")