import axios from "axios";

const endpoint = import.meta.env.VITE_BLACKBIRD_API_ENDPOINT; // Corrected environment variable access

export const getAppointments = async () => {
    try {
        // Use await to get the resolved response
        const res = await axios.get(endpoint + "/appointments"); 
        return res.data; // Return the actual data from the response
    } catch (error) {
        // Log and handle any errors that occur
        console.error("Error fetching appointments:", error);
        throw error; // Optionally, re-throw the error for further handling
    }
};
