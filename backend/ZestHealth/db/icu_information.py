icu_schema = """
    CREATE TABLE IF NOT EXISTS icu_information (
        icu_bed_id INT AUTO_INCREMENT PRIMARY KEY,
        allotted_date DATE NOT NULL,
        allotted_time TIME NOT NULL,
        retaining_date DATE NOT NULL,
        retaining_time TIME NOT NULL,
        patient_id INT NOT NULL,
        icu_bed_number VARCHAR(50) NOT NULL,
        patient_health_details JSON
    );
"""
