import { combineReducers } from "redux";
import { promptReducer } from "./prompt/prompt.reducer";
import { AppointmentReducer } from "./appointments/appointment.reducer";


export const RootReducer = combineReducers({
    Prompts: promptReducer,
    Appointments: AppointmentReducer
})