doctor_table_schema = """
    CREATE TABLE IF NOT EXISTS doctors (
        doctor_id INT AUTO_INCREMENT PRIMARY KEY,
        appointment_date DATE NOT NULL,
        appointment_time TIME NOT NULL,
        doctor_name VARCHAR(100) NOT NULL,
        doctor_age INT NOT NULL,
        doctor_department VARCHAR(3) NOT NULL, 
        doctor_details JSON
    );
    """
