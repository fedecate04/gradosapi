# api_conversion.py

import streamlit as st

def density_to_api(density_kg_m3: float) -> float:
    """
    Convierte densidad (kg/m³) a grados API.
    
    Fórmula:
    API = 141.5 * (999.016 / densidad) - 131.5
    
    :param density_kg_m3: Densidad a 60°F (kg/m³)
    :return: Grados API
    """
    api = 141.5 * (999.016 / density_kg_m3) - 131.5
    return api

# Interfaz Streamlit
st.title("Conversor de Densidad a Grados API")
st.write("Introduce la densidad del crudo a 60°F para obtener el API.")

# Entrada del usuario
density_input = st.number_input("Densidad (kg/m³)", min_value=500.0, max_value=1200.0, value=850.0, step=0.1)

# Calcular API
if st.button("Calcular API"):
    api_value = density_to_api(density_input)
    st.success(f"Grados API: {api_value:.2f}")
