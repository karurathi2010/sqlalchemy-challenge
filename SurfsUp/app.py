# Import the dependencies.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement=Base.classes.measurement
Station=Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app=Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return(f"Welcome to the Climate App!!! <br>"
           f"The available routes are : <br>"
           f"/api/v1.0/precipitation <br>"
           f"/api/v1.0/stations <br>"
           f"/api/v1.0/tobs <br>"
           f"/api/v1.0/start <br>"
           f"/api/v1.0/start/end")


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session=Session(engine)

    #query to retrieve only the last 12 months of data.

    date_oneyear_ago=dt.date(2017,8,23)-dt.timedelta(days=365)

    perc_data = session.query(Measurement.prcp,Measurement.date).filter(Measurement.date>=date_oneyear_ago).all()

    session.close()
    # Create a dictionary from the row data and append to a list of perc_list.
    
    perc_list=[]

    for prcp,date in perc_data:
       perc_dict={}
       perc_dict[date]= prcp
       perc_list.append(perc_dict)


    return jsonify(perc_list)

@app.route("/api/v1.0/stations")
def station():
    # Create our session (link) from Python to the DB
    session=Session(engine)

   #query to retrieve all station names.
    stations = session.query(Station.station).all()

    session.close()
    # Convert list of tuples into normal list
    station_name=list(np.ravel(stations))

    return jsonify(station_name)


@app.route("/api/v1.0/tobs")
def temp():
    # Create our session (link) from Python to the DB
    session=Session(engine)

    #query to retrieve temperature observations of the most-active station for the previous year of data.
    active_station=session.query(Measurement.station,func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    stndate_oneyear_ago=dt.date(2017,8,18)-dt.timedelta(days=365)
    year_temp=session.query(Measurement.date,Measurement.tobs).filter(Measurement.station== active_station[0][0]).filter(Measurement.date>=stndate_oneyear_ago).all()

    session.close()
    # Create a dictionary from the row data and append to a list of temp_list.
    temp_list=[]

    for date,tobs in year_temp:
       temp_dict={}
       temp_dict[date]= tobs
       temp_list.append(temp_dict)


    return jsonify(temp_list)


@app.route("/api/v1.0/<start>")
def start_date(start:str):
     
    # Create our session (link) from Python to the DB
    session=Session(engine)
    #query to calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the specified start date.
    TMIN=func.min(Measurement.tobs)
    TAVG=func.avg(Measurement.tobs)
    TMAX=func.max(Measurement.tobs)
    temperature=session.query(TMIN,TAVG,TMAX).filter(Measurement.date >= start).all()              

    
    session.close()

    # Create a dictionary from the row data and append to a list of temps_list.

    temps_list=[]

    for TMIN,TAVG,TMAX in temperature:
       temps_dict={}
       temps_dict["Min_temperature"]= TMIN
       temps_dict["Avg_temperature"]= TAVG
       temps_dict["Max_temperature"]= TMAX
       temps_list.append(temps_dict)
    return jsonify(temps_list)


@app.route("/api/v1.0/<start>/<end>")
def dates(start:str,end:str):
    # Create our session (link) from Python to the DB
    session=Session(engine)
    #query to calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
    TMIN=func.min(Measurement.tobs)
    TAVG=func.avg(Measurement.tobs)
    TMAX=func.max(Measurement.tobs)
    temperature=session.query(TMIN,TAVG,TMAX).filter(Measurement.date >= start).filter(Measurement.date <= end).all()              

    
    session.close()

    # Create a dictionary from the row data and append to a list of temps_list.

    temps_list=[]

    for TMIN,TAVG,TMAX in temperature:
       temps_dict={}
       temps_dict["Min_temperature"]= TMIN
       temps_dict["Avg_temperature"]= TAVG
       temps_dict["Max_temperature"]= TMAX
       temps_list.append(temps_dict)

    return jsonify(temps_list)



if __name__=="__main__":
    app.run(debug=True)