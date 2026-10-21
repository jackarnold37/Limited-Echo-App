import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Cleveland Clinic - Limited Echo Protocol Generator",
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
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Zoom TV (2D)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Color TV", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "PV tilt 2D", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Zoom PV (2D)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "Color PV", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "PARASTERNAL SHORT AXIS (PSAX)", "step": "PSAX LVOT 2D & Color sweep", "condition": "HOCM/Camzyos"},

    # APICAL 4-CHAMBER
    {"window": "APICAL 4-CHAMBER", "step": "LV/RV 2D", "condition": "Default required views"},
    {"window": "APICAL 4-CHAMBER", "step": "Zoom LV / LV Focused View (for strain / GLS)", "condition": "Default required views"},
    {"window": "APICAL 4-CHAMBER", "step": "Long clip Interventricular Septum 2D", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "APICAL 4-CHAMBER", "step": "Color MV", "condition": "Default required views"},
    {"window": "APICAL 4-CHAMBER", "step": "PW MV", "condition": "Mitral Valve"},
    {"window": "APICAL 4-CHAMBER", "step": "PW Mitral inflow with respiratory variation", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "APICAL 4-CHAMBER", "step": "CW MV", "condition": "Mitral Valve"},
    {"window": "APICAL 4-CHAMBER", "step": "Tissue Doppler (Septal Annulus)", "condition": "Default required views"},
    {"window": "APICAL 4-CHAMBER", "step": "Tissue Doppler (Lateral Annulus)", "condition": "Default required views"},
    {"window": "APICAL 4-CHAMBER", "step": "PW Pulmonary Vein flow with respiratory variation (Long clip)", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "APICAL 4-CHAMBER", "step": "Pulmonary Vein Color", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "APICAL 4-CHAMBER", "step": "PW Pulmonary Vein long clip", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "APICAL 4-CHAMBER", "step": "Zoomed 2D (MV)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "APICAL 4-CHAMBER", "step": "Zoomed Color Doppler (MV)", "condition": "Endocarditis / Rule Out Thrombus"},

    # APICAL RV FOCUSED VIEW
    {"window": "APICAL RV FOCUSED VIEW", "step": "2D RV Focused View", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "APICAL RV FOCUSED VIEW", "step": "2D", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "APICAL RV FOCUSED VIEW", "step": "Color Doppler TV", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "APICAL RV FOCUSED VIEW", "step": "PW Tricuspid inflow with respiratory variation", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "APICAL RV FOCUSED VIEW", "step": "CW Doppler TV", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "APICAL RV FOCUSED VIEW", "step": "TR Jet max velocity CW", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "APICAL RV FOCUSED VIEW", "step": "Tricuspid Annular Tissue Doppler (S' / TAPSE)", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "APICAL RV FOCUSED VIEW", "step": "2D", "condition": "Tricuspid Valve"},
    {"window": "APICAL RV FOCUSED VIEW", "step": "Color Doppler TV", "condition": "Tricuspid Valve"},
    {"window": "APICAL RV FOCUSED VIEW", "step": "CW Doppler TV", "condition": "Tricuspid Valve"},

    # MODIFIED / REVERSE APICAL 4-CHAMBER
    {"window": "MODIFIED / REVERSE APICAL 4-CHAMBER", "step": "2D", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "MODIFIED / REVERSE APICAL 4-CHAMBER", "step": "Color Doppler TV", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "MODIFIED / REVERSE APICAL 4-CHAMBER", "step": "CW Doppler TV", "condition": "RV Function & Pulmonary Hypertension"},
    {"window": "MODIFIED / REVERSE APICAL 4-CHAMBER", "step": "2D", "condition": "Tricuspid Valve"},
    {"window": "MODIFIED / REVERSE APICAL 4-CHAMBER", "step": "Color Doppler TV", "condition": "Tricuspid Valve"},
    {"window": "MODIFIED / REVERSE APICAL 4-CHAMBER", "step": "CW Doppler TV", "condition": "Tricuspid Valve"},

    # APICAL 5-CHAMBER
    {"window": "APICAL 5-CHAMBER", "step": "LVOT/AV 2D", "condition": "Default required views"},
    {"window": "APICAL 5-CHAMBER", "step": "Color LVOT/AV", "condition": "Default required views"},
    {"window": "APICAL 5-CHAMBER", "step": "PW LVOT", "condition": "Aortic Valve / TAVR"},
    {"window": "APICAL 5-CHAMBER", "step": "CW AV", "condition": "Aortic Valve / TAVR"},
    {"window": "APICAL 5-CHAMBER", "step": "Zoomed 2D (AV)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "APICAL 5-CHAMBER", "step": "Zoomed Color Doppler (AV)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "APICAL 5-CHAMBER", "step": "Resting LVOT focused view", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 5-CHAMBER", "step": "Resting Color LVOT", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 5-CHAMBER", "step": "CW Resting LVOT gradient", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 5-CHAMBER", "step": "Valsalva LVOT focused view", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 5-CHAMBER", "step": "Valsalva Color LVOT", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 5-CHAMBER", "step": "CW Valsalva LVOT gradient", "condition": "HOCM/Camzyos"},

    # APICAL 2-CHAMBER
    {"window": "APICAL 2-CHAMBER", "step": "2D", "condition": "Default required views"},
    {"window": "APICAL 2-CHAMBER", "step": "Zoom LV / LV Focused View (for strain / GLS)", "condition": "Default required views"},
    {"window": "APICAL 2-CHAMBER", "step": "Color MV", "condition": "Mitral Valve"},
    {"window": "APICAL 2-CHAMBER", "step": "CW MV", "condition": "Mitral Valve"},
    {"window": "APICAL 2-CHAMBER", "step": "Zoomed 2D (MV)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "APICAL 2-CHAMBER", "step": "Zoomed Color Doppler (MV)", "condition": "Endocarditis / Rule Out Thrombus"},

    # APICAL 3-CHAMBER
    {"window": "APICAL 3-CHAMBER", "step": "2D", "condition": "Default required views"},
    {"window": "APICAL 3-CHAMBER", "step": "Zoom LV / LV Focused View (for strain / GLS)", "condition": "Default required views"},
    {"window": "APICAL 3-CHAMBER", "step": "Color LVOT/AV", "condition": "Aortic Valve / TAVR"},
    {"window": "APICAL 3-CHAMBER", "step": "PW LVOT", "condition": "Aortic Valve / TAVR"},
    {"window": "APICAL 3-CHAMBER", "step": "CW AV", "condition": "Aortic Valve / TAVR"},
    {"window": "APICAL 3-CHAMBER", "step": "Color MV", "condition": "Mitral Valve"},
    {"window": "APICAL 3-CHAMBER", "step": "CW MV", "condition": "Mitral Valve"},
    {"window": "APICAL 3-CHAMBER", "step": "Zoomed 2D (AV, MV)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "APICAL 3-CHAMBER", "step": "Zoomed Color Doppler (AV, MV)", "condition": "Endocarditis / Rule Out Thrombus"},
    {"window": "APICAL 3-CHAMBER", "step": "Resting LVOT focused view", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 3-CHAMBER", "step": "Resting Color LVOT", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 3-CHAMBER", "step": "CW Resting LVOT gradient", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 3-CHAMBER", "step": "Valsalva LVOT focused view", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 3-CHAMBER", "step": "Valsalva Color LVOT", "condition": "HOCM/Camzyos"},
    {"window": "APICAL 3-CHAMBER", "step": "CW Valsalva LVOT gradient", "condition": "HOCM/Camzyos"},

    # SUBCOSTAL
    {"window": "SUBCOSTAL", "step": "Subcostal 4-Chamber 2D", "condition": "Default required views"},
    {"window": "SUBCOSTAL", "step": "Subcostal 4-Chamber Color Doppler", "condition": "Default required views"},
    {"window": "SUBCOSTAL", "step": "Subcostal Hepatic Vein Pulsed-Wave Doppler Flow", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "SUBCOSTAL", "step": "Subcostal IVC with sniff test", "condition": "Default required views"},
    {"window": "SUBCOSTAL", "step": "Subcostal M-mode Right Atrium (RA collapse)", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "SUBCOSTAL", "step": "Subcostal M-mode Right Ventricle (RV collapse)", "condition": "Pericardial Effusion / Tamponade"},

    # SUPRASTERNAL
    {"window": "SUPRASTERNAL", "step": "Aortic Arch 2D", "condition": "Aorta"},
    {"window": "SUPRASTERNAL", "step": "Color Descending Aorta", "condition": "Aorta"},
    {"window": "SUPRASTERNAL", "step": "CW Descending Aorta", "condition": "Aorta"},
    {"window": "SUPRASTERNAL", "step": "SVC Color Doppler", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "SUPRASTERNAL", "step": "SVC PW Doppler", "condition": "Pericardial Effusion / Tamponade"},
    {"window": "SUPRASTERNAL", "step": "Suprasternal Notch 2D", "condition": "Aortic Valve / TAVR"},
    {"window": "SUPRASTERNAL", "step": "Suprasternal Notch Color", "condition": "Aortic Valve / TAVR"},
    {"window": "SUPRASTERNAL", "step": "Suprasternal Notch CW", "condition": "Aortic Valve / TAVR"},
    {"window": "SUPRASTERNAL", "step": "Suprasternal Notch PW", "condition": "Aortic Valve / TAVR"},

    # RIGHT STERNAL BORDER
    {"window": "RIGHT STERNAL BORDER", "step": "Right Sternal Border Aorta 2D", "condition": "Aorta"},
    {"window": "RIGHT STERNAL BORDER", "step": "Right Sternal Border Aorta Color", "condition": "Aorta"},
    {"window": "RIGHT STERNAL BORDER", "step": "Right Sternal Border 2D", "condition": "Aortic Valve / TAVR"},
    {"window": "RIGHT STERNAL BORDER", "step": "Right Sternal Border Color", "condition": "Aortic Valve / TAVR"},
    {"window": "RIGHT STERNAL BORDER", "step": "Right Sternal Border CW", "condition": "Aortic Valve / TAVR"}
]

# App Title
st.title("Cleveland Clinic - Limited Echo Protocol Generator")
st.markdown("Select target assessments below to dynamically generate the required protocol checklist.")

# Checkboxes placed front and center
with st.expander("📌 Tap here to select Target Assessments", expanded=True):
    # Default required views is permanently included and cannot be unchecked
    selected_conditions = ["Default required views"]
    
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Default required views", value=True, disabled=True)
        if st.checkbox("LV Function & Wall Motion", value=False):
            selected_conditions.append("LV Function & Wall Motion")
        if st.checkbox("Pericardial Effusion / Tamponade", value=False):
            selected_conditions.append("Pericardial Effusion / Tamponade")
        if st.checkbox("RV Function & Pulmonary Hypertension", value=False):
            selected_conditions.append("RV Function & Pulmonary Hypertension")
        if st.checkbox("Aortic Valve / TAVR", value=False):
            selected_conditions.append("Aortic Valve / TAVR")
        if st.checkbox("Mitral Valve", value=False):
            selected_conditions.append("Mitral Valve")
    with col2:
        if st.checkbox("Tricuspid Valve", value=False):
            selected_conditions.append("Tricuspid Valve")
        if st.checkbox("Pulmonic Valve", value=False):
            selected_conditions.append("Pulmonic Valve")
        if st.checkbox("Endocarditis / Rule Out Thrombus", value=False):
            selected_conditions.append("Endocarditis / Rule Out Thrombus")
        if st.checkbox("Aorta", value=False):
            selected_conditions.append("Aorta")
        if st.checkbox("HOCM/Camzyos", value=False):
            selected_conditions.append("HOCM/Camzyos")

# Filter Database based on selections
active_steps = [item for item in PROTOCOL_DATABASE if item["condition"] in selected_conditions]

# Group by Window Header
grouped_protocol = {}
for item in active_steps:
    win = item["window"]
    if win not in grouped_protocol:
        grouped_protocol[win] = []
    grouped_protocol[win].append(item["step"])

# Display Protocol Output
st.markdown("---")
st.subheader("Required Views Protocol")

total_pictures = len(active_steps)

if not grouped_protocol:
    st.info("Please select at least one assessment.")
else:
    for window, steps in grouped_protocol.items():
        st.markdown(f'<div class="window-header">{window}</div>', unsafe_allow_html=True)
        for step in steps:
            st.markdown(f'<div class="step-item">• {step}</div>', unsafe_allow_html=True)
    
    # Total Estimated Pictures Metric Box
    st.markdown(
        f'<div class="metric-box" style="color: #002D62;">Total Estimated Pictures: {total_pictures} (± 5 pictures)</div>',
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown("*Tip: Press `Ctrl + P` or `Cmd + P` in your browser to cleanly print or save this protocol checklist as a PDF.*")
