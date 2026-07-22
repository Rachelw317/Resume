from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from llm_config import get_llm

load_dotenv()


class ConceptExplanation(BaseModel):
    concept: str = Field(..., description="要解释的概念")
    explanation: str = Field(..., description="概念的解释")
    summary: str = Field(..., description="概念的总结")


structured_llm = get_llm().with_structured_output(ConceptExplanation)

prompt = ChatPromptTemplate.from_messages([
    ("human", "LangChain 里的 {concept} 是什么？"),
])

chain = prompt | structured_llm

concept_list = [
    {"concept": "Chain"},
    {"concept": "PromptTemplate"},
    {"concept": "LLM"},
]

for item in concept_list:
    result = chain.invoke(item)
    print(f"问题: {item['concept']}\n回答: {result.model_dump()}\n")