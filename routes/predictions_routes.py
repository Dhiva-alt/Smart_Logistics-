from flask import Blueprint, jsonify
import pandas as pd

prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route('/predictions', methods=['GET'])
def get_predictions():

    df = pd.read_csv("prediction_results.csv")

    data = df.to_dict(orient='records')

    return jsonify(data)