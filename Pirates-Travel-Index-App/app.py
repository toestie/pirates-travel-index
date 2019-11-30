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
GDCI_Tourists                       = Base.classes.gdci_tourists
GDCI_Expenses                       = Base.classes.gdci_expenses
GDCI_City_Country                   = Base.classes.gdci_city_country
World_Bank_Tourism                  = Base.classes.world_bank_tourism
World_Bank_Country_Classification   = Base.classes.world_bank_country_classification
World_Bank_Indicator_Code           = Base.classes.world_bank_indicator_code
World_Happiness_Report              = Base.classes.world_happiness_report
UN_City_Population                  = Base.classes.un_city_population


@app.route("/")
def home():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/maps")
def maps():
    """Return the homepage."""
    return render_template("maps.html")


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

    df = pd.DataFrame(results_list).sort_values(["Year", "Visitors_in_Millions"], ascending=[True, False])
    df_top10 = df.groupby("Year").head(10).reset_index(drop=True)
    df_top10['Rank'] = df_top10.groupby('Year').cumcount()+1

    df_top10_line = df_top10.copy()
    df_top10_line["id"] = "line"

    df_top10_circle = df_top10.copy()
    df_top10_circle["id"] = "circle"

    df_top10 = pd.concat([df_top10_line, df_top10_circle])
    df_top10.sort_values(['Year', 'Rank', 'id']).reset_index(drop=True)

    top10_results = df_top10.to_dict('records')
        
    return jsonify(top10_results)


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
        
    df = pd.DataFrame(results_list).sort_values(["Year", "Expenses_in_USD_Billions"], ascending=[True, False])
    df_top10 = df.groupby("Year").head(10).reset_index(drop=True)
    df_top10['Rank'] = df_top10.groupby('Year').cumcount()+1

    df_top10_line = df_top10.copy()
    df_top10_line["id"] = "line"

    df_top10_circle = df_top10.copy()
    df_top10_circle["id"] = "circle"

    df_top10 = pd.concat([df_top10_line, df_top10_circle])
    df_top10.sort_values(['Year', 'Rank', 'id']).reset_index(drop=True)

    top10_results = df_top10.to_dict('records')
    
    return jsonify(top10_results)


@app.route("/un_city_population")
def un_city_pop():
    """Return all cities and their corresponding countries in the GDCI data"""
    results_list = []
    all_columns =   [ 
                        UN_City_Population.Country, 
                        UN_City_Population.City, 
                        UN_City_Population.Year, 
                        UN_City_Population.Population_in_Thousands,
                        UN_City_Population.Interpolated
                    ]

    results = db.session.query(*all_columns).all()

    for result in results:
        results_dict = {}
        results_dict["Country"]                 = result[0]
        results_dict["City"]                    = result[1]
        results_dict["Year"]                    = result[2]
        results_dict["Population_in_Thousands"] = result[3]
        results_dict["Interpolated"]            = result[4]
        
        results_list.append(results_dict)
        
    return jsonify(results_list)


@app.route("/tourism-ratio")
def tourism_ratio():
    """Return all cities and their corresponding countries in the GDCI data"""
    un_results_list = []
    un_city_columns =   [ 
                        UN_City_Population.Country, 
                        UN_City_Population.City, 
                        UN_City_Population.Year, 
                        UN_City_Population.Population_in_Thousands,
                    ]

    un_results = db.session.query(*un_city_columns).all()

    for result in un_results:
        results_dict = {}
        results_dict["Country"]                 = result[0]
        results_dict["City"]                    = result[1]
        results_dict["Year"]                    = result[2]
        results_dict["Population_in_Thousands"] = result[3]
        
        un_results_list.append(results_dict)

    un_df = pd.DataFrame(un_results_list)
    un_df["Population_in_Thousands"] = un_df["Population_in_Thousands"] / 1000
    un_df = un_df.rename(columns={"Population_in_Thousands": "Population_in_Millions"})

    """Return all cities and their corresponding countries in the GDCI data"""
    gdci_results_list = []
    gdci_columns = [ 
                    GDCI_Tourists.City, 
                    GDCI_Tourists.Year, 
                    GDCI_Tourists.Overnight_International_Visitors_in_Millions
                  ]

    gdci_results = db.session.query(*gdci_columns).all()

    for result in gdci_results:
        results_dict = {}
        results_dict["City"] = result[0]
        results_dict["Year"] = result[1]
        results_dict["Visitors_in_Millions"] = result[2]
        gdci_results_list.append(results_dict)

    gdci_df = pd.DataFrame(gdci_results_list)

    combined_df = gdci_df.merge(right=un_df, how="inner", on=["City", "Year"])
    combined_df["Tourist_Ratio_Index"] = combined_df["Visitors_in_Millions"] / combined_df["Population_in_Millions"]
    combined_df = combined_df.sort_values(["Year", "Tourist_Ratio_Index"], ascending=[True, False])
    combined_df = combined_df.groupby("Year").head(10).reset_index(drop=True)
    combined_df['Rank'] = combined_df.groupby('Year').cumcount()+1

    combined_df_line = combined_df.copy()
    combined_df_line["id"] = "line"

    combined_df_circle = combined_df.copy()
    combined_df_circle["id"] = "circle"

    combined_df = pd.concat([combined_df_line, combined_df_circle])
    combined_df.sort_values(['Year', 'Rank', 'id']).reset_index(drop=True)

    top10_results = combined_df.to_dict('records')
        
    return jsonify(top10_results)

if __name__ == "__main__":
    app.run()
