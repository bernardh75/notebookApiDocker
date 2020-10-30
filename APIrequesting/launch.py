from flask import Flask, render_template, request

import json
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title='Home')

#2
@app.route("/prediction", methods=['POST'])
def retour():
    
    user_text = request.form.get('input_sqft')
    #cls = pickle.load(open("./data/house_model.pkl", "rb"))
    #return cls.predict(np.array([int(user_text), 5]).reshape(1,-1))

    lr_baseline = pickle.load(open('./data/house_model.pkl', 'rb'))
    resp = int(lr_baseline.predict(np.array([int(user_text), 4]).reshape(1,-1)))

    return "L'estimation selon le mètre carré donné est de : " + str(resp) + "$"

if __name__ == "__main__":
    app.run(debug=True)


