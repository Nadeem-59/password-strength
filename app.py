import streamlit as st
from password_strength import PasswordStats


st.set_page_config(page_title="🔐 Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    stats = PasswordStats(password)

    # Score: 0 (weak) to 1 (strong)
    score = stats.strength()
    length = stats.length
    letters = stats.letters
    numbers = stats.numbers
    special_chars = stats.special_characters

    # Check for common patterns manually
    common_sequences = ['123', 'abc', 'password', 'qwerty', '111', '000']
    found_sequence = any(seq in password.lower() for seq in common_sequences)

    st.markdown("### 🧪 Strength Analysis:")

    st.write("🔢 Length (8+ recommended):", "✅" if length >= 8 else "❌")
    st.write("🔤 Letters:", "✅" if letters > 0 else "❌")
    st.write("🔢 Numbers:", "✅" if numbers > 0 else "❌")
    st.write("🔣 Special Characters:", "✅" if special_chars > 0 else "❌")
    st.write("🧬 Common Patterns:", "❌" if found_sequence else "✅")

    st.markdown("### 📊 Overall Strength:")

    if score < 0.3:
        st.error("😖 Weak Password — Too easy to guess!")
    elif score < 0.7:
        st.warning("😐 Moderate Password — Can be improved.")
    else:
        st.success("💪 Strong Password — Looks good!")

    st.markdown("---")
    st.markdown("🔁 Try different combinations to get a strong password!")

else:
    st.info("👆 Please enter a password above to check its strength.")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsDZR9Sz-K8oT8StTlI3heNoW8FScpMYoIXQ&s");
        background-size: cover;
        background-position: center;
    }       
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .word-display {
        font-size: 2.5rem;
        letter-spacing: 0.5rem;
        font-family: monospace;
    }
    .game-title {
        color: #2c3e50;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .category {
        color: purple;
        font-weight: bold;
    }
    .score {
        font-size: 1.2rem;
        color: #2980b9;
    }
    </style>
    """, unsafe_allow_html=True)    
