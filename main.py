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

data = {}
col_arr = ["supplier", "amount", "department", "cost_center", "project_id", "personnel", "reference", "tax_percentage", "city", "created_at", "Test_category"] 

@app.route("/submit", methods=['POST'])
def submit():
    for i in col_arr:
        if i in ["tax_percentage", "amount"]:
            try:
                data[i] = float(request.form.get(i, ""))
            except:
                data[i] = 0.0
        else:
            data[i] = request.form.get(i, "")


    df = pd.DataFrame([data], columns=col_arr)
    print(df)

    pred_value = predict.main(model, le_dict, df)

    return jsonify({"pred_value": pred_value})


if __name__ == '__main__':
    app.run(debug=True, port=5001)