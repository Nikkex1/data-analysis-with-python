#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model

def split_date(df):
    #df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    df = df.dropna(how="all")
    df = df.dropna(axis=1,how="all")

    dates = df["Päivämäärä"]
    dates = dates.str.split(expand=True)

    # rename columns
    dates.rename(columns={
        0: "Weekday",
        1: "Day",
        2: "Month",
        3: "Year",
        4: "Hour"
    },inplace=True)

    # remove minutes
    dates["Hour"]=dates["Hour"].str.replace(":00","")

    # convert weekdays
    days = {"ma":"Mon","ti":"Tue","ke":"Wed","to":"Thu","pe":"Fri","la":"Sat","su":"Sun"}
    dates["Weekday"].replace(days,inplace=True)

    # convert months
    months = {"tammi":1,"helmi":2,"maalis":3,"huhti":4,"touko":5,"kesä":6,"heinä":7,"elo":8,"syys":9,"loka":10,"marras":11,"joulu":12}
    dates["Month"].replace(months,inplace=True)

    # convert datatypes
    dates = dates.astype({
        "Day": int,
        "Month": int,
        "Year": int,
        "Hour": int
    })

    return dates

def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    dates = split_date(df)
    df = df.dropna(how="all")
    df = df.dropna(axis=1,how="all")
    df.drop("Päivämäärä",axis="columns",inplace=True)

    df = pd.concat([dates,df],axis=1)

    return df

def cycling_weather_continues(station):
    c_df = split_date_continues()
    c_df = c_df[c_df["Year"] == 2017]
    #c_df = 
    daygroups = c_df.groupby(["Year","Month","Day"]).sum()
    w_df = pd.read_csv("src/kumpula-weather-2017.csv",sep=",")
    merged = pd.merge(daygroups,w_df,left_on=["Year","Month","Day"],right_on=["Year","m","d"]).ffill()
    X = merged.loc[:,
                   ["Precipitation amount (mm)",
                   "Snow depth (cm)",
                   "Air temperature (degC)"]]
    y = merged.loc[:,station]

    # explain station counts using daily weather data
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(X,y)
    r2 = model.score(X,y)
    # return regression coeffs and score

    return model.coef_,r2
    
def main():
    station = "Baana"
    intercept, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {intercept[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {intercept[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {intercept[2]:.1f}")
    print(f"Score: {score:.2f}")

if __name__ == "__main__":
    main()
