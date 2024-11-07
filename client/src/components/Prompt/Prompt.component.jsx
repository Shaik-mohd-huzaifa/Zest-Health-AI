import { AppointmentsList } from "../Appointments Widget/Appointments.widget";
import { DoctorWidget } from "../Doctors Widget/Doctors.widget";
import { IcuWidgetComponent } from "../ICU Widget/IcuWidget.component";
import "./Prompt.Styles.scss";

export const Prompt = ({ prompt, type }) => {
    console.log(prompt);

    const { response, tablename, res_type } = prompt?.prompt || {};

    return (
        <div className={`prompt ${type}`}>
            {prompt.type === "user" ? (
                <p>{prompt.prompt}</p>
            ) : (
                <>
                    {tablename === "appointments" && <AppointmentsList appointments={response} />}
                    {tablename === "doctors" && <DoctorWidget data={response} />}
                    {tablename === "icu" && <IcuWidgetComponent data={response} />}
                    {res_type === "normal" && <p>{response}</p>}
                </>
            )}
        </div>
    );
};
