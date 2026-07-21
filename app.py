import streamlit as st
import qrcode

st.title("QRify")

data = st.text_input("Enter a URL or Text of a website :)")

if st.button("QRify!"):
    if data:
        img = qrcode.make(data)

        # Save QR code
        img.save("QRcode.png")

        # Display QR code
        st.image("QRcode.png")

        # Download button
        with open("QRcode.png", "rb") as file:
            st.download_button(
                label="📥 Download QR Code",
                data=file,
                file_name="QRcode.png",
                mime="image/png"
            )

        st.success("🎉 QRify generated a QR code successfully!")

    else:
        st.warning("Please enter some text first!")