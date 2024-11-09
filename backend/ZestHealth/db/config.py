import os
import pymysql.cursors
from dotenv import load_dotenv

# from .icu_information import icu_schema

load_dotenv()

ENDPOINT = os.getenv("AWS_RDS_ENDPOINT")
USER = os.getenv("AWS_RDS_USER")
PASSWORD = os.getenv("AWS_RDS_PASSWORD")
DATABASE = os.getenv("AWS_RDS_DATABASE")
PORT = 3306

connection = pymysql.connect(
    host=ENDPOINT,
    user=USER,
    password=PASSWORD,
    database=DATABASE,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

try:
    connection = pymysql.connect(
        host=ENDPOINT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

    print("Connection Established")

    cursor = connection.cursor()

    # Define the SQL statement for creating a table

    # Execute the query
    cursor.execute(
        """
        INSERT INTO appointments (appointment_date, appointment_time, patient_name, patient_age, patient_blood_group, consulting_department, consulting_type, appointment_type, documents) VALUES
('2024-11-01', '09:30:00', 'Alice Johnson', 34, 'O+', 'Cardiology', 'Follow-up on heart condition', 'revisit', JSON_OBJECT(
    'previous_reports', 'Echocardiogram, ECG from last visit',
    'medications', 'Beta blockers, ACE inhibitors'
)),
('2024-11-01', '10:15:00', 'Michael Green', 28, 'A-', 'Dermatology', 'Skin rash diagnosis', 'fresh', JSON_OBJECT(
    'symptoms', 'Redness, itching',
    'prior_treatment', 'Over-the-counter creams'
)),
('2024-11-02', '11:00:00', 'Samantha Lee', 45, 'B+', 'Orthopedics', 'Back pain assessment', 'fresh', JSON_OBJECT(
    'pain_duration', '2 weeks',
    'previous_injuries', 'None'
)),
('2024-11-02', '13:45:00', 'Daniel Kim', 55, 'AB+', 'Cardiology', 'Routine heart check-up', 'revisit', JSON_OBJECT(
    'last_visit', '2024-05-10',
    'notes', 'Maintaining stable condition'
)),
('2024-11-03', '09:00:00', 'Nancy Wilson', 63, 'O-', 'Radiology', 'MRI for suspected fracture', 'fresh', JSON_OBJECT(
    'injury_details', 'Fall from stairs',
    'allergies', 'None'
)),
('2024-11-03', '14:30:00', 'Oliver Brown', 5, 'A+', 'Pediatrics', 'Routine pediatric check-up', 'fresh', JSON_OBJECT(
    'vaccinations', 'Up to date',
    'growth_parameters', 'Normal'
)),
('2024-11-04', '10:30:00', 'Emma Taylor', 29, 'B-', 'Dermatology', 'Acne treatment', 'revisit', JSON_OBJECT(
    'previous_medications', 'Topical retinoids',
    'allergies', 'None'
)),
('2024-11-04', '12:00:00', 'Henry Scott', 40, 'A+', 'Orthopedics', 'Knee pain evaluation', 'fresh', JSON_OBJECT(
    'pain_duration', '3 months',
    'physical_activity', 'Jogging, light weightlifting'
)),
('2024-11-05', '09:15:00', 'Sophia Lewis', 50, 'O-', 'Cardiology', 'Hypertension follow-up', 'revisit', JSON_OBJECT(
    'medications', 'ACE inhibitors, statins',
    'exercise_regimen', 'Walking 30 minutes daily'
)),
('2024-11-05', '11:45:00', 'James Anderson', 72, 'AB-', 'Radiology', 'CT scan for chest pain', 'fresh', JSON_OBJECT(
    'symptoms', 'Shortness of breath, chest discomfort',
    'family_history', 'Heart disease'
));

        """
    )
    data = cursor.fetchmany()

    print(data)

    # Commit the transaction
    connection.commit()

except pymysql.MySQLError as e:
    print(e)
# finally:

#     if connection:
#         connection.close()
#         print("Connection Closed")
