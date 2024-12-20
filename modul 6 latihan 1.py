#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:52:49 2024

@author: adesintia
"""

def main():
    grades = {'A': 4.0, 'A-': 3.75, 'B+': 3.5, 'B': 3.0, 'B-': 2.75, 'C': 2.0, 'C-': 1.75, 'E': 1.25}
    total, count = 0, 0

    while True:
        grade = input("Masukkan Nilai :").upper()
        if grade == '':  # Mengakhiri jika input kosong
            break
        grade_value = grades.get(grade)
        if grade_value is not None:
            print(f"Nilai: {grade_value}")
            total += grade_value
            count += 1
        else:
            print(f"Kategori huruf '{grade}' tidak valid dan akan diabaikan.")

    if count:
        print(f"Rata-ratanya adalah: {total / count:.2f}")
    else:
        print("Tidak ada nilai yang valid dimasukkan.")

main()