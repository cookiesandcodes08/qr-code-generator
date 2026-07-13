import streamlit as st
import qrcode

st.title("QR Code Generator")

data = st.text_input("Enter a URL or Text")

if st.button("Generate QR Code"):
    if data:
        img = qrcode.make(data)

        img.save("QRcode.png")   # Save first

        st.image("QRcode.png")   # Display the saved image

        st.success("QR Code Generated Successfully!")

    else:
        st.warning("Please enter some text first!")