# File: main.py
# Author: Arvid Möller
# Date: 2025-05-08
# Description: The main file for the backend, uses FlaskAPI to take input from the NEXT.js front-end and then calls the main() function in the predict.py file. 
# Required files: model[number].pkl, modelInfo[number].pkl, predict.py
# Required modules: Flask, Flask CORS, pickle, pandas

from flask import Flask, request, jsonify     # type: ignore
from flask_cors import CORS     # type: ignore
import pandas as pd     # type: ignore
import predict
import pickle

app = Flask(__name__)
CORS(app)

# Load model and model info
model = pickle.load(open("models/model2.pkl", "rb"))
le_dict = pickle.load(open("models/modelInfo2.pkl", "rb"))

col_arr = ["supplier", "amount", "department", "cost_center", "project_id", "personnel", "reference", "tax_percentage", "city", "created_at", "Test_category"] 


# This function contains the API for the submit button in the NEXT.js front-end and then calls the main() function in the predict.py file to make a prediction. 
#
# Paramiters: void
#
# Return: The prediction as JSON.
@app.route("/submit", methods=['POST'])
def submit():
    data = {}

    for i in col_arr:
        if i in ["tax_percentage", "amount"]:
            try:
                data[i] = float(request.form.get(i, ""))
            except:
                data[i] = 0.0
        else:
            data[i] = request.form.get(i, "")


    df = pd.DataFrame([data], columns=col_arr)

    pred_value = predict.main(model, le_dict, df)

    return jsonify({"pred_value": pred_value})


# Change port to 5001 and start debug mode
if __name__ == '__main__':
    app.run(debug=False, port=5001)