from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from core.config import settings

template = PromptTemplate(
    input_variables=["variables"],
    template="Based on Today's date and all the other {variables}, tell the Horoscope of the person. Respond in such a way as if you are talking to a friend.",
)

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, api_key=settings.OPENAI_API_KEY)

