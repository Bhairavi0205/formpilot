from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from rag.retriever import retrieve_context
from agent.prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3
    )

def chat_with_formpilot(user_message: str, lang: str = "English") -> str:
    try:
        context = retrieve_context(user_message)
        llm = get_llm()

        if lang == "Hindi":
            lang_instruction = """IMPORTANT: You MUST reply in Hindi only using Devanagari script. 
No English words at all. Pure Hindi answer dena."""
        else:
            lang_instruction = """IMPORTANT: You MUST reply in English only. 
No Hindi words at all. Pure English answer dena."""

        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                SYSTEM_PROMPT + "\n\n" + lang_instruction + "\n\nRelevant Information:\n{context}"
            ),
            HumanMessagePromptTemplate.from_template("{question}")
        ])

        chain = prompt | llm | StrOutputParser()
        response = chain.invoke({"context": context, "question": user_message})
        return response

    except Exception as e:
        return f"Something went wrong. Please try again!\nError: {str(e)}"