from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.write("##### 本アプリの概要: 筋トレとプログラミングの専門家に質問できるWebアプリ")
st.write("質問したい専門家の種類をラジオボタンで選択、入力フォームに質問を入力し、「実行」ボタンを押すことで、専門家からの回答を得ることができます。")
st.divider()

selected_item = st.radio(
    "AIが振る舞う専門家を選択してください",
    ["A：筋トレ", "B：プログラミング"]
)
input_message = st.text_input(label="選択した専門家に質問したい内容を入力してください", placeholder="例: 筋トレの効果的な方法は？")

def llm_response(input_text, selected_expert):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    if selected_expert == "A：筋トレ":
        system_message = "あなたは筋トレの専門家です。筋トレに関するアドバイスを提供してください"
    else:
        system_message = "あなたはプログラミングの専門家です。プログラミングに関するアドバイスを提供してください"
        
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]
    
    response = llm(messages)
    return response.content

if st.button("実行"):
    st.divider()

    if input_message == "":
        st.error("入力テキストを入力してください。")
    else:

      response_text = llm_response(input_message, selected_item)
      st.write("LLMからの回答:")
      st.write(response_text)
