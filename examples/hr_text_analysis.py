#!/usr/bin/env python3
"""
HR Text Analysis Examples
Contoh analisis teks untuk data HR (review karyawan dan log kehadiran)
"""

import re
from collections import Counter, defaultdict
from datetime import datetime

def parse_employee_reviews():
    """Parse dan analisis review karyawan"""
    print("=== ANALISIS REVIEW KARYAWAN ===")
    
    # Baca file review
    with open('../hr/employee_reviews.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split berdasarkan separator
    sections = content.split('=' * 80)
    
    employees = []
    for section in sections:
        if 'EMPLOYEE ID:' in section:
            employee = parse_single_review(section)
            if employee:
                employees.append(employee)
    
    print(f"Total review yang dianalisis: {len(employees)}")
    
    # Analisis departemen
    departments = Counter([emp['department'] for emp in employees])
    print("\nDistribusi departemen:")
    for dept, count in departments.items():
        print(f"- {dept}: {count} karyawan")
    
    # Analisis rating
    ratings = [emp['rating'] for emp in employees if emp['rating']]
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        print(f"\nRating rata-rata: {avg_rating:.2f}/5.0")
        print(f"Rating tertinggi: {max(ratings)}")
        print(f"Rating terendah: {min(ratings)}")
    
    # Analisis rekomendasi
    recommendations = Counter([emp['recommendation'] for emp in employees if emp['recommendation']])
    print("\nRekomendasi:")
    for rec, count in recommendations.items():
        print(f"- {rec}: {count} karyawan")
    
    return employees

def parse_single_review(section):
    """Parse review individual"""
    lines = section.strip().split('\n')
    employee = {
        'id': None,
        'name': None,
        'position': None,
        'department': None,
        'rating': None,
        'recommendation': None,
        'strengths': [],
        'improvements': [],
        'goals': []
    }
    
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('EMPLOYEE ID:'):
            employee['id'] = line.split(':')[1].strip()
        elif line.startswith('NAME:'):
            employee['name'] = line.split(':')[1].strip()
        elif line.startswith('POSITION:'):
            employee['position'] = line.split(':')[1].strip()
        elif line.startswith('DEPARTMENT:'):
            employee['department'] = line.split(':')[1].strip()
        elif line.startswith('OVERALL RATING:'):
            rating_text = line.split(':')[1].strip()
            rating_match = re.search(r'(\d+\.\d+)', rating_text)
            if rating_match:
                employee['rating'] = float(rating_match.group(1))
        elif line.startswith('RECOMMENDATION:'):
            employee['recommendation'] = line.split(':')[1].strip()
        elif 'STRENGTHS:' in line:
            current_section = 'strengths'
        elif 'AREAS FOR IMPROVEMENT:' in line:
            current_section = 'improvements'
        elif 'GOALS FOR NEXT QUARTER:' in line:
            current_section = 'goals'
        elif line.startswith('-') and current_section:
            item = line[1:].strip()
            if current_section == 'strengths':
                employee['strengths'].append(item)
            elif current_section == 'improvements':
                employee['improvements'].append(item)
            elif current_section == 'goals':
                employee['goals'].append(item)
    
    return employee if employee['id'] else None

def analyze_performance_themes():
    """Analisis tema dalam performa karyawan"""
    print("\n=== ANALISIS TEMA PERFORMA ===")
    
    employees = parse_employee_reviews()
    
    # Kumpulkan semua strengths dan improvements
    all_strengths = []
    all_improvements = []
    
    for emp in employees:
        all_strengths.extend(emp['strengths'])
        all_improvements.extend(emp['improvements'])
    
    # Analisis kata kunci dalam strengths
    strength_keywords = extract_keywords(all_strengths)
    print("Kata kunci dalam strengths (top 10):")
    for keyword, count in strength_keywords.most_common(10):
        print(f"- {keyword}: {count} kali")
    
    # Analisis kata kunci dalam areas for improvement
    improvement_keywords = extract_keywords(all_improvements)
    print("\nKata kunci dalam areas for improvement (top 10):")
    for keyword, count in improvement_keywords.most_common(10):
        print(f"- {keyword}: {count} kali")

def extract_keywords(text_list):
    """Extract keywords dari daftar teks"""
    # Kata-kata yang diabaikan
    stop_words = {'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 
                  'by', 'from', 'about', 'into', 'through', 'during', 'before', 
                  'after', 'above', 'below', 'up', 'down', 'out', 'off', 'over',
                  'under', 'again', 'further', 'then', 'once', 'the', 'a', 'an',
                  'yang', 'dalam', 'untuk', 'dengan', 'pada', 'ke', 'dari', 'di',
                  'dan', 'atau', 'tapi', 'tetapi', 'serta', 'lebih', 'sangat'}
    
    all_words = []
    for text in text_list:
        # Bersihkan teks dan split kata
        clean_text = re.sub(r'[^\w\s]', ' ', text.lower())
        words = clean_text.split()
        
        # Filter kata-kata bermakna
        meaningful_words = [word for word in words 
                          if len(word) > 3 and word not in stop_words]
        all_words.extend(meaningful_words)
    
    return Counter(all_words)

def parse_attendance_log():
    """Parse log kehadiran"""
    print("\n=== ANALISIS LOG KEHADIRAN ===")
    
    with open('../hr/hr_attendance_log.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split berdasarkan separator
    sections = content.split('=' * 40)
    
    employees = []
    for section in sections:
        if 'EMPLOYEE:' in section and 'Department:' in section:
            employee = parse_attendance_section(section)
            if employee:
                employees.append(employee)
    
    print(f"Total karyawan dalam log: {len(employees)}")
    
    # Analisis kehadiran
    total_hours = sum(emp['total_hours'] for emp in employees)
    total_overtime = sum(emp['overtime_hours'] for emp in employees)
    
    print(f"\nTotal jam kerja: {total_hours} jam")
    print(f"Total overtime: {total_overtime} jam")
    print(f"Rata-rata jam kerja per karyawan: {total_hours/len(employees):.1f} jam")
    print(f"Rata-rata overtime per karyawan: {total_overtime/len(employees):.1f} jam")
    
    # Karyawan dengan overtime tertinggi
    high_overtime = sorted(employees, key=lambda x: x['overtime_hours'], reverse=True)
    print(f"\nKaryawan dengan overtime tertinggi:")
    for emp in high_overtime[:3]:
        print(f"- {emp['name']} ({emp['department']}): {emp['overtime_hours']} jam")
    
    # Analisis keterlambatan
    late_employees = [emp for emp in employees if emp['late_arrivals'] > 0]
    if late_employees:
        print(f"\nKaryawan dengan keterlambatan: {len(late_employees)}")
        for emp in late_employees:
            print(f"- {emp['name']}: {emp['late_arrivals']} kali")
    
    return employees

def parse_attendance_section(section):
    """Parse section kehadiran individual"""
    lines = section.strip().split('\n')
    employee = {
        'name': None,
        'department': None,
        'total_hours': 0,
        'overtime_hours': 0,
        'days_present': 0,
        'days_absent': 0,
        'late_arrivals': 0,
        'early_departures': 0
    }
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('EMPLOYEE:'):
            # Extract name (before parentheses)
            match = re.search(r'EMPLOYEE:\s*([^(]+)', line)
            if match:
                employee['name'] = match.group(1).strip()
        elif line.startswith('Department:'):
            employee['department'] = line.split(':')[1].strip()
        elif line.startswith('Total Hours Worked:'):
            match = re.search(r'(\d+)', line)
            if match:
                employee['total_hours'] = int(match.group(1))
        elif line.startswith('Overtime Hours:'):
            match = re.search(r'(\d+)', line)
            if match:
                employee['overtime_hours'] = int(match.group(1))
        elif line.startswith('Days Present:'):
            match = re.search(r'(\d+)', line)
            if match:
                employee['days_present'] = int(match.group(1))
        elif line.startswith('Days Absent:'):
            match = re.search(r'(\d+)', line)
            if match:
                employee['days_absent'] = int(match.group(1))
        elif line.startswith('Late Arrivals:'):
            match = re.search(r'(\d+)', line)
            if match:
                employee['late_arrivals'] = int(match.group(1))
        elif line.startswith('Early Departures:'):
            match = re.search(r'(\d+)', line)
            if match:
                employee['early_departures'] = int(match.group(1))
    
    return employee if employee['name'] else None

def generate_hr_insights():
    """Generate insights dari data HR"""
    print("\n=== HR INSIGHTS ===")
    
    # Data dari reviews
    employees_review = parse_employee_reviews()
    employees_attendance = parse_attendance_log()
    
    # Korelasi departemen dan rating
    dept_ratings = defaultdict(list)
    for emp in employees_review:
        if emp['rating'] and emp['department']:
            dept_ratings[emp['department']].append(emp['rating'])
    
    print("Rating rata-rata per departemen:")
    for dept, ratings in dept_ratings.items():
        avg_rating = sum(ratings) / len(ratings)
        print(f"- {dept}: {avg_rating:.2f}/5.0")
    
    # Identifikasi karyawan high-performer
    high_performers = [emp for emp in employees_review if emp['rating'] and emp['rating'] >= 4.0]
    print(f"\nHigh performers (rating ≥4.0): {len(high_performers)} karyawan")
    for emp in high_performers:
        print(f"- {emp['name']} ({emp['department']}): {emp['rating']}/5.0")
    
    # Identifikasi area improvement yang sering muncul
    improvement_keywords = []
    for emp in employees_review:
        improvement_keywords.extend(emp['improvements'])
    
    common_improvements = extract_keywords(improvement_keywords).most_common(5)
    print("\nArea improvement yang paling sering:")
    for improvement, count in common_improvements:
        print(f"- {improvement}: {count} karyawan")

if __name__ == "__main__":
    # Jalankan semua analisis
    parse_employee_reviews()
    analyze_performance_themes()
    parse_attendance_log()
    generate_hr_insights()
    
    print("\n=== ANALISIS SELESAI ===")