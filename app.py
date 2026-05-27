from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
from utils.error_handler import handle_error
import os

from routes.report_routes import report_bp
from routes.email_routes import email_bp
from config.mail_config import mail
from routes.chatbot_routes import chat_bp
from routes.sla_routes import sla_bp
from routes.otif_routes import otif_bp
from routes.mobile_routes import mobile_bp
from routes.predictions_routes import prediction_bp
from routes.weather_routes import weather_bp
from routes.live_routes import live_bp


load_dotenv()

app=Flask(__name__)


app.config["MAIL_SERVER"]=os.getenv(
    "MAIL_SERVER",
    "smtp.gmail.com"
)

app.config["MAIL_PORT"]=int(
    os.getenv(
        "MAIL_PORT",
        587
    )
)

app.config["MAIL_USE_TLS"]=(
    os.getenv(
        "MAIL_USE_TLS",
        "True"
    )=="True"
)

app.config["MAIL_USERNAME"]=os.getenv(
    "MAIL_USERNAME",
    ""
)

app.config["MAIL_PASSWORD"]=os.getenv(
    "MAIL_PASSWORD",
    ""
)

mail.init_app(app)


app.config["JWT_SECRET_KEY"]=os.getenv(
    "JWT_SECRET_KEY",
    "SmartLogisticsSecret"
)

jwt=JWTManager(app)


app.register_blueprint(auth_bp)
app.register_blueprint(report_bp)
app.register_blueprint(email_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(sla_bp)
app.register_blueprint(otif_bp)
app.register_blueprint(mobile_bp)
app.register_blueprint(prediction_bp)
app.register_blueprint(weather_bp)
app.register_blueprint(live_bp)


app.register_error_handler(
    Exception,
    handle_error
)


@app.route('/')

def home():

    return {

        "message":
        "Smart Logistics API Running"

    }



if __name__=="__main__":

    app.run(

        host="0.0.0.0",

        port=int(
            os.getenv(
                "PORT",
                5000
            )
        ),

        debug=True

    )