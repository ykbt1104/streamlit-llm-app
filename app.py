from dotenv import load_dotenv

load_dotenv()

import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# APIキーの取得
api_key = os.getenv("OPENAI_API_KEY")

# LangChain LLMインスタンスを作成
llm = ChatOpenAI()

# 専門家の種類を定義
experts = {
    "AIエンジニア": "あなたは優秀なAIエンジニアです。技術的な助言をしてください。",
    "経営コンサルタント": "あなたは経験豊富な経営コンサルタントです。経営のアドバイスをしてください。"
    # 必要に応じて追加OK
}

# StreamlitのUI
st.title("LLM Expert App")
st.write("このアプリは、専門家の立場でChatGPTが質問に答えます。下記で専門家を選び、質問を入力してください。")

expert_choice = st.radio("専門家を選択してください", list(experts.keys()))
user_input = st.text_input("質問を入力してください")

def ask_llm(user_input, expert_role):
    system_msg = SystemMessage(content=experts[expert_role])
    human_msg = HumanMessage(content=user_input)
    response = llm([system_msg, human_msg])
    return response.content

if st.button("送信") and user_input:
    answer = ask_llm(user_input, expert_choice)
    st.markdown("#### 回答")
    st.write(answer)

