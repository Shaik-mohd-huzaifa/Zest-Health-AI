import { useEffect, useState } from "react"
import { getAppointments } from "../../utils/BlackBird/getAppointments"
import { UpdateActions } from "../../store/appointments/appointment.actions"

export const Appointments = () => {
    const [Appointments, setAppointments] = useState([])

    useEffect(() => {
        async function getAppoints(){
            const res = await getAppointments();
            UpdateActions(res.data)
            setAppointments(res.data)
            console.log(Appointments)
        }
        getAppoints()
    }, [])

    return (
        <div className="">
            {/* {
                Appointments ? Appointments.map(appointment => (<p key={appointment.id}>Appointment 11</p>)) : 'Appointment' 
            } */}
        </div>
    )
}