from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("heart_model.pkl", "rb"))



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["POST"])
def predict():
    if request.method == "POST":

        # age
        age = int(request.form["age"])
        print("age : ",age)

        # sex
        sex = int(request.form["sex"])
        print("sex : ",sex)

        # chest pain
        cp = int(request.form["cp"])
        print("cp : ",cp)

              # trestbps
        trestbps =int(request.form["trestbps"])
        print("trestbps : ",trestbps)

        # chol
        chol = int(request.form["chol"])
        print("chol : ",chol)

        # fbs
        fbs = int(request.form["fbs"])
        print("fbs : ",fbs)
        
            # restecg
        restecg = int(request.form["restecg"])
        print("restecg : ",restecg)

        # thalach
        thalach = int(request.form["thalach"])
        print("thalach : ",thalach)

        # exang
        exang = int(request.form["exang"])
        print("exang : ",exang)

              # oldpeak
        oldpeak = float(request.form["oldpeak"])
        print("oldpeak : ",oldpeak)

        # slope
        slope = int(request.form["slope"])
        print("slope : ",slope)

        # ca
        ca = int(request.form["ca"])
        print("ca : ",ca)
        
              # thal
        thal = int(request.form["thal"])
        print("thal : ",thal)
        
        prediction=model.predict([[
           age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal
        ]])
        

        output=prediction[0]

        return render_template('result.html',prediction=output)



if __name__ == "__main__":
    app.run(debug=True)

