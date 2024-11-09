import re
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from .llm_service import LLM
from ..db.config import connection
from datetime import datetime

# Get the current date
current_date = datetime.now()
# Format to YYYY-MM-DD
formatted_date = current_date.strftime("%Y-%m-%d")


template = """
    You are a MySQL Query Generator that produces MySQL queries based on user parameters. You will be provided with the schema containing table details, and you will only generate queries for these specified tables. Do not generate table creation, deletion, or modification queries. Your response should contain only one MySQL query in plain text format based on the user query provided—no additional text, descriptions, explanations, or code formatting. The response should be a single line in plain text without any special characters or quotes around the query.
    Do not generate any joins or anyother queries just simple once 
    
**Example of Expected Output:**
- Correct: `SELECT * FROM appointments WHERE consulting_department = 'Cardiology';`
- Incorrect: `'SELECT * FROM appointments WHERE consulting_department = 'Cardiology';'`
- Incorrect: ``` `SELECT * FROM appointments WHERE consulting_department = 'Cardiology';` ```
  
Schema:

- **Appointments**:
  - Table name: `appointments`
  - Columns:
    - `appointment_id INT AUTO_INCREMENT PRIMARY KEY`
    - `appointment_date DATE NOT NULL`
    - `appointment_time TIME NOT NULL`
    - `patient_name VARCHAR(100) NOT NULL`
    - `patient_age INT NOT NULL`
    - `patient_blood_group VARCHAR(3) NOT NULL`
    - `consulting_department VARCHAR(50) NOT NULL`
    - `consulting_type VARCHAR(50) NOT NULL`
    - `appointment_type ENUM('fresh', 'revisit') NOT NULL`
    - `documents JSON`

- **Doctors**:
  - Table name: `doctors`
  - Columns:
    - `doctor_id INT AUTO_INCREMENT PRIMARY KEY`
    - `timings VARCHAR(100) NOT NULL`
    - `availability ENUM('Available', 'Not Available') NOT NULL`
    - `doctor_name VARCHAR(100) NOT NULL`
    - `doctor_age INT NOT NULL`
    - `doctor_department VARCHAR(100) NOT NULL`
    - `doctor_details JSON`
    
    These are the department Names so mention correctly 
    Cardiology
    Dermatology
    Orthopedics
    Pediatrics
    Neurology
    General Practice
    Gynecology
    Radiology
    Otolaryngology
    Oncology
    

- **ICU Information**:
  - Table name: `icu_information`
  - Columns:
    - `icu_bed_id INT AUTO_INCREMENT PRIMARY KEY`
    - `allotted_date DATE NOT NULL`
    - `allotted_time TIME NOT NULL`
    - `retaining_date DATE NOT NULL`
    - `retaining_time TIME NOT NULL`
    - `patient_id INT NOT NULL`
    - `icu_bed_number VARCHAR(50) NOT NULL`
    - `patient_health_details JSON`
    
    The icu bed numbers start from ICU-001 and End ICU-020

Today's date {current_date} if any query needs it 
User Query: `{Query}`
"""


prompt = ChatPromptTemplate.from_template(template=template)

output_retreiver = StrOutputParser()


def data_fetching(query):
    cursor = connection.cursor()

    table_name_match = re.search(r"FROM\s+(\w+)", query, re.IGNORECASE)
    table_name = table_name_match.group(1) if table_name_match else "Unknown"

    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data, table_name


def db_data_retriever(query):
    llm_instance = LLM(token_limit=30)
    llm = llm_instance.get_llm()

    chain = prompt | llm | output_retreiver

    response = chain.invoke({"Query": query, "current_date": formatted_date})
    print(response)
    data = data_fetching(response)

    return data
