
# Job Skills Matcher Streamlit App

## Overview
The Job Skills Matcher is a Streamlit-based application that leverages Together.ai’s language model to assist job seekers in tailoring their resumes for specific job descriptions. The app extracts essential hard skills from a given job description, matches them to a provided resume template, and outputs an updated, optimized resume.

## Features
- **Extract Key Skills**: Automatically identify the most important hard skills from a job description.
- **Skill Table Generation**: Display the extracted skills in a formatted table with 2-3 columns.
- **Resume Optimization**: Match extracted skills to relevant resume bullet points and update the resume template.
- **Validation and Grading**: Ensure the updated resume is grounded in the job description and consistent with the original resume template.

## Business Value
- Streamlines the process of tailoring resumes to job descriptions.
- Enhances job seekers' chances of landing interviews by focusing on relevant hard skills.
- Saves time by automating resume customization.

## Setup and Installation

### Prerequisites
- Python 3.9 or later
- Together.ai API key

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/job-skills-matcher.git
   cd job-skills-matcher
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your Together.ai API key as an environment variable:
   ```bash
   export TOGETHER_API_KEY="your_api_key"
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run streamlit_resume_app.py
   ```

5. Open the app in your browser at `http://localhost:8501`.

## How It Works

### Workflow
1. Enter a **job description** and a **resume template** into the text areas.
2. Click the **"Generate Skills and Updated Resume"** button.
3. The app will:
   - Extract key skills from the job description.
   - Format the skills into a table.
   - Match the skills to the resume bullet points and update the resume.
   - Validate the updated resume for accuracy and consistency.
4. View the extracted skills and the validated updated resume.

### Key Modules
- **`streamlit`**: For creating the web interface.
- **`together`**: For integrating the Together.ai LLM API.
- **`pandas`**: For formatting the skills into a table.

## Example
### Input:
- **Job Description**:
  *"Looking for a data scientist with expertise in Python, machine learning, and data visualization tools."*
- **Resume Template**:
  A resume template with various bullet points.

### Output:
- **Extracted Skills**: Python, Machine Learning, Data Visualization
- **Updated Resume**: Each skill is matched to a relevant bullet point.

## Future Enhancements
1. **Improved Matching Algorithms**:
   - Incorporate machine learning to enhance skill-to-bullet matching.
   - Business Value: Increased precision in matching skills to resume content.

2. **Support for Multiple Job Descriptions**:
   - Allow comparison and merging of skills from multiple job descriptions.
   - Business Value: Tailor resumes for multiple positions simultaneously.

3. **Integration with Job Portals**:
   - Directly fetch job descriptions from popular job boards.
   - Business Value: Saves users time and simplifies the input process.

4. **Multilingual Support**:
   - Expand the app to support non-English job descriptions and resumes.
   - Business Value: Broader accessibility for international users.

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- **Together.ai** for their powerful LLM API.
- **Streamlit** for providing an easy-to-use platform for deploying data apps.

---

For any issues or feature requests, please create an issue in this repository or reach out to the maintainer.