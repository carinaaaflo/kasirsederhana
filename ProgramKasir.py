import streamlit as st

st.title("Kasir Chilless Cafe")
st.write("-------------------------- Selamat Datang Di Chilless Cafe --------------------------")

st.write("====================== Daftar Menu ======================")

st.write("1. Chicken Ball  :           @23000")
st.write("2. French Fries  :           @15000")
st.write("3. Vanila Latte  :           @18000")
st.write("4. Rose Tea      :           @15000")
st.write("5. Dumpling      :           @12000")
st.write("6. Ice Cream     :           @10000")
st.write("7. Pecel Buaya Darat :       @200000")
st.write("8. Nasi Goreng Cacing Kremi :@150000") 

st.write("====================== Daftar Menu ======================")

    

nama = st.text_input('Nama pelanggan')
beli = int(st.number_input("Pilih Menu (nomor booking) :"))
jumlah =int(st.number_input("Jumlah Pesanan :"))
totalharga = jumlah*beli


st.write("====================== Detail Pembayaran ======================")
st.write("Nama pelanggan           : ",nama)
st.write("Menu yang dipesan        : ",beli)
st.write("Jumlah yang dipesan      : ",jumlah)
st.write("Total Biaya              : ",totalharga)
st.write("                TERIMA KASIH TELAH MEMESAN DI CAFE KAMI ")