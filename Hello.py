import streamlit as st

st.set_page_config(
    page_title="Hola! Soy Fany",
    page_icon="👋",
)

st.write("# Bienvenido a Fany! 👋")

st.sidebar.success("Elegí la conversación en la que te puedo ayudar.")

st.markdown(
    """
    Fany es un beta de un asistente para conversaciones con clientes basado en el Framework de acercamiento al Negocio (FAN). \n \n La idea es ayudarte a producir propuestas e ideas que tengan fit con la experiencia, valor y empatía que busca. \n\nComo asistente, Fany te inspira para que lleves tu conversacion adelante. 
    \n\n **👈 Elegí una conversación de la izquierda ** 
    \n\n ### Queres saber más?
    \n- Docu [documentation](https://docs.google.com/presentation/d/1E3GP2ZKFpw3iCw7bBwWAJ4SwDxEXqSW5CCl5KYzu8FQ/edit#slide=id.g22cd5875b8d_5_0)
"""
)