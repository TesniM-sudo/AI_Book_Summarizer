import streamlit as st
import base64
from pathlib import Path

from utils import read_pdf, split_text
from summarizer import summarize_chunks, final_summary

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Book Summarizer",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ------------------ BACKGROUND ------------------
def set_background(image_filename):
    """Set background image"""
    try:
        image_path = Path(__file__).parent / "assets" / image_filename

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
                padding-top: 5rem;
                padding-bottom: 5rem;
                max-width: 100%;
            }}

            /* Title styling - left side */
            .title-text {{
                font-family: 'Georgia', serif;
                font-size: 4rem;
                font-style: italic;
                color: #f5e6d3;
                text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
                line-height: 1.2;
                margin-bottom: 2rem;
            }}

            /* Button container - right side */
            .button-container {{
                display: flex;
                flex-direction: column;
                gap: 1.5rem;
                align-items: flex-end;
                justify-content: center;
                padding: 2rem;
            }}

            /* Custom buttons */
            .custom-button {{
                background-color: rgba(212, 165, 116, 0.7);
                color: #3e2723;
                font-size: 1.2rem;
                font-weight: bold;
                padding: 1rem 3rem;
                border-radius: 50px;
                border: none;
                cursor: pointer;
                text-align: center;
                min-width: 250px;
                backdrop-filter: blur(5px);
                transition: all 0.3s ease;
            }}

            .custom-button:hover {{
                background-color: rgba(212, 165, 116, 0.9);
                transform: translateY(-3px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }}

            /* File uploader styling */
            [data-testid="stFileUploader"] {{
                background-color: rgba(212, 165, 116, 0.7);
                padding: 1rem 3rem;
                border-radius: 50px;
                border: none;
                backdrop-filter: blur(5px);
                min-width: 250px;
            }}

            [data-testid="stFileUploader"] label {{
                color: #3e2723 !important;
                font-size: 1.2rem !important;
                font-weight: bold !important;
                text-align: center;
            }}

            [data-testid="stFileUploader"] section {{
                border: none !important;
            }}

            /* Streamlit button styling */
            .stButton > button {{
                background-color: rgba(212, 165, 116, 0.7);
                color: #3e2723;
                font-size: 1.2rem;
                font-weight: bold;
                padding: 1rem 3rem;
                border-radius: 50px;
                border: none;
                min-width: 250px;
                backdrop-filter: blur(5px);
                transition: all 0.3s ease;
            }}

            .stButton > button:hover {{
                background-color: rgba(212, 165, 116, 0.9);
                transform: translateY(-3px);
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }}

            /* Alert boxes */
            .stAlert {{
                background-color: rgba(255, 255, 255, 0.8);
                backdrop-filter: blur(5px);
                border-radius: 10px;
            }}

            /* Spinner */
            .stSpinner > div {{
                border-top-color: #d4a574 !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        pass


set_background("background.jpg")

# Initialize session state
if 'summary' not in st.session_state:
    st.session_state.summary = None
if 'pdf_name' not in st.session_state:
    st.session_state.pdf_name = None
if 'pdf_uploaded' not in st.session_state:
    st.session_state.pdf_uploaded = False

# ------------------ LAYOUT: LEFT TITLE + RIGHT BUTTONS ------------------
col1, col2 = st.columns([1.2, 1])

with col1:
    # Left side - Title
    st.markdown("""
    <div class="title-text">
        AI Book<br>
        Summarizer<br>
        Mockup
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Right side - Buttons
    st.markdown("<br><br><br>", unsafe_allow_html=True)  # Spacing

    # Upload PDF button
    pdf_file = st.file_uploader(
        "UPLOAD PDF",
        type=["pdf"],
        label_visibility="collapsed"
    )

    if pdf_file is not None:
        st.session_state.pdf_uploaded = True
        st.success(f"✓ {pdf_file.name}")

    # Summarize button
    if st.session_state.pdf_uploaded and pdf_file is not None:
        if st.button("SUMMARIZE", use_container_width=True):
            with st.spinner("🔄 Summarizing your book..."):
                try:
                    # Process the PDF
                    text = read_pdf(pdf_file)
                    chunks = split_text(text)

                    # Generate summary
                    summary_text = summarize_chunks(chunks)
                    final = final_summary(summary_text)

                    # Store in session state
                    st.session_state.summary = final
                    st.session_state.pdf_name = pdf_file.name

                    st.success("✅ Summary completed!")
                    st.balloons()

                    # Auto-navigate to summary page - FIXED PATH
                    st.switch_page("pages/Summary.py")

                except Exception as e:
                    st.error(f"❌ Error: {e}")
    else:
        # Disabled state button
        st.markdown("""
        <div style="text-align: right;">
            <button class="custom-button" disabled style="opacity: 0.5; cursor: not-allowed;">
                SUMMARIZE
            </button>
        </div>
        """, unsafe_allow_html=True)