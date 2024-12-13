import os
import pandas as pd
import streamlit as st
from typing import List
from together import Together
from dotenv import load_dotenv

# define the model and temperature
model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
temperature=0.0

# get the api key from the environment variables or from the streamlit secrets file
def get_api_key(key_name):
    load_dotenv()
    if isinstance(key_name, list):
        keys = {}
        for key in key_name:
            api_key = os.getenv(key)
            if api_key:
                keys[key] = api_key
            else:
                keys[key] = st.secrets[key]
        return keys
    elif isinstance(key_name, str):
        api_key = os.getenv(key_name)
        if api_key:
            return api_key
        else:
            return st.secrets[key_name]

# Initialize the Together.ai LLM API
def initialize_llm():
    # Replace with your actual Together.ai API key
    api_key = get_api_key("TOGETHER_API_KEY")
    return Together(api_key=api_key)

# Extract important skills from the job description
def extract_skills(llm, job_description):
    prompt = f"Extract the key skills from the following job description,make each skill 1-3 words, focus more on hard skills over soft skills:\n\n{job_description} --- Return only the skills separated by commas and nothing else."
    response = llm.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content

# Generate a table of skills in 2-3 columns
def format_skills_table(skills: List[str]) -> str:
    num_columns = 2 if len(skills) % 2 == 0 else 3
    rows = [skills[i:i+num_columns] for i in range(0, len(skills), num_columns)]
    # Ensure all rows have the same number of columns
    for row in rows:
        while len(row) < num_columns:
            row.append("")
    table = pd.DataFrame(rows, columns=[f"Column {i+1}" for i in range(num_columns)])
    return table.to_html(index=False, escape=False)

# Update resume template with skills in bullets
def update_resume(llm, skills: List[str], resume_template: str) -> str:
    prompt = (
        "Match the following skills to the relevant bullets in the resume and insert the skill as the first item in each bullet point. "
        "Each skill should only match one bullet. Return the updated resume:\n\n"
        f"Skills:\n{', '.join(skills)}\n\nResume Template:\n{resume_template}"
    )
    response = llm.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content

# Grade hallucinations and ensure consistency
def hallucinations_grader(llm, job_description: str, resume_template: str, updated_resume: str) -> str:
    prompt = (
        "Review the following job description, resume template, and updated resume template. Ensure that the skills list in the updated resume template is grounded in truth from the job description, "
        "and that the updated resume remains consistent with the original resume template. Highlight any discrepancies and return the validated updated resume:\n\n"
        f"Job Description:\n{job_description}\n\nResume Template:\n{resume_template}\n\nUpdated Resume Template:\n{updated_resume}"
    )
    response = llm.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content

# Streamlit app
st.title("📝 Job Skills Matcher")

llm = initialize_llm()

# Inputs
job_description = st.text_area("✅Enter Job Description", "")
resume_template = st.text_area("✏️Enter Resume Template", "")

if st.button("Generate Skills and Updated Resume"):
    if not job_description or not resume_template:
        st.warning("Please provide both a job description and a resume template.")
    else:
        with st.spinner("Processing..."):
            skills = extract_skills(llm, job_description)
            skills_list = skills.split(", ")  # Convert skills string to list
            skills_table = format_skills_table(skills_list)
            updated_resume = update_resume(llm, skills_list, resume_template)
            validated_resume = hallucinations_grader(llm, job_description, resume_template, updated_resume)

        st.subheader("Extracted Skills")
        st.markdown(skills_table, unsafe_allow_html=True)

        st.subheader("Updated Resume Template")
        st.markdown(updated_resume, unsafe_allow_html=True)

        st.subheader("Validated Updated Resume Template")
        st.text_area("Validated Updated Resume", validated_resume, height=300)

st.caption("Powered by Together.ai")
