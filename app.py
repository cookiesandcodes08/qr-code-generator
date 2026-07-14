import streamlit as st
import qrcode

st.title("QRify")

data = st.text_input("Enter a URL or Text of a website :) ")

if st.button("QRify!"): #used for button creation
    if data:
        img = qrcode.make(data)

        img.save("QRcode.png")   # Save first

        st.image("QRcode.png")   # Display the saved image

        st.success("QRify generated a QR for your website!")

    else:
        st.warning("Please enter some text first!")