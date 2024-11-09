from ZestHealth.Services.llm_service import LLM

appointments_schema = """
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INT AUTO_INCREMENT PRIMARY KEY,
        appointment_date DATE NOT NULL,
        appointment_time TIME NOT NULL,
        patient_name VARCHAR(100) NOT NULL,
        patient_age INT NOT NULL,
        patient_blood_group VARCHAR(3) NOT NULL,
        consulting_department VARCHAR(50) NOT NULL,
        consulting_type VARCHAR(50) NOT NULL,
        appointment_type ENUM('fresh', 'revisit') NOT NULL,
        documents JSON
    );
    """
