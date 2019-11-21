﻿-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE "gdci_city_country" (
    "City" VARCHAR(255)   NOT NULL,
    "Country" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_gdci_city_country" PRIMARY KEY (
        "City","Country"
     )
);

CREATE TABLE "gdci_expenses" (
    "City" VARCHAR(255)   NOT NULL,
    "Year" INTEGER   NOT NULL,
    "Overnight_International_Visitor_Spend_in_USD_Billions" FLOAT   NULL,
    CONSTRAINT "pk_gdci_expenses" PRIMARY KEY (
        "City","Year"
     ),
    FOREIGN KEY("City") REFERENCES "gdci_city_country" ("City")
);

CREATE TABLE "gdci_tourists" (
    "City" VARCHAR(255)   NOT NULL,
    "Year" INTEGER   NOT NULL,
    "Overnight_International_Visitors_in_Millions" FLOAT   NULL,
    CONSTRAINT "pk_gdci_tourists" PRIMARY KEY (
        "City","Year"
     ),
    FOREIGN KEY("City") REFERENCES "gdci_city_country" ("City")
);


CREATE TABLE "un_city_population" (
    "Country_Code" INTEGER   NOT NULL,
    "Country" VARCHAR(255)   NOT NULL,
    "City_Code" INTEGER   NOT NULL,
    "City" VARCHAR(255)   NOT NULL,
    "Latitude" FLOAT   NULL,
    "Longitude" FLOAT   NULL,
    "Year" INTEGER   NOT NULL,
    "Population_in_Thousands" FLOAT   NULL,
    "Interpolated" BOOLEAN   NULL,
    CONSTRAINT "pk_un_city_population" PRIMARY KEY (
        "Country_Code","City_Code","Year"
     )
);

CREATE TABLE "world_happiness_report_2017" (
    "Country" VARCHAR(255)   NOT NULL,
    "Happiness_Score" FLOAT   NOT NULL,
    "GDP_per_Capita" FLOAT   NOT NULL,
    "Social_Support" FLOAT   NOT NULL,
    "Healthy_Life_Expectency" FLOAT   NOT NULL,
    "Freedom_To_Make_Life_Choices" FLOAT   NOT NULL,
    "Genorosity" FLOAT   NOT NULL,
    "Perceptions_of_Corruption" FLOAT   NOT NULL,
    CONSTRAINT "pk_world_happiness_report_2017" PRIMARY KEY (
        "Country"
     )
);

CREATE TABLE "world_bank_country_classification" (
    "Country_Code" CHAR(3)   NOT NULL,
    "Region" VARCHAR(255)   NULL,
    "Income_Group" VARCHAR(255)   NULL,
    "Special_Notes" VARCHAR(1500)   NULL,
    "Country" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_world_bank_country_classification" PRIMARY KEY (
        "Country_Code"
     )
);

CREATE TABLE "world_bank_indicator_code" (
    "Indicator_Code" VARCHAR(255)   NOT NULL,
    "Indicator_Name" VARCHAR(255)   NOT NULL,
    "Source_Note" VARCHAR(1500)   NULL,
    "Source_Organization" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_world_bank_indicator_code" PRIMARY KEY (
        "Indicator_Code"
     )
);

CREATE TABLE "world_bank_tourism" (
    "Country" VARCHAR(255)   NOT NULL,
    "Country_Code" CHAR(3)   NOT NULL,
    "Indicator_Name" VARCHAR(255)   NOT NULL,
    "Indicator_Code" VARCHAR(255)   NOT NULL,
    "Year" INTEGER   NOT NULL,
    "Arrivals" FLOAT   NULL,
    "Departures" FLOAT   NULL,
    "Receipts" FLOAT   NULL,
    "Expenditures" FLOAT   NULL,
    CONSTRAINT "pk_world_bank_tourism" PRIMARY KEY (
        "Country_Code","Year"
     ),
    FOREIGN KEY("Country_Code") REFERENCES "world_bank_country_classification" ("Country_Code"),
    FOREIGN KEY("Indicator_Code") REFERENCES "world_bank_indicator_code" ("Indicator_Code")
);


