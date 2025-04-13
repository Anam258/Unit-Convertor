import streamlit as st
import time

# Set page title and icon
st.set_page_config(
    page_title="ProConverter 🛠️",
    page_icon="⚙️",
    layout="centered"
)

# Custom CSS for professional look
st.markdown(
    """
    <style>
    /* Set a clean, neutral background */
    body {
        background-color: #F8F8F8 !important;
    }
    
    .stApp {
        background-color: #F8F8F8;
        color: #333 !important;
    }

    /* Main container styling */
    .main-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .card {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        width: 100%;
        max-width: 650px;
    }

    /* Title styling */
    .stTitle {
        font-size: 36px;
        font-weight: 600;
        color: #2c3e50;
    }

    /* Subtitle for description */
    .stSubtitle {
        font-size: 18px;
        color: #7f8c8d;
        margin-bottom: 20px;
        font-weight: 400;
    }

    /* Button styling */
    .stButton button {
        background-color: #2980b9 !important;
        color: white !important;
        border-radius: 8px;
        font-size: 18px;
        padding: 12px 0;
        width: 100%;
        font-weight: 500;
        transition: background-color 0.3s ease;
    }

    .stButton button:hover {
        background-color: #3498db !important;
    }

    /* Input fields styling */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background-color: #f1f1f1 !important;
        color: #2c3e50 !important;
        border-radius: 8px;
        font-size: 16px;
        padding: 12px;
        width: 100%;
    }

    .stTextInput label, .stNumberInput label, .stSelectbox label {
        font-size: 14px;
        color: #2980b9 !important;
    }

    /* Success message styling */
    .stSuccess {
        background-color: #e6f7ff !important;
        color: #3498db !important;
        padding: 12px;
        border-radius: 8px;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("ProConverter ⚙️")
st.subheader("**Efficient and Professional Unit Conversion Tool**")
st.write("**ProConverter is a sleek, precise tool to convert units with ease. It's fast, reliable, and user-friendly.**")

# Conversion Categories
conversion_type = st.selectbox("Select Conversion Type", [
    "Length", "Weight", "Temperature", "Area", "Volume", "Speed", "Time", "Energy", "Pressure"
])

# Conversion Functions
def convert_units(value, from_unit, to_unit, conversion_dict):
    return value * (conversion_dict[to_unit] / conversion_dict[from_unit])

def convert_temperature(value, from_unit, to_unit):
    conversions = {
        ("celsius", "fahrenheit"): lambda v: (v * 9/5) + 32,
        ("fahrenheit", "celsius"): lambda v: (v - 32) * 5/9,
        ("celsius", "kelvin"): lambda v: v + 273.15,
        ("kelvin", "celsius"): lambda v: v - 273.15,
        ("fahrenheit", "kelvin"): lambda v: (v - 32) * 5/9 + 273.15,
        ("kelvin", "fahrenheit"): lambda v: (v - 273.15) * 9/5 + 32,
    }
    return conversions.get((from_unit, to_unit), lambda v: v)(value)

# Unit Dictionaries
unit_dicts = {
    "Length": {"meters": 1, "kilometers": 0.001, "centimeters": 100, "inches": 39.37, "feet": 3.281, "miles": 0.000621},
    "Weight": {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274},
    "Area": {"square_meters": 1, "square_kilometers": 0.000001, "square_feet": 10.7639, "acres": 0.000247105},
    "Volume": {"liters": 1, "milliliters": 1000, "gallons": 0.264172, "cubic_feet": 0.0353147},
    "Speed": {"m/s": 1, "km/h": 3.6, "mph": 2.237, "knots": 1.944},
    "Time": {"seconds": 1, "minutes": 1/60, "hours": 1/3600, "days": 1/86400},
    "Energy": {"joules": 1, "kilojoules": 0.001, "calories": 0.239, "kWh": 2.7778e-7},
    "Pressure": {"pascals": 1, "bar": 1e-5, "psi": 0.000145, "atm": 9.8692e-6}
}

# Input Fields
value = st.number_input("Enter value for conversion", value=1.0)
units = unit_dicts.get(conversion_type, {})
if conversion_type == "Temperature":
    from_unit = st.selectbox("From", ["celsius", "fahrenheit", "kelvin"])
    to_unit = st.selectbox("To", ["celsius", "fahrenheit", "kelvin"])
    result = convert_temperature(value, from_unit, to_unit)
else:
    from_unit = st.selectbox("From", list(units.keys()))
    to_unit = st.selectbox("To", list(units.keys()))
    result = convert_units(value, from_unit, to_unit, units)

# Convert Button
if st.button("Convert"):
    with st.spinner("Converting..."):
        time.sleep(1)
        st.success("Converted value: {:.4f} {}".format(result, to_unit))

st.markdown("</div></div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("© 2025 ProConverter Inc. All rights reserved.")
