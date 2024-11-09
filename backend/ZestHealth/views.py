from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ZestHealth.Services.predication import prediction
from ZestHealth.Services.db_tool import db_data_retriever
from ZestHealth.Services.plain_llm import plain_llm
from ZestHealth.Services.llm_and_rag import data_from_rag
from ZestHealth.Services.predictor import predictor
import json


@csrf_exempt
def ask(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        prompt = data.get("user_input")

        # intent = prediction(prompt)
        intent = predictor(prompt)
        print(intent)

        if intent[:3] == "LLM":
            
            response = plain_llm(prompt)
            return JsonResponse({"response": response, "res_type": "normal"})
        elif intent[:2] == "db":
            data, table_name = db_data_retriever(prompt)
            return JsonResponse(
                {"response": data, "res_type": "db", "tablename": table_name}
            )
        elif intent[:3] == "RAG":
            response = data_from_rag(prompt)
            return JsonResponse({"response": response, "res_type": "normal"})
