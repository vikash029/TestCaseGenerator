# TestCaseGenerator
ML-based Test Case Generator: Automatically generates functional, boundary, and negative test cases from requirement documents using Python and Streamlit.

# ML-based Test Case Generator

Automatically generate QA test cases from requirement documents using **classical ML** and **Streamlit**. This tool classifies requirements into **functional**, **boundary**, and **negative** types and produces structured test cases in JSON format.

## Features
- Upload `.docx` or `.txt` requirement files.
- Predict test case type using ML (functional, boundary, negative).
- Automatically generate structured test cases with unique IDs.
- Preview generated test cases in the UI.
- Download test cases in JSON format for QA use.

## Installation

1. Clone the repository:

git clone https://github.com/vikash029/TestCaseGenerator.git
cd TestCaseGenerator
Install dependencies:

pip install -r requirements.txt
Usage
Run the Streamlit app:


streamlit run test_case_generator.py
Upload your requirement document (.docx or .txt).

The app will classify requirements into test case types.

Generated test cases will be displayed in the UI.

Download the JSON file of structured test cases.

Sample Output

[
  {
    "id": "TC001",
    "type": "functional",
    "requirement": "User should be able to register with valid name, email, and password",
    "input": "Valid name, email, password",
    "expected_output": "User account created successfully"
  },
  {
    "id": "TC002",
    "type": "boundary",
    "requirement": "Password must be at least 8 characters",
    "input": "Password with minimum 8 characters",
    "expected_output": "Password accepted"
  }
]

Folder Structure

TestCaseGenerator/
│
├─ test_case_generator.py      # Streamlit + ML script
├─ requirements.txt            # Sample requirement texts (optional)
├─ README.md                   # Project description
├─ .gitignore                  # Files to ignore
└─ data/                       # Optional folder for datasets
    └─ requirements.docx
Dependencies
Python 3.8+

pandas

scikit-learn

streamlit

python-docx

Install all dependencies using:

pip install -r requirements.txt
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

License
This project is licensed under the MIT License.


---

If you want, I can **also generate a ready-to-push GitHub folder** with:  

- `test_case_generator.py` (Streamlit + ML)  
- `requirements.txt`  
- Sample `.docx` file  
- `.gitignore`  
- This `README.md`  


