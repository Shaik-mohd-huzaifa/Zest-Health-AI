import axios from "axios";

const endpoint = import.meta.env.VITE_BLACKBIRD_API_ENDPOINT;

export const getChatResponse = async (query) => {
    try {
        // Making a POST request to the endpoint with the query and intent
        const res = await axios.post(endpoint + "/chat", { query: query, intent: "RAG" });

        // Return the response from the API
        return res.data;
    } catch (error) {
        // Log any error that occurs during the request
        console.error("Error fetching chat response:", error);
        throw error;  // Optionally, re-throw the error for further handling
    }
};
