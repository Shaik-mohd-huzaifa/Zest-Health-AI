from .llm_service import LLM
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

llm_instance = LLM(token_limit=3)
llm = llm_instance.get_llm()

template = """
    You are a assisstant who predict the intent of the user query.
    
    These are the following intents you will be replying with 
    RAG, db, LLM
    
    Examples: 
    ("List out Doctor Aisha's Appointments", "db"),
    ("What doctor's are Available now", "db"),
    ("How many doctors does this hospital have?", "RAG"),
    ("When was this hospital established?", "RAG"),
    ("Patients waiting for Orthopedic consultation", "db"),
    ("Timing of Optician", "RAG"),
    ("What are the hospital timings?", "RAG"),
    ("Show me my profile", "RAG"),
    ("What are diabetes?", "LLM"),
    ("Why is CPR done?", "LLM"),
    ("What is the study of the heart called?", "LLM"),
    ("Who is the head of Cardiology?", "RAG"),
    ("What services are available at this hospital?", "RAG"),
    ("Are there any Pediatricians on duty now?", "db"),
    ("Where is the nearest pharmacy?", "RAG"),
    ("How many appointments are scheduled today?", "db"),
    ("Can I reschedule my appointment?", "db"),
    ("What are the visiting hours?", "RAG"),
    ("What is an MRI scan?", "LLM"),
    ("Can you tell me about flu symptoms?", "LLM"),
    ("Where can I park?", "RAG"),
    ("What should I do for chest pain?", "LLM"),
    ("Show me all appointments with Dr. Smith", "db"),
    ("Who are the on-call doctors for today?", "db"),
    ("What are the reviews of this hospital?", "RAG"),
    ("Is there a children’s ward?", "RAG"),
    ("Who can I contact for billing issues?", "RAG"),
    ("What are the Timings of Dr. Batra?", "RAG"),
    ("List today's appointments with Dr. Ray", "db"),
    ("What services does the Neurology department offer?", "RAG"),
    ("Show my recent activity log", "Auth_Profile"),
    ("Is Dr. Sarah available this evening?", "db"),
    ("Can I update my address?", "Auth_Profile"),
    ("How can I schedule a new appointment?", "db"),
    ("I want to view my medical history", "db"),
    ("Who are the available cardiologists?", "db"),
    ("I would like to book a follow-up with Dr. Kim", "db"),
    ("Are there any doctors specializing in dermatology?", "db"),
    ("Show the current waiting list for Dr. Ahmed", "db"),
    ("What treatments are offered for arthritis?", "LLM"),
    ("Explain the process of a CT scan", "LLM"),
    ("List all the doctors in Pediatrics", "RAG"),
    ("Tell me the hospital’s emergency contact number", "RAG"),
    ("Can I access my medical records?", "db"),
    ("What are the latest visiting hours?", "RAG"),
    ("When does the pharmacy close?", "RAG"),
    ("Are there any doctors on duty in the Oncology department?", "db"),
    ("Tell me about symptoms of high blood pressure", "LLM"),
    ("How can I create a family account?", "Auth"),
    ("I want to modify my appointment details", "db"),
    ("Who is on the Board of Directors?", "RAG"),
    ("List all appointments for this week", "db"),
    ("What do I do if I have a fever?", "LLM"),
    ("Show doctors with morning shifts", "db"),
    ("Are there doctors specializing in respiratory care?", "RAG"),
    ("Who can I reach out to for surgery inquiries?", "RAG"),
    ("What are symptoms of anxiety?", "LLM"),
    ("How do I sign up?", "Auth"),
    ("List all departments in this hospital", "RAG"),
    ("Show available slots with Dr. Patel", "db"),
    ("What should I bring to my appointment?", "LLM"),
    ("I want to view my prescription history", "db"),
    ("How many specialists are on staff?", "RAG"),
    ("What is a typical recovery time for knee surgery?", "LLM"),
    ("Where is the cardiology department located?", "RAG"),
    ("Who heads the oncology department?", "RAG"),
    ("What should I do if I lose my medical card?", "RAG"),
    ("Are there any on-call doctors now?", "db"),
    ("Tell me about diabetes management", "LLM"),
    ("List out the available doctors", "db"),
    
    Above are the examples but don't respond in the above format
    
    Response should be like this that's all nothing else:
    RAG Or db or LLM
    
    User Query: {Query}
"""

prompt = ChatPromptTemplate.from_template(template=template)

retriever = StrOutputParser()


def predictor(query):
    chain = prompt | llm | retriever

    return chain.invoke({"Query": query})


# print(predictor("List out the appointments of Dr Batra"))
