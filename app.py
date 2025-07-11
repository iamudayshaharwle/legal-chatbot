import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.memory import ConversationSummaryBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_chroma import Chroma

# Load environment variables
load_dotenv()

# Initialize Vectorstore
vectorstore = Chroma(
    persist_directory="Chromadb",
    embedding_function=GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )
)

# Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Create the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

# Define prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful chatbot. If the context is relevant, use it to improve your answer. "
        "Otherwise, answer the question from your own knowledge.\n\n{context}"
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])


# Create memory
memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=150,
    memory_key="history",
    return_messages=True
)

# Combine into chain
chain = prompt | llm

# --- STREAMLIT UI ---
st.set_page_config(page_title="LegalBot", page_icon="⚖️")

st.title("⚖️ AI-Powered Legal Advisor")
st.header("Ask your legal questions and get instant AI-powered answers.")

# Initialize session state to store history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Load memory variables (previous chat)
    memory_variables = memory.load_memory_variables({})
    chat_history = memory_variables.get("history", [])

    # Retrieve relevant docs
    try:
        docs = retriever.invoke(user_input)
        context_texts = "\n\n".join([doc.page_content for doc in docs])
    except Exception as e:
        st.error(f"Error during retrieval: {e}")
        context_texts = ""

    # Call the chain
    response = chain.invoke({
        "history": chat_history,
        "input": user_input,
        "context": context_texts
    })

    # Save to memory
    memory.save_context(
        {"input": user_input},
        {"output": response.content}
    )

    # Add to session state for display
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response.content))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "user":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)