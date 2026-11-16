from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from tools import scraped_data ,get_research
from langchain_core.output_parsers import StrOutputParser
import os
import requests
load_dotenv()



parser =StrOutputParser()

llm = ChatGroq(model="openai/gpt-oss-20b",temperature=0)

# 1st Agent

def get_research_agent():
    return create_agent(

        model=llm,
        tools=[get_research]
    )


# 2nd Agent
def get_scraped_agent():
    return create_agent(
        model =llm,
        tools=[scraped_data]
    )


writer_prompt = ChatPromptTemplate.from_messages([
   
    ("system", "You are an expert research writer. Write clear, structured and insightful reports based on the provided research."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional.""")
])

#Chain 1
writer_chain = writer_prompt | llm | parser

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
...""")
])

#Chain 2
crictic_chain = critic_prompt| llm | parser

