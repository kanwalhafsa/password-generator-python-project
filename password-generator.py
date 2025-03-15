import streamlit as st
import random
import string
import pyperclip
import time

# 🎨 Custom Styles
st.markdown(
    """
    <style>
        .big-text { font-size:24px; font-weight:bold; text-align:center; }
        .strength-weak { color: red; font-weight: bold; }
        .strength-medium { color: orange; font-weight: bold; }
        .strength-strong { color: green; font-weight: bold; }
        .password-box { background-color: #f4f4f4; padding: 10px; border-radius: 8px; font-size: 18px; text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🎯 Password Generator Function
def generate_password(length, use_digits, use_special, use_uppercase):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

# 🎯 Password Strength Evaluation
def evaluate_strength(password):
    if len(password) < 8:
        return "Weak", "strength-weak"
    elif len(password) < 12:
        return "Medium", "strength-medium"
    else:
        return "Strong", "strength-strong"

# 🎨 UI Design
st.title("🔐 Advanced Password Generator")
st.markdown('<p class="big-text">Generate secure and stylish passwords instantly! 🔥</p>', unsafe_allow_html=True)

# 🎚 User Inputs
length = st.slider("🔢 Select Password Length", min_value=6, max_value=32, value=12)
use_uppercase = st.checkbox("🔠 Include Uppercase Letters")
use_digits = st.checkbox("🔢 Include Digits (0-9)")
use_special = st.checkbox("🔣 Include Special Characters (!@#$%^&)")

# 🎯 Generate Password & Evaluate Strength
password = generate_password(length, use_digits, use_special, use_uppercase)
strength_text, strength_class = evaluate_strength(password)

# 📌 Display Password Properly
st.text_input("🔑 Generated Password:", password, disabled=True)


# 🔥 Strength Meter
st.markdown(f'<p class="{strength_class}">🛡 Password Strength: {strength_text}</p>', unsafe_allow_html=True)

# 📋 Copy Button
if st.button("📋 Copy Password"):
    pyperclip.copy(password)
    st.toast("✅ Password copied to clipboard!", icon="🔑")

# 📝 Footer
st.write("---")
st.markdown("💡 *Use a mix of uppercase, lowercase, numbers, and special characters for a stronger password!*")
