import streamlit as st
import base64
from pathlib import Path

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Summary Results",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ------------------ BACKGROUND ------------------
def set_background(image_filename):
    """Set background image"""
    try:
        # Go up one level since we're in pages/ folder
        image_path = Path(__file__).parent.parent / "assets" / image_filename

        if not image_path.exists():
            return

        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()

        st.markdown(
            f"""
            <style>
            /* Background */
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            /* Hide default Streamlit elements */
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}

            /* Main container */
            .main .block-container {{
                padding-top: 3rem;
                max-width: 1200px;
            }}

            /* Title */
            .summary-title {{
                font-family: 'Georgia', serif;
                font-size: 3rem;
                font-style: italic;
                color: #f5e6d3;
                text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
                text-align: center;
                margin-bottom: 2rem;
            }}

            /* Summary box */
            .summary-box {{
                background-color: rgba(255, 248, 240, 0.85);
                padding: 3rem;
                border-radius: 20px;
                border-left: 5px solid #d4a574;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
                backdrop-filter: blur(10px);
                margin: 2rem 0;
                font-size: 1.1rem;
                line-height: 1.8;
                color: #3e2723;
            }}

            /* Buttons */
            .stButton > button {{
                background-color: rgba(212, 165, 116, 0.8);
                color: #3e2723;
                font-size: 1.1rem;
                font-weight: bold;
                padding: 0.8rem 2.5rem;
                border-radius: 50px;
                border: none;
                backdrop-filter: blur(5px);
                transition: all 0.3s ease;
            }}

            .stButton > button:hover {{
                background-color: rgba(212, 165, 116, 1);
                transform: translateY(-3px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }}

            .stDownloadButton > button {{
                background-color: rgba(74, 124, 89, 0.8);
                color: white;
                font-size: 1.1rem;
                font-weight: bold;
                padding: 0.8rem 2.5rem;
                border-radius: 50px;
                border: none;
                backdrop-filter: blur(5px);
                transition: all 0.3s ease;
            }}

            .stDownloadButton > button:hover {{
                background-color: rgba(74, 124, 89, 1);
                transform: translateY(-3px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }}

            /* PDF name tag */
            .pdf-name {{
                background-color: rgba(212, 165, 116, 0.6);
                color: #3e2723;
                padding: 0.5rem 1.5rem;
                border-radius: 20px;
                display: inline-block;
                margin-bottom: 1rem;
                font-weight: bold;
                backdrop-filter: blur(5px);
            }}

            /* Alert boxes */
            .stAlert {{
                background-color: rgba(255, 255, 255, 0.85);
                backdrop-filter: blur(5px);
                border-radius: 15px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        pass


set_background("background.jpg")

# ------------------ HEADER ------------------
st.markdown("""
<div class="summary-title">
    📘 Book Summary
</div>
""", unsafe_allow_html=True)

# ------------------ DISPLAY SUMMARY ------------------
if st.session_state.get('summary') is None:
    st.warning("⚠️ No summary available yet!")
    st.info("Please go back to the main page and upload a PDF to summarize")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Upload", use_container_width=True):
            st.switch_page("app.py")
else:
    # Display PDF name
    if st.session_state.get('pdf_name'):
        st.markdown(f"""
        <div style="text-align: center;">
            <span class="pdf-name">📄 {st.session_state.pdf_name}</span>
        </div>
        """, unsafe_allow_html=True)

    # Display summary
    st.markdown(f"""
    <div class="summary-box">
        {st.session_state.summary.replace(chr(10), '<br>')}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Action buttons - centered
    col1, col2, col3, col4, col5 = st.columns([1, 1.5, 0.5, 1.5, 1])

    with col2:
        # Download button
        st.download_button(
            label="💾 Download Summary",
            data=st.session_state.summary,
            file_name=f"summary_{st.session_state.pdf_name.replace('.pdf', '.txt')}",
            mime="text/plain",
            use_container_width=True
        )

    with col4:
        # New summary button
        if st.button("📚 New Summary", use_container_width=True):
            # Clear session state
            st.session_state.summary = None
            st.session_state.pdf_name = None
            st.session_state.pdf_uploaded = False
            st.switch_page("app.py")