import streamlit as st

class Tabung:
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_volume(self):
        return 3.14 * (self.jari_jari ** 2) * self.tinggi

def run():
    st.title("Menghitung Volume Tabung")

    # Input pengguna
    st.header("Masukkan Dimensi Tabung")
    jari_jari = st.number_input("Masukkan Jari_jari Alas (cm):", min_value = 0.0, step = 0.1, format ="%.2f")
    tinggi = st.number_input("Masukkan Tinggi Tabung (cm):", min_value = 0.0, step=0.1, format ="%.2f")

    # Tombol untuk menghitung
    if st.button("Hitung Volume"):
        if jari_jari > 0 and tinggi > 0:
            # objek Tabung
            tabung = Tabung(jari_jari, tinggi)
            volume = tabung.hitung_volume()
            st.success(f"Volume tabung adalah {volume:.2f} cm³")
        else:
            st.error("Jari_jari dan tinggi harus lebih dari 0!")
