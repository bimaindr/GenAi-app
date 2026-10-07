import os
import streamlit as st
from langchain_community.tools import DuckDuckGoSearchResults, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

# -----------------------------------------------------------------------------
# 1. Konfigurasi API Key (Menggunakan os.getenv agar aman tanpa secrets.toml)
# -----------------------------------------------------------------------------
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# -----------------------------------------------------------------------------
# 2. Inisialisasi LLM & Tools (Dioptimasi agar Cepat & Hemat Token)
# -----------------------------------------------------------------------------
# Temperature rendah (0.1) & timeout 15 detik untuk mencegah hang
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash", 
    temperature=0.1,
    request_timeout=15
)

# Batasi output pencarian agar tidak membebani konteks LLM
search = DuckDuckGoSearchResults(max_results=2)
wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
)
tools = [search, wikipedia]

# -----------------------------------------------------------------------------
# 3. Buat ReAct Agent (LangGraph Architecture)
# -----------------------------------------------------------------------------
system_prompt = (
    "You are a helpful and concise assistant. Use tools ONLY when necessary. "
    "Make at most 1-2 tool calls. Answer directly and concisely."
)

agent_executor = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)

# -----------------------------------------------------------------------------
# 4. Pengelolaan Memori (Menggunakan Streamlit Session State agar Awet)
# -----------------------------------------------------------------------------
if "store" not in st.session_state:
    st.session_state.store = {}

def get_session_history(session_id: str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = InMemoryChatMessageHistory()
    return st.session_state.store[session_id]

agent_with_history = RunnableWithMessageHistory(
    agent_executor,
    get_session_history,
    input_messages_key="messages",
    history_messages_key="history",
)

# -----------------------------------------------------------------------------
# 5. Antarmuka Pengguna (Streamlit UI)
# -----------------------------------------------------------------------------
st.title("Fast Agentic RAG (Gemini Flash)")

# Tampilkan riwayat obrolan di layar
if "messages_ui" not in st.session_state:
    st.session_state.messages_ui = []

for msg in st.session_state.messages_ui:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input pertanyaan dari user
if question := st.chat_input(
    "Tanyakan sesuatu...",
    key="main_chat_input"
):
    # Simpan dan tampilkan pesan user
    st.session_state.messages_ui.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Eksekusi agent
    with st.chat_message("assistant"):
        with st.spinner("Mencari informasi..."):
            config = {"configurable": {"session_id": "sess1"}}
            
            result = agent_with_history.invoke(
                {"messages": [("user", question)]}, 
                config=config
            )
            
            # Deteksi pemanggilan Tool
            messages = result["messages"]
            tools_used = []
            for m in messages:
                if hasattr(m, "tool_calls") and m.tool_calls:
                    for call in m.tool_calls:
                        tools_used.append(call["name"])
            
            if tools_used:
                st.caption(f"*Sumber Tool:* `{', '.join(set(tools_used))}`")

            # Parsing output agar tidak berbentuk JSON/List
            last_content = result["messages"][-1].content
            if isinstance(last_content, list):
                answer = "".join([b.get("text", "") for b in last_content if isinstance(b, dict)])
            else:
                answer = str(last_content)

            st.markdown(answer)
            st.session_state.messages_ui.append({"role": "assistant", "content": answer})