import streamlit as st
from PIL import Image

# Load your custom image using its exact filename
try:
    icon = Image.open("Limited_icon.jpg")
    st.set_page_config(
        page_title="Cleveland Clinic - Limited Echo Protocol Generator",
        page_icon=icon,
        layout="wide"
    )
except FileNotFoundError:
    st.set_page_config(
        page_title="Cleveland Clinic - Limited Echo Protocol Generator",
        page_icon="🩺",
        layout="wide"
    )

# Custom Styling (Cleveland Clinic Navy Blue & Clean Healthcare Aesthetic)
st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #002D62;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .window-header {
        background-color: #002D62;
        color: white;
        padding: 8px 12px;
        font-weight: bold;
        font-size: 16px;
        border-radius: 4px;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    .step-item {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 14px;
        color: #222222;
        padding: 2px 0px 2px 15px;
    }
    .metric-box {
        background-color: #F0F4F8;
        border-left: 5px solid #002D62;
        padding: 10px 15px;
        font-size: 16px;
        font-weight: bold;
        color: #002D62;
        margin-top: 20px;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Master Database of Windows, Steps, and Required Conditions
PROTOCOL_DATABASE = [
    # PLAX
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Zoomed-out wide-field PLAX 2D", "condition": "Default required views"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Standard PLAX 2D with increased depth", "condition": "Default required views"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Zoom AV & MV (2D)", "condition": "Default required views"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Color Doppler on zoomed AV & MV", "condition": "Default required views"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "M-mode LV (mid-ventricle)", "condition": "LV Function & Wall Motion"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Long clip LV 2D", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Long clip M-mode LV", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "M-mode MV", "condition": "Mitral Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Zoom AV", "condition": "Aortic Valve / TAVR"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Color zoom AV", "condition": "Aortic Valve / TAVR"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Zoom MV", "condition": "Mitral Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Color zoom MV", "condition": "Mitral Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "RV Inflow 2D", "condition": "Tricuspid Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "RV Inflow Color Doppler", "condition": "Tricuspid Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "RV Inflow CW Doppler TV", "condition": "Tricuspid Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "RV Inflow TR Jet max velocity", "condition": "Tricuspid Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "RV Outflow / RVOT 2D (Pulmonic)", "condition": "Pulmonic Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "RV Outflow / RVOT Color Doppler (Pulmonic)", "condition": "Pulmonic Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "RVOT / PV PW Doppler", "condition": "Pulmonic Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "RVOT / PV CW Doppler", "condition": "Pulmonic Valve"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "TV tilt 2D", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Zoom TV (2D)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Color TV", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "PV tilt 2D", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Zoom PV (2D)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Color PV", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Ascending Aorta 2D", "condition": "Aorta"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Ascending Aorta Color", "condition": "Aorta"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Zoom LVOT (2D)", "condition": "HOCM/Camzyos"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Color LVOT", "condition": "HOCM/Camzyos"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Tricuspid Valve Tilt 2D", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Tricuspid Valve Color", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Tricuspid Valve CW Doppler", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "PARASTERNAL LONG AXIS (PLAX)", "step": "Pulmonary Valve Tilt", "condition": "RV Function & Pulmonary Hypertension"},

    # PSAX
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Aortic level 2D (AV, TV)", "condition": "Default required views"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "PSAX Zoomed AV 2D", "condition": "Default required views"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "PSAX Aortic Level Color Doppler (AV)", "condition": "Default required views"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "CW TV", "condition": "Tricuspid Valve"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "RVOT / PV 2D", "condition": "Pulmonic Valve"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "RVOT / PV Color Doppler", "condition": "Pulmonic Valve"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "PV PW Doppler", "condition": "Pulmonic Valve"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "PV CW Doppler", "condition": "Pulmonic Valve"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Mitral level 2D", "condition": "Default required views"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Mitral level Color Doppler", "condition": "Default required views"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Zoom Mitral Valve (2D)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Color Mitral Valve", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "PSAX Mid-LV Papillary 2D", "condition": "Default required views"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Long clip PSAX Mid-LV Papillary 2D", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Long clip PSAX M-mode Papillary level", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "PSAX Apex", "condition": "Default required views"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "TV tilt 2D", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL
