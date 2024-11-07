import React from "react";
import "./Doctors.styles.scss";

export const DoctorWidget = ({ data = [] }) => {
    const doctorsToShow = data.slice(0, 3);

    return (
        <div className="doctor-widget-container">
            <h2 className="doctor-widget-header">Doctor Widget</h2>
            <div className="doctor-list">
                {doctorsToShow.map((doctor, index) => (
                    <div className="doctor-card" key={index}>
                        <div className="doctor-name">{doctor.doctor_name}</div>
                        <div className="doctor-department">
                            <span className="label">Department:</span> {doctor.doctor_department}
                        </div>
                        <div className="doctor-age">
                            <span className="label">Age:</span> {doctor.doctor_age}
                        </div>
                        <div className="doctor-availability">
                            <span className="label">Availability:</span> {doctor.availability}
                        </div>
                        <div className="doctor-timings">
                            <span className="label">Timings:</span> {doctor.timings}
                        </div>
                        <div className="doctor-details">
                            <h4>Details:</h4>
                            <p>{doctor.doctor_details.expertise}</p>
                            <p>{doctor.doctor_details.experience}</p>
                            <p>{doctor.doctor_details.achievements}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};
