"""
UI para conversaciones de negocio, segun especificación de framework de acercanmiento a negocio.

"""

import streamlit as st
from openai import OpenAI
import time
from Utils import BusinessConversationPrompt

EXPANDER_TRANSITION_TIME = 2

def generateAnswer():
  return None
  

def buildMarketVariables() -> list:

  options_mkt_variables = list()

  if st.session_state.my_country == "Argentina":
    options_mkt_variables = ['Aumento de competencia por precio','Inflación','Baja de salario real de los clientes',
      'Baja de confianza en las empresas por parte del consumidor','Aumento desconfianza con el producto de seguros']
  else:
    options_mkt_variables = ['Inflación']    

  return options_mkt_variables

def generateAnswer():
   
  time.sleep(EXPANDER_TRANSITION_TIME)
  st.session_state.param_expanded = False

  country = st.session_state.my_country
  industry = st.session_state.my_industry
  market_variables = st.session_state.my_market_variables
  kpis = st.session_state.my_kpis
  consumer_trend = st.session_state.my_consumer_trend
  industry_trend = st.session_state.my_industry_trend
  problem = st.session_state.my_problem


  idea = "Yo, como Fany, asistente a business developers y owners de oportunidades de negocio, te sugiero esta idea...\n" + BusinessConversationPrompt.getIdea(country,industry,market_variables,kpis,consumer_trend,industry_trend,problem) + "\n \n \n Comentame si está bien o la cambiarías."
   
  st.session_state.messages.append({"role": "assistant", "content": idea})
  st.session_state.clicked_generate_idea = True

def resetAllParameters():
  time.sleep(EXPANDER_TRANSITION_TIME)
  st.session_state.param_expanded = True
  st.session_state.messages = []
  st.session_state.clicked_generate_idea = False

def resetConversation():
  initSession()
  resetAllParameters()

def initSession():
  if 'param_expanded' not in st.session_state:
      st.session_state.param_expanded = True
  if 'clicked_generate_idea' not in st.session_state:
      st.session_state.clicked_generate_idea = False

initSession()

with  st.expander("¿Cuál es la situación que querés abordar?", expanded=st.session_state.param_expanded):
  my_country = st.selectbox('¿En qué mercado estás?', ['Argentina','Peru','Chile'],index=None,on_change=buildMarketVariables,key="my_country")
  my_industry = st.selectbox('¿En qué industria?', ['Fintech','Seguros','Logistica'],index=None,key="my_industry")
  
  my_problem = st.text_area('Problema/Situación que te plantea el cliente',key="my_problem")
  
  my_market_variables = st.multiselect('Variables de mercado relevantes al problema', buildMarketVariables(),default=None,key="my_market_variables")

  my_kpis = st.multiselect('KPIs de negocio a mejorar', ['Gross Expense Ratio','Risk Premium','Expenses','Profit','Amount of Remuneration','Gross commission ratio'
    ,'Cancellation, Lapses, Non-Renewals, Replacement, Surrenders, Alterations','Withdrawal rates','Lapse rate','Cancellation Rate'
    ,'Rates of policies not taken up','Persistency ratio','Non-renewal ratio'
    ,'Renewal ratio','Replacement rates','Claims/loss ratio','Claims paid frequency','Claims declined','Claims paid' 
    ,'Claims outstanding rate','Fraud incidents'
    ,'Consumer complaints and disputes','Fraud'],default=None,key="my_kpis")
    
  my_consumer_trend = st.selectbox('Consumer trend que podría ser útil en una idea',['Beyond God','Triple impacto','Inteligencia Artificial avanza'
    ,'Complex disparity','Muscles as success','Extra payments','Jumping Stages','Lusty Food','Secret tourism'],index=None,key="my_consumer_trend")

  my_industry_trend = st.selectbox('Industry trend que podría ser útil en una idea',['Seguros embebidos','Digitalizacion y omnicanalidad','Hiperpersonalizacion'
    ,'IA Aplicada','Blockchain','Internet of Things'],index=None,key="my_industry_trend")
      
  st.button("Sugerime una idea",type="primary",on_click=generateAnswer)

if ("messages" not in st.session_state):
  st.session_state.messages = []

for message in st.session_state.messages:
  st.chat_message(message["role"]).write(message["content"])

if (st.session_state.clicked_generate_idea):
  if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    client = OpenAI(api_key=st.secrets["openai_key"])

    response = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

    st.button("Volvamos a empezar",type="secondary",on_click=resetConversation)
  


