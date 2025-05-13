import streamlit as st
import base64

st.set_page_config(page_title="Secret Encryptor", layout="centered", page_icon="🔐")

# Title and description
st.markdown("""
    <h2 style='text-align: center; color: #4B0082;'>Secret Message Encryptor & Decryptor</h2>
    <p style='text-align: center;'>Secure your messages using Base64 encryption. Enter a message and a secret key to encrypt or decrypt.</p>
    <hr style='border: 1px solid #eee;'>
""", unsafe_allow_html=True)

# Layout container
with st.container():
    st.markdown("####  Enter your message:")
    message = st.text_area("", placeholder="Type your message here...", height=150)

    st.markdown("####  Enter Secret Key:")
    password = st.text_input("", type="password", placeholder="Enter your password (Hint: 1234)")

    action = st.radio("Choose an action:", ["Encrypt", "Decrypt"], horizontal=True)

    if st.button("Submit"):
        if password == "1234":
            if action == "Encrypt":
                encoded_bytes = base64.b64encode(message.encode("ascii"))
                encoded_str = encoded_bytes.decode("ascii")
                st.success("✅ Encrypted Message:")
                st.code(encoded_str, language='text')

            elif action == "Decrypt":
                try:
                    decoded_bytes = base64.b64decode(message.encode("ascii"))
                    decoded_str = decoded_bytes.decode("ascii")
                    st.success("✅ Decrypted Message:")
                    st.code(decoded_str, language='text')
                except Exception:
                    st.error("❌ Invalid input or corrupted encrypted text.")
        elif password == "":
            st.warning("⚠️ Please enter the secret key.")
        else:
            st.error("❌ Incorrect password.")

st.markdown("---")
