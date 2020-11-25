import joblib
from flask import Flask,render_template,request,send_from_directory
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__,static_url_path='', static_folder='web/static')

@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    pkl_model = open("rf_best.pkl", "rb")
    model = joblib.load(pkl_model)
    global result
    classes = np.array(["Charged off", "Fully Paid"])
    if request.method == "POST":
        term = request.form['Term']
        credit_score = request.form['Credit Score']
        annual_income = request.form['Annual Income']
        years_credit_hist = request.form['Years of Credit History']
        home_ownership = request.form['Home Ownership']
        current_loan_amount = request.form["Current Loan Amount"]
        
        input_data = [{
            'Term': term,
            'Credit Score': credit_score,
            'Annual Income': annual_income,
            'Years of Credit History': years_credit_hist,
            'Home Ownership': home_ownership,
            'Current Loan Amount': current_loan_amount
        }]
        data = pd.DataFrame(input_data)
        result = model.predict(data)
        proba_result = model.predict_proba(data)
        if result == 0:
            proba = (proba_result[:,0][0] *100)
        else:
            proba = (proba_result[:,1][0] *100)
        return render_template("prediction.html", script=classes[result].item(), probability=proba)

@app.route('/data')
def data():
    sqlengine = create_engine('mysql+mysqlconnector://brandon:xxxxxxxxxx@localhost/credit?host=localhost?port=3306')
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    cursor.execute("SELECT * FROM mytable")
    data2 = cursor.fetchall()
    return render_template('data.html', data=data2)

@app.route('/pie')
def pie():
    return render_template('pie.html')

@app.route('/bar')
def bar():
    return render_template('bar.html')

if __name__ == '__main__':
    app.run(debug=True)