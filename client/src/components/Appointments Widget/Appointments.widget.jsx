import "./Appointments.styles.scss";

export const AppointmentsList = ({ appointments }) => {
    return (
        <div className="appointments-list">
            {appointments.map((appointment) => (
                <AppointmentWidget key={appointment.appointment_id} appointment={appointment} />
            ))}
        </div>
    );
};

const AppointmentWidget = ({ appointment }) => {
    const {
        appointment_date,
        appointment_id,
        appointment_time,
        appointment_type,
        consulting_department,
        consulting_type,
        doctor_name,
        documents,
        patient_age,
        patient_blood_group,
        patient_name,
    } = appointment;

    const parsedDocuments = JSON.parse(documents || "{}");

    return (
        <div className="appointment-widget">
            <h2 className="appointment-widget__header">Appointment ID: {appointment_id}</h2>
            <div className="appointment-widget__content">
                <div className="appointment-widget__row">
                    <span className="label">Patient Name:</span> {patient_name}
                </div>
                <div className="appointment-widget__row">
                    <span className="label">Age:</span> {patient_age}
                </div>
                <div className="appointment-widget__row">
                    <span className="label">Blood Group:</span> {patient_blood_group}
                </div>
                <div className="appointment-widget__row">
                    <span className="label">Date:</span> {appointment_date}
                </div>
                <div className="appointment-widget__row">
                    <span className="label">Time:</span> {appointment_time}
                </div>
                <div className="appointment-widget__row">
                    <span className="label">Type:</span> {appointment_type}
                </div>
                <div className="appointment-widget__row">
                    <span className="label">Department:</span> {consulting_department}
                </div>
                <div className="appointment-widget__row">
                    <span className="label">Consulting Type:</span> {consulting_type}
                </div>
                <div className="appointment-widget__row">
                    <span className="label">Doctor:</span> {doctor_name || "Not Assigned"}
                </div>
                <div className="appointment-widget__documents">
                    <h3 className="appointment-widget__documents-header">Documents:</h3>
                    {Object.entries(parsedDocuments).map(([key, value]) => (
                        <div key={key} className="appointment-widget__document">
                            <span className="label">{key}:</span> {value}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};
