import streamlit as st

def run():
# Judul aplikasi
         st.title("Kalkulator Luas Persegi Panjang")

# Fungsi untuk menghitung luas persegi panjang
def hitung_luas_panjang(lebar, panjang):
     return lebar * panjang


# Input dari pengguna
panjang = st.number_input("Masukkan panjang (cm):", min_value=0)
lebar = st.number_input("Masukkan lebar (cm):", min_value=0)

# Tombol untuk menghitung luas
if st.button("Hitung Luas"):
     if panjang <= 0 or lebar <= 0:
         st.error("Panjang dan lebar harus lebih besar dari 0.")
     else:
         luas = hitung_luas_panjang(lebar, panjang)
         st.success(f"Luas persegi panjang adalah: {luas} cm²")
