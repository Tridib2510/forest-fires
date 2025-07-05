from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler

applicaiton=Flask(__name__)
app=applicaiton

#import ridge regressor and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')#It will try to find index.html inside template folder


@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
   if request.method=='POST':
       Temperature=float(request.form.get('Temperature'))#This temperature should match with name in html file
       RH=float(request.form.get('RH'))
       Ws=float(request.form.get('Ws'))
       Rain=float(request.form.get('Rain'))
       FFMC=float(request.form.get('FFMC'))
       DMC=float(request.form.get('DMC'))
       ISI=float(request.form.get('ISI'))
       Classes=float(request.form.get('Classes'))
       Region=float(0 if request.form.get('Region')=='Bejaia Region' else 1)
      #For the new datapoints
       new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
       result=ridge_model.predict(new_data_scaled)
       print([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
       return render_template('home.html',results=result[0])
   else:
    return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)#This 0.0.0.0 map to the local IP address of your device