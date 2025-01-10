from openai import OpenAI
import streamlit as st


class BusinessConversationPrompt:
    def getIdea(country,industry,market_variables,kpis,consumer_trend,industry_trend,problem):   
        client = OpenAI(api_key=st.secrets["openai_key"])
        formattedText = f"""Como business developer o vendedor de Flux IT, una empresa que vende productos digitales basados en experience design y desarrollo de software quiero que me propongas una idea para un cliente. La idea que me propongas debe abarcar todos los puntos a continuacion, debe ser profesional y debe basarse en la comprension de la situacion del cliente. 
 1- El mercado target es {country}. 
 2- La situacion planteada por el cliente es esta:{problem} 
 3- La industria o rubro en la que se debe basar la idea es {industry} 
 4- Se debe mejorar el este indicador de negocio: {kpis} 
 5- Se debe usar la tendencia de consumo: {consumer_trend} 
 6- Se debe usar la tendencia de industria: {industry_trend}
 7- La situacion del mercado de los clientes se encuentra condicionada por {market_variables}
 7- Se debe poder explicitar a qué business capabilities de ACORD o cualquier otra arquitectura de empresas de la industria de seguro la idea que propongas 
 se podría asociar"""


        response = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": formattedText}])
        msg = response.choices[0].message.content
    
        return msg

