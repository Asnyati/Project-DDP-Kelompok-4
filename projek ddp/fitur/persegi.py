import streamlit as st

def run():
    st.title("Menghitung Luas Persegi")
    sisi = st.number_input("Masukkan Panjang Sisi (cm):", min_value=0.0, format="%.2f")
    if st.button("Hitung Luas"):
        luas = sisi * sisi
        st.success(f"Luas persegi adalah {luas:.2f} cm²")

