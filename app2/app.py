import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd
import os

load_dotenv()
# Configuración de la página
st.set_page_config(page_title="AI Product", page_icon=":sparkles:")
st.title("AI Product")

def get_response(user_query, chat_history):
    df = pd.read_csv("")

    agent = create_pandas_dataframe_agent(OpenAI(temperature=0),
                                        df,
                                        allow_dangerous_code=True,
                                        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,)
    
    result = agent.invoke(user_query)

    template = """
    Aqui escribimos el template de la conversación

    Chat history: {chat_history}

    Pregunta: {user_query}

    Respuesta: {result}

    Humaniza la respuesta con base en la última pregunta.
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI(
        model = "gpt-3.5-turbo",
    )
        
    chain = prompt | llm | StrOutputParser()
    
    return chain.stream({
        "chat_history": chat_history,
        "user_query": user_query,
        "result": result["output"],
    })

    

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hola soy un chatbot, ¿Cómo puedo ayudarte?"),
    ]

# Conversation history
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# User input
user_query = st.chat_input("Escribe tu mensaje aqui...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = st.write_stream(get_response(user_query, st.session_state.chat_history))

    st.session_state.chat_history.append(AIMessage(content=response))
