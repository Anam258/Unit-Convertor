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
        /* Full viewport height and margin reset */
        body {
            background-color: #FFC5D3 !important;
            margin: 0;
            padding: 0;
            height: 100vh; /* Full height */
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden; /* Prevent unnecessary scroll */
        }

        /* Centering content vertically and horizontally */
        .stApp {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100%; /* Full height */
            width: 100%; /* Full width */
            color: #000000 !important; /* Black text */
        }

        /* Adjusting the size of input boxes and select dropdowns */
        .stSelectbox, .stTextInput, .stNumberInput {
            margin: 10px 0;
            width: 100%;
            max-width: 500px; /* Limiting max width for better alignment */
        }

        /* Button Styling */
        .stButton button {
            background: linear-gradient(145deg, #FF69B4, #FF4786) !important; /* Gradient pink color */
            color: white !important;
            border-radius: 12px;
            font-size: 18px;
            padding: 12px 30px;
            border: none;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease-in-out;
        }

        .stButton button:hover {
            background: linear-gradient(145deg, #FF4786, #FF69B4) !important; /* Lighter pink on hover */
            transform: translateY(-3px); /* Slight button lift on hover */
            box-shadow: 2px 5px 15px rgba(0, 0, 0, 0.2);
        }

        /* Label Styling for input fields */
        .stSelectbox label, .stTextInput label, .stNumberInput label {
            font-size: 16px;
            font-weight: bold;
            color: #000000 !important;
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
