# pylint: skip-file
import os
ENV_URI = os.getenv('DATABASE_URL')

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = ENV_URI
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
GDCI_Expenses                       = Base.classes.gdci_expenses
GDCI_Tourists                       = Base.classes.gdci_tourists
GDCI_City_Country                   = Base.classes.gdci_city_country
World_Bank_Tourism                  = Base.classes.world_bank_tourism
World_Bank_Country_Classification   = Base.classes.world_bank_country_classification
World_Bank_Indicator_Code           = Base.classes.world_bank_indicator_code
World_Happiness_Report              = Base.classes.world_happiness_report
UN_City_Population                  = Base.classes.un_city_population


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/gdci-city-country")
def city_country():
    """Return all cities and their corresponding countries in the GDCI data"""
    results_list = []
    all_columns = [ 
                    GDCI_City_Country.City, 
                    GDCI_City_Country.Country
                  ]

    results = db.session.query(*all_columns).all()

    for result in results:
        results_dict = {}
        results_dict["City"] = result[0]
        results_dict["Country"] = result[1]
        results_list.append(results_dict)

    return jsonify(results_list)


@app.route("/gdci-expenses")
def expenses():
    """Return all cities and their corresponding countries in the GDCI data"""
    results_list = []
    all_columns = [ 
                    GDCI_Expenses.City, 
                    GDCI_Expenses.Year, 
                    GDCI_Expenses.Overnight_International_Visitor_Spend_in_USD_Billions
                  ]

    results = db.session.query(*all_columns).all()

    for result in results:
        results_dict = {}
        results_dict["City"] = result[0]
        results_dict["Year"] = result[1]
        results_dict["Expenses_in_USD_Billions"] = result[2]
        results_list.append(results_dict)
        
    return jsonify(results_list)


@app.route("/gdci-tourists")
def tourists():
    """Return all cities and their corresponding countries in the GDCI data"""
    results_list = []
    all_columns = [ 
                    GDCI_Tourists.City, 
                    GDCI_Tourists.Year, 
                    GDCI_Tourists.Overnight_International_Visitors_in_Millions
                  ]

    results = db.session.query(*all_columns).all()

    for result in results:
        results_dict = {}
        results_dict["City"] = result[0]
        results_dict["Year"] = result[1]
        results_dict["Visitors_in_Millions"] = result[2]
        results_list.append(results_dict)
        
    return jsonify(results_list)


@app.route("/world-bank-tourism")
def world_bank_tourists():
    """Return all cities and their corresponding countries in the GDCI data"""
    results_list = []
    all_columns =   [ 
                        World_Bank_Tourism.Country, 
                        World_Bank_Tourism.Country_Code, 
                        World_Bank_Tourism.Year, 
                        World_Bank_Tourism.Arrivals_in_Thousands, 
                        World_Bank_Tourism.Departures_in_Thousands, 
                        World_Bank_Tourism.Receipts_in_USD_Millions, 
                        World_Bank_Tourism.Expenditures_in_USD_Millions, 
                        World_Bank_Tourism.Population_in_Thousands
                    ]

    results = db.session.query(*all_columns).all()

    for result in results:
        results_dict = {}
        results_dict["Country"]                         = result[0]
        results_dict["Country_Code"]                    = result[1]
        results_dict["Year"]                            = result[2]
        results_dict["Arrivals_in_Thousands"]           = result[3]
        results_dict["Departures_in_Thousands"]         = result[4]
        results_dict["Receipts_in_USD_Millions"]        = result[5]
        results_dict["Expenditures_in_USD_Millions"]    = result[6]
        results_dict["Population_in_Thousands"]         = result[7]
        
        results_list.append(results_dict)
        
    return jsonify(results_list)


@app.route("/world-bank-country")
def world_bank_country():
    """Return all cities and their corresponding countries in the GDCI data"""
    results_list = []
    all_columns =   [ 
                        World_Bank_Country_Classification.Country_Code,
                        World_Bank_Country_Classification.Country, 
                        World_Bank_Country_Classification.Region, 
                        World_Bank_Country_Classification.Income_Group, 
                        World_Bank_Country_Classification.Special_Notes
                    ]

    results = db.session.query(*all_columns).all()

    for result in results:
        results_dict = {}
        results_dict["Country_Code"]    = result[0]
        results_dict["Country"]         = result[1]
        results_dict["Region"]          = result[2]
        results_dict["Income_Group"]    = result[3]
        results_dict["Special_Notes"]   = result[4]
        
        results_list.append(results_dict)
        
    return jsonify(results_list)


@app.route("/world-bank-indicator")
def world_bank_indicator():
    """Return all cities and their corresponding countries in the GDCI data"""
    results_list = []
    all_columns =   [ 
                        World_Bank_Indicator_Code.Indicator_Code,
                        World_Bank_Indicator_Code.Indicator_Name, 
                        World_Bank_Indicator_Code.Source_Note, 
                        World_Bank_Indicator_Code.Source_Organization
                    ]

    results = db.session.query(*all_columns).all()

    for result in results:
        results_dict = {}
        results_dict["Indicator_Code"]      = result[0]
        results_dict["Indicator_Name"]      = result[1]
        results_dict["Source_Note"]         = result[2]
        results_dict["Source_Organization"] = result[3]
        
        results_list.append(results_dict)
        
    return jsonify(results_list)


@app.route("/world-happiness")
def world_happiness():
    """Return all cities and their corresponding countries in the GDCI data"""
    results_list = []
    all_columns =   [ 
                        World_Happiness_Report.Country, 
                        World_Happiness_Report.Happiness_Score, 
                        World_Happiness_Report.GDP_per_Capita, 
                        World_Happiness_Report.Social_Support, 
                        World_Happiness_Report.Healthy_Life_Expectancy, 
                        World_Happiness_Report.Freedom_to_Make_Life_Choices, 
                        World_Happiness_Report.Generosity, 
                        World_Happiness_Report.Perceptions_of_Corruption,
                        World_Happiness_Report.Report_Year,
                        World_Happiness_Report.Years_Averaged
                    ]

    results = db.session.query(*all_columns).all()

    for result in results:
        results_dict = {}
        results_dict["Country"]                         = result[0]
        results_dict["Happiness_Score"]                 = result[1]
        results_dict["GDP_per_Capita"]                  = result[2]
        results_dict["Social_Support"]                  = result[3]
        results_dict["Healthy_Life_Expectancy"]         = result[4]
        results_dict["Freedom_to_Make_Life_Choices"]    = result[5]
        results_dict["Generosity"]                      = result[6]
        results_dict["Perceptions_of_Corruption"]       = result[7]
        results_dict["Report_Year"]                     = result[8]
        results_dict["Years_Averaged"]                  = result[9]
        
        results_list.append(results_dict)
        
    return jsonify(results_list)

@app.route("/un_city_population")
def un_city_pop():
    """Return all cities and their corresponding countries in the GDCI data"""
    results_list = []
    all_columns =   [ 
                        UN_City_Population.Country_Code, 
                        UN_City_Population.Country, 
                        UN_City_Population.City_Code, 
                        UN_City_Population.City, 
                        UN_City_Population.Latitude, 
                        UN_City_Population.Longitude, 
                        UN_City_Population.Year, 
                        UN_City_Population.Population_in_Thousands,
                        UN_City_Population.Interpolated
                    ]

    results = db.session.query(*all_columns).all()

    for result in results:
        results_dict = {}
        results_dict["Country_Code"]            = result[0]
        results_dict["Country"]                 = result[1]
        results_dict["City_Code"]               = result[2]
        results_dict["City"]                    = result[3]
        results_dict["Latitude"]                = result[4]
        results_dict["Longitude"]               = result[5]
        results_dict["Year"]                    = result[6]
        results_dict["Population_in_Thousands"] = result[7]
        results_dict["Interpolated"]            = result[8]
        
        results_list.append(results_dict)
        
    return jsonify(results_list)


if __name__ == "__main__":
    app.run()
