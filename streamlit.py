import os
from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
input_variables=["degree", "year", "topics", "duration", "goal"],
template="""You are an AI that generates structured learning roadmaps.

## User Details:
- Degree: {degree}
- Year of Study: {year}
- topics covered: {topics}

- Duration: {duration} weeks
- Goal: {goal}

## Instructions:
0. generate a list of topics to be covered next on the basis of the topics already covered
1. Generate a week-by-week study roadmap depicting the topics to be covered after the {topics}.
2. Recommend study materials and learning resources (books, courses, YouTube, official docs).
3. Include hands-on projects and exercises.
4. Add revision and assessments.
5. Ensure the roadmap is practical and beginner-friendly 

Return the roadmap in a structured format:
### Week 1:
- Topic to study: XYZ
- Learning Resources: A, B, C
- Practice: Exercise 1
- Mini Project: ABC

### Week 2:
...
"""
)

st.title("Personalized Learning Roadmap Generator")
degree = st.text_input("Degree (e.g., B.Tech CSE, BSc Maths)")
year = st.selectbox("Year of Study", ["1st", "2nd", "3rd", "4th"])
topics = st.text_area("Topics Already Covered (comma-separated)")
duration = st.slider("Duration (weeks)", min_value=1, max_value=12, value=4)
goal = st.text_area("Learning Goal (optional)")

llm = OllamaLLM(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if st.button("Generate Roadmap"):
    input_data = {
        "degree": degree if degree else "Not specified",
        "year": year if year else "Not specified",
        "topics": topics if topics else "None",
        "duration": duration,
        "goal": goal if goal else "Not specified"
    }

    response = chain.invoke(input_data)

    st.subheader("Generated Learning Roadmap:")
    st.write(response)




