# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:39:31 2023

@author: LOTACHIM EHIEZE
"""

import pandas as pd
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

pl = pd.read_csv("C:/Users/LOTACHIM EHIEZE/Documents/Master_notes/archive (1)/stadcleaned.csv")

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Stadium Data API"

@app.route('/stadiums/all', methods=['GET'])
def get_stadiums():
    return jsonify(pl.to_dict(orient="records"))

# API endpoint to filter the data based on confederation
@app.route('/stadiums', methods=['GET'])
def filter_stadiums():
    confederation = request.args.get('confederation')
    country = request.args.get('country')
    
    if confederation and country:
        filtered_data = pl[(pl['Confederation'] == confederation) & (pl['Country'] == country)]
    elif confederation:
        filtered_data = pl[pl['Confederation'] == confederation]
    elif country:
        filtered_data = pl[pl['Country'] == country]
    else:
        return "Error: Please specify a confederation or country"
    
    return jsonify(filtered_data.to_dict(orient="records"))
if __name__ == '__main__':
    app.run(debug=True)