from flask import jsonify

def handle_error(e):

    return jsonify({

        "status":"error",

        "message":str(e)

    }),500