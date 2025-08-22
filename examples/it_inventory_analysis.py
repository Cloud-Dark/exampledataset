#!/usr/bin/env python3
"""
IT Inventory Analysis Examples
Contoh analisis data untuk inventaris IT dan lisensi software
"""

import pandas as pd
import json
from collections import Counter
from datetime import datetime

def analyze_it_inventory():
    """Analisis inventaris IT"""
    print("=== ANALISIS INVENTARIS IT ===")
    
    # Load data inventaris
    df = pd.read_csv('../it/it_inventory.csv')
    
    print(f"Total aset IT: {len(df)}")
    
    # Distribusi jenis aset
    asset_types = df['asset_type'].value_counts()
    print("\nDistribusi jenis aset:")
    for asset_type, count in asset_types.items():
        print(f"- {asset_type}: {count} unit")
    
    # Brand yang paling populer
    brands = df['brand'].value_counts().head(5)
    print("\nBrand yang paling banyak digunakan:")
    for brand, count in brands.items():
        print(f"- {brand}: {count} unit")
    
    # Status aset
    status_dist = df['status'].value_counts()
    print("\nStatus aset:")
    for status, count in status_dist.items():
        print(f"- {status}: {count} unit")
    
    # Distribusi per departemen
    dept_dist = df['department'].value_counts()
    print("\nDistribusi per departemen:")
    for dept, count in dept_dist.items():
        print(f"- {dept}: {count} aset")
    
    return df

def analyze_asset_costs():
    """Analisis biaya aset IT"""
    print("\n=== ANALISIS BIAYA ASET ===")
    
    df = pd.read_csv('../it/it_inventory.csv')
    
    # Total nilai aset
    total_value = df['cost'].sum()
    print(f"Total nilai aset: Rp {total_value:,}")
    
    # Rata-rata harga per kategori
    avg_cost = df.groupby('asset_type')['cost'].agg(['mean', 'count', 'sum'])
    print("\nAnalisis biaya per kategori aset:")
    for asset_type, data in avg_cost.iterrows():
        print(f"- {asset_type}:")
        print(f"  Rata-rata: Rp {data['mean']:,.0f}")
        print(f"  Jumlah: {data['count']} unit")
        print(f"  Total nilai: Rp {data['sum']:,}")
    
    # Aset termahal
    expensive_assets = df.nlargest(5, 'cost')[['asset_id', 'asset_type', 'brand', 'model', 'cost']]
    print("\nAset termahal:")
    for _, asset in expensive_assets.iterrows():
        print(f"- {asset['asset_id']}: {asset['brand']} {asset['model']} - Rp {asset['cost']:,}")

def analyze_software_licenses():
    """Analisis lisensi software"""
    print("\n=== ANALISIS LISENSI SOFTWARE ===")
    
    # Load data lisensi
    with open('../it/software_licenses.json', 'r', encoding='utf-8') as f:
        licenses = json.load(f)
    
    # Konversi ke DataFrame
    df = pd.DataFrame(licenses)
    
    print(f"Total software berlisensi: {len(licenses)}")
    
    # Total biaya lisensi tahunan
    total_cost = 0
    for license_info in licenses:
        if 'total_annual_cost' in license_info:
            total_cost += license_info['total_annual_cost']
        elif 'total_cost' in license_info:
            # Untuk lisensi perpetual, hitung amortisasi 5 tahun
            total_cost += license_info['total_cost'] / 5
    
    print(f"Total biaya lisensi tahunan: Rp {total_cost:,}")
    
    # Utilisasi lisensi
    print("\nUtilisasi lisensi:")
    for license_info in licenses:
        utilization = (license_info['used_licenses'] / license_info['total_licenses']) * 100
        print(f"- {license_info['software_name']}: {utilization:.1f}% ({license_info['used_licenses']}/{license_info['total_licenses']})")
    
    # Status compliance
    compliance_status = Counter([l['compliance_status'] for l in licenses])
    print("\nStatus compliance:")
    for status, count in compliance_status.items():
        print(f"- {status}: {count} software")
    
    # Software dengan utilisasi tinggi (>90%)
    high_util = []
    for license_info in licenses:
        utilization = (license_info['used_licenses'] / license_info['total_licenses']) * 100
        if utilization > 90:
            high_util.append({
                'software': license_info['software_name'],
                'utilization': utilization,
                'available': license_info['available_licenses']
            })
    
    if high_util:
        print("\nSoftware dengan utilisasi tinggi (>90%):")
        for software in high_util:
            print(f"- {software['software']}: {software['utilization']:.1f}% (sisa {software['available']} lisensi)")

def warranty_expiry_check():
    """Cek aset yang warranty-nya akan habis"""
    print("\n=== CEK EXPIRY WARRANTY ===")
    
    df = pd.read_csv('../it/it_inventory.csv')
    
    # Konversi tanggal warranty_expiry ke datetime
    df['warranty_expiry'] = pd.to_datetime(df['warranty_expiry'])
    today = pd.Timestamp.now()
    
    # Aset dengan warranty habis dalam 6 bulan
    six_months = today + pd.DateOffset(months=6)
    expiring_soon = df[df['warranty_expiry'] <= six_months]
    
    if not expiring_soon.empty:
        print("Aset dengan warranty habis dalam 6 bulan:")
        for _, asset in expiring_soon.iterrows():
            print(f"- {asset['asset_id']}: {asset['brand']} {asset['model']} - Expired: {asset['warranty_expiry'].strftime('%Y-%m-%d')}")
    else:
        print("Tidak ada aset dengan warranty yang akan habis dalam 6 bulan")

def generate_it_report():
    """Generate laporan IT komprehensif"""
    print("\n=== LAPORAN IT KOMPREHENSIF ===")
    
    # Load data
    inventory_df = pd.read_csv('../it/it_inventory.csv')
    
    with open('../it/software_licenses.json', 'r', encoding='utf-8') as f:
        licenses = json.load(f)
    
    # Summary metrics
    print("SUMMARY METRICS:")
    print(f"- Total Hardware Assets: {len(inventory_df)}")
    print(f"- Total Software Licenses: {len(licenses)}")
    print(f"- Total Hardware Value: Rp {inventory_df['cost'].sum():,}")
    
    total_software_cost = sum(l.get('total_annual_cost', l.get('total_cost', 0)/5) for l in licenses)
    print(f"- Annual Software Cost: Rp {total_software_cost:,}")
    
    # Departemen dengan aset terbanyak
    dept_assets = inventory_df['department'].value_counts()
    print(f"\nDepartemen dengan aset terbanyak: {dept_assets.index[0]} ({dept_assets.iloc[0]} aset)")
    
    # Brand preference
    top_brand = inventory_df['brand'].value_counts()
    print(f"Brand yang paling dipilih: {top_brand.index[0]} ({top_brand.iloc[0]} unit)")
    
    # Compliance issues
    at_risk_licenses = [l for l in licenses if l.get('compliance_status') == 'At Risk']
    if at_risk_licenses:
        print(f"\nPeringatan: {len(at_risk_licenses)} software memiliki compliance risk")
        for license_info in at_risk_licenses:
            print(f"- {license_info['software_name']}: {license_info.get('notes', 'No details')}")

if __name__ == "__main__":
    # Jalankan semua analisis
    analyze_it_inventory()
    analyze_asset_costs()
    analyze_software_licenses()
    warranty_expiry_check()
    generate_it_report()
    
    print("\n=== ANALISIS SELESAI ===")