const Inital_State = {
    appointments: []
}

export const AppointmentReducer = (state = Inital_State, action) => {
    const {type, payload} = action

    if(type == '@update/appointments'){
        return {
            appointments: payload
        }
    }

    return state
}