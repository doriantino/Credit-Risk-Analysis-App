import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    credit_history = float(request.form['Credit_History'])
    applicant_income = int(request.form['ApplicantIncome'])
    loan_amount = float(request.form['LoanAmount'])
    coapplicant_income = float(request.form['CoapplicantIncome'])
    property_area_semiurban = int(request.form['Property_Area_Semiurban'])
    loan_amount_term = float(request.form['Loan_Amount_Term'])

    # Appliquer les mêmes étapes de prétraitement qu'à l'entraînement
    applicant_income_log = np.log1p(applicant_income)
    loan_amount_log = np.log1p(loan_amount)

    final_features = np.array([credit_history,
                               applicant_income_log,
                               loan_amount_log,
                               coapplicant_income,
                               property_area_semiurban,
                               loan_amount_term]).reshape(1, -1)

    prediction = model.predict(final_features)
    output = prediction[0]

    if output == 0:
        prediction_text = 'Prêt Refusé'
    else:
        prediction_text = 'Prêt Approuvé'

    # Renvoyer la prédiction au format JSON
    return jsonify({'prediction': prediction_text})

if __name__ == "__main__":
    app.run(debug=True)