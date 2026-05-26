from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required,get_jwt_identity,get_jwt
from flask_jwt_extended import (
jwt_required,
get_jwt
)
def login():

    data = request.get_json()

    username = data["username"]
    password = data["password"]

    if username=="admin" and password=="admin123":

        token=create_access_token(
            identity="admin",
            additional_claims={
                "role":"Admin"
            }
        )

        return {
            "token":token,
            "role":"Admin"
        },200

    return {"message":"Invalid Credentials"},401


@jwt_required()
def protected():

    current_user=get_jwt_identity()

    claims=get_jwt()

    return {
        "message":"Protected Route Accessed",
        "user":current_user,
        "role":claims["role"]
    },200


@jwt_required()
def admin_panel():

    claims=get_jwt()

    if claims["role"]!="Admin":

        return{

        "message":
        "Access Denied"

        },403

    return{

    "message":
    "Welcome Admin"

    },200