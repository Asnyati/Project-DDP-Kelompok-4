import streamlit as st
import pandas as pd

# judul
st.title("Dashboard Perhitungan")

# Sidebar menu
menu = st.sidebar("Menu Utama", ["Persegi", "Persegi Panjang", "Tabung", "Kerucut"])

# Class Perhitungan
class perhitungan:
    def __init__(self):
        self.luas_persegi = 0
        self.luas_persegi_panjang = 0
        self.volume_tabung = 0
        self.volume_kerucut = 0

    def hitung_persegi(self, sisi):
        self.luas_persegi = sisi ** 2
        return self.luas_persegi
    
    def hitung_persegi_panjang(self, panjang, lebar):
        self.luas_persegi_panjang = panjang * lebar
        return self.luas_persegi_panjang
    
    def hitung_tabung(self, jari_jari, tinggi):
        self.volume_tabung = 3.14 * (jari_jari ** 2) * tinggi
        return self.volume_tabung
    
    def hitung_kerucut(self, jari_jari, tinggi):
        self.volume_kerucut = (1 / 3) * 3.14 * (jari_jari** 2) * tinggi
        return self.volume_kerucut
    
# Objek Perhitungan
perhitungan = perhitungan()

# Variabel menyimpan hasil perhitungan
luas_persegi = 0
luas_persegi_panjang = 0
volume_tabung = 0
volume_kerucut = 0

if menu == "Dasboard":
    st.header("Dashboard Perhitungan")
elif menu == "Persegi":
    st.header("perhitungan Persegi")
    sisi = st.number_input("Masukkan panjang sisi:", min_value=0.0)
    luas_persegi = perhitungan.hitung_persegi(sisi)
    st.write(f"Luas Persegi: {luas_persegi}")
elif menu == "Persegi Panjang":
    st.header("Perhitungan Persegi Panjang")
    panjang = st.number_input("Masukkan panjang:", min_value=0.0)
    lebar = st.number_input("Masukkan lebar:", min_value=0.0)
    luas_persegi_panjang = perhitungan.hitung_persegi_panjang(panjang, lebar)
    st.write(f"Luas Persegi Panjang: {luas_persegi_panjang}")
elif menu == "Tabung":
    st.header("Perhitungan Tabung")
    jari_jari = st.number_input("Masukkan jari-jari tabung:", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi tabung:", min_value=0.0)
    volume_tabung = perhitungan.hitung_tabung(jari_jari, tinggi)
    st.write(f"Volume Tabung: {volume_tabung}")
elif menu == "Kerucut":
    st.header("Perhitungan Kerucut")
    jari_jari = st.number_input("Masukkan jari-jari kerucut:", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi kerucut:", min_value=0.0)
    volume_kerucut = perhitungan.hitung_kerucut(jari_jari, tinggi)
    st.write(f"Volume Kerucut: {volume_kerucut}")

# Hasil
st.subheader("Hasil dari Perhitungan:")
data = {
    "Bentuk": ["Persegi", "Persegi Panjang", "Tabung", "Kerucut"],
    "Hasil": [
        luas_persegi if menu == "Persegi" else 0,
        luas_persegi_panjang if menu == "Persegi Panjang" else 0,
        volume_tabung if menu == "Tabung" else 0,
        volume_kerucut if menu == "Kerucut" else 0
    ]
}
df = pd.DataFrame(data)
st.table(df)