import streamlit as st

# Judul
st.title("Dashboard")

# sidebar menu
menu = st.sidebar.radio("Menu Utama", ["Dashboard", "Persegi", "Persegi Panjang", "Tabung", "Kerucut"])

# Tobol Reset Untuk Menghapus Hasil
reset = st.sidebar.button("Reset Hasil")

# Jika tombol reset ditekan maka akan menghapus hasil
if reset:
    st.session_state.clear()
    st.write("Semua hasil sudah di hapus!!")

# menu yang dipilih
if menu == "Dashboard":
    st.header("")
    st.write("")

    # Menampilkan hasil perhitungan yang tersimpan 
    st.subheader("Hasil dari perhitungan")

    # Menggunakan Dictionary untuk Hasil Perhitungan
    hasil_perhitungan = {
        "Persegi": st.session_state.get("luas_persegi",0), 
        "Persegi Panjang": st.session_state.get("luas_persegi_panjang", 0),
        "Tabung": st.session_state.get("volume_tabung", 0),
        "Kerucut": st.session_state.get("volume_kerucut", 0),
    }

    # Menampilkan hasil menggunakan for untuk tabel
    data = {
        "Bentuk":[],
        "Hasil":[]
    }

    for bentuk, hasil in hasil_perhitungan.items():
        data["Bentuk"].append(bentuk)
        data["Hasil"].append(hasil)

    st.table(data)

elif menu == "Persegi":
    st.header("Perhitungan Persegi")
    sisi = st.number_input("Masukkan sisi persegi", min_value=0.0)

    if st.button("Hitung"):
        # Operator untuk menghitung luas persegi
        luas_persegi = sisi ** 2
        st.session_state.luas_persegi = luas_persegi
        st.write(f"Luas Persegi: {luas_persegi}")
        # Penjelasa hasil perhitungan
        
        st.info(f"Hasil Perhitungan adalah  = {luas_persegi}")

elif menu == "Persegi Panjang":
    st.header("Perhitungan Persegi Panjang")
    panjang = st.number_input("Masukkan panjang persegi panjang", min_value=0.0)
    lebar = st.number_input("Masukkan lebar:", min_value=0.0)

    if st.button("Hitung"):
        luas_persegi_panjang = panjang * lebar
        st.session_state.luas_persegi_panjang = luas_persegi_panjang
        st.write(f"Luas Persegi Panjang: {luas_persegi_panjang}")

        st.info(f"Hasil Perhitungan adalah = {luas_persegi_panjang}")

elif menu == "Tabung":
    st.header("Perhitungan Tabung")
    jari_jari = st.number_input("Masukkan jari-jari:", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi:", min_value=0.0)

    if st.button("Hitung"):
        volume_tabung = 3.14 * (jari_jari ** 2) * tinggi
        st.session_state.volume_tabung = volume_tabung
        st.write(f"Volume Tabung: {volume_tabung}")

        st.info(f"Hasil Perhitungan adalah = {volume_tabung}")

elif menu == "Kerucut":
    st.header("Perhitungan Kerucut")
    jari_jari = st.number_input("Masukkan jari-jari:", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi:", min_value=0.0)

    if st.button("Hitung"):
        volume_kerucut = (1 / 3) * 3.14 * (jari_jari **2) * tinggi
        st.session_state.volume_kerucut = volume_kerucut
        st.write(f"Volume Kerucut: {volume_kerucut}")

        st.info(f"Hasil Perhitungan adalah = {volume_kerucut}")

