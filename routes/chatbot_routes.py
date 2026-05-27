from flask import Blueprint,request,jsonify
from services.chatbot_service import ask_bot

chat_bp = Blueprint(
    'chat',
    __name__
)

@chat_bp.route(
    '/chat',
    methods=['POST']
)

def chatbot():

    data = request.json

    question = data.get(
        "message",
        ""
    )

    answer = ask_bot(
        question
    )

    return jsonify({

        "response":answer

    })