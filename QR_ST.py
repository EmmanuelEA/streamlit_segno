import streamlit as st
from segno import make_qr
import io
import os

def generate_qr(data, color, scale):
    qr = make_qr(data)
    return qr

color_options = {
    "Black": "black",
    "Dark Blue": "darkblue",
    "Red": "red",
    "Green": "green",
}

st.title("Generador de QR")

data_input = st.text_input("Escribe la información que contendrá tu código QR")
color_selected = st.selectbox("Selecciona el color para tu código QR", list(color_options.keys()))
scale_selected = int(st.selectbox('Selecciona la escala de la imagen:', [1, 5, 10]))

if st.button("Generar el código QR"):
    color = color_options[color_selected]
    qr_code = generate_qr(data_input, color=color, scale=scale_selected) 

    buff = io.BytesIO()
    qr_code.save(buff, kind='svg', scale=scale_selected, dark=color)
    svg_data = buff.getvalue()

    file_path = os.path.join(os.getcwd(), "eea_code.svg")
    with open(file_path, "wb") as f:
        f.write(svg_data)

    st.markdown(svg_data.decode(), unsafe_allow_html=True)

    st.write(f"Archivo guardado en: {file_path}")


html_string = """
<footer style="text-align: center; padding: 10px 0;">
  <p>2024 EEA</p>
</footer>
"""

st.divider()
st.html(html_string)
leftc, centerc, rigthc = st.columns(3)
with centerc:
    st.image("./Emmanuel_linkedin.svg")
