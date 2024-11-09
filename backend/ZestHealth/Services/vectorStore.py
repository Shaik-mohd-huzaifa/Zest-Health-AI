import os
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = "2024-02-01"


embedding_model = AzureOpenAIEmbeddings(
    api_key=AZURE_OPENAI_API_KEY,
    model="text-embedding-3-small",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)
# Define document chunks with text and metadata
document_strings = [
    "Hospital Overview: City Central Hospital is a state-of-the-art healthcare facility located in the heart of downtown. The hospital provides a wide range of medical services, from emergency care to specialized surgeries. With modern equipment and highly qualified staff, City Central Hospital is committed to providing excellent healthcare services to the community.",
    "Timings: The hospital operates 24/7. Outpatient services are available Monday to Friday from 8:00 AM to 8:00 PM. Emergency services are available at all times, with specialized staff on-call during night hours.",
    "Doctor Details - Dr. Samantha Ray, Cardiology: Dr. Ray specializes in cardiovascular treatments and has over 15 years of experience. She is available for consultations Monday, Wednesday, and Friday from 10:00 AM to 4:00 PM. Current waitlist includes 5 patients.",
    "Doctor Details - Dr. Alan Chen, Neurology: Dr. Chen has expertise in treating neurological disorders and has been part of City Central for 10 years. Consultation hours are Tuesday and Thursday from 9:00 AM to 3:00 PM. Current waitlist includes 8 patients.",
    "Doctor Details - Dr. Emily Carter, Pediatrics: Dr. Carter is a specialist in pediatric care with a focus on childhood diseases. Available Monday to Friday from 8:00 AM to 12:00 PM. Current waitlist includes 3 patients.",
    "Amenities: The hospital provides free Wi-Fi, a cafeteria, pharmacy services, and a 24/7 ATM. There is also a children’s play area and family waiting rooms to ensure comfort during longer waiting periods.",
    "Contact Information: City Central Hospital, 123 Main St., Downtown. Phone: (555) 123-4567. Email: contact@citycentralhospital.com. For emergencies, dial (555) 999-9111.",
]


# Initialize the DocArrayInMemorySearch vector store
vector_store = DocArrayInMemorySearch.from_texts(
    texts=document_strings, embedding=embedding_model
)


vector_retriever = vector_store.as_retriever()
