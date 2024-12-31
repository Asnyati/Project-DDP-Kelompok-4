import streamlit as st
import math

def run():
    st.title("Menghitung Volume Kerucut")

    # Input dari pengguna
    st.header("Masukkan nilai")
    jari_jari = st.number_input("Masukkan Jari-jari Alas (cm):", min_value=0.0, step=0.1, format="%.2f")
    tinggi = st.number_input("Masukkan Tinggi Kerucut (cm):", min_value=0.0, step=0.1, format="%.2f")

    # Perhitungan
    if st.button("Hitung Volume"):
        if jari_jari > 0 and tinggi > 0:
            # Menggunakan for loop untuk menampilkan proses perhitungan
            for step in range(1, 2):  # Simulasi 1 langkah perhitungan
                st.write(f"Langkah {step}: Hitung volume menggunakan formula (1/3)πr²t")
            
            # Menggunakan while untuk menghitung volume
            hasil = 0
            counter = 0
            while counter < 1: 
                hasil = (1/3) * math.pi * (jari_jari ** 2) * tinggi
                counter += 1

            st.success(f"Volume kerucut adalah {hasil:.2f} cm³")
        else:
            st.error("Jari-jari dan tinggi harus lebih dari 0!")