# sqlalchemy-challenge
## Precipitation Analysis:
The following steps are performed for this analysis:
1- Imported all required dependancies like pandas and matplotlib.
2- imported python SQL toolkit and Object Relational Mapper.
3- created engine.
4- Reflected an existing database into a new model and reflected the tables.
5- Listed all of the classes that automap found.
6- Saved references to tables as Measurement,Station.
7-Created session (link) from Python to the DB.
8-Found the most recent date in the data set using 'func.max'.
9- Retrieved the last 12 months of precipitation data,for that calculated the date one year from the last date in data set using 'time_delta'.
10- Performed a query to retrieve the data and precipitation scores of the last 12 months.
11- Saved the query results as a Pandas DataFrame as 'precipitation_df'.
12-Removed the null values and sorted the dataframe by date.
13-Used Matplotlib to plot the data.
14- Used Pandas to calculate the summary statistics for the precipitation data,in which count,mean,std,min,Q1,Q2,Q3 and max are calculated.
15- populated those results in a dataframe.

## Station Analysis:
In this analysis the following steps are performed:
1- Calculated the total number of stations in the dataset using 'func.count'.
2- Designed a query to find the most active stations ie, stations havimg most rows.For that, listed the stations and their counts in descending order and the first station taken as the most active one.
3- Using the most active station id from the previous query, calculated the lowest, highest, and average temperature.
4- Using the most active station id,found last 12 months of temperature observation data for this station and ploted the results as a histogram.

## Climate App:
Flask API is created based on the queries of the above analyses. So that,Flask is used to create the routes as follows:
1- Imported the dependencies.
2-Set up the DB.
3- Set up the Flask.
4-Set the routs as follows:

  1- "/" used as the home page route:
     * Start at the homepage.
     * List all the available routes.

  2- "/api/v1.0/precipitation" :
     * Retrevied last 12 months of percipation data from the previous analysis and return the JSON representation of the result as dictionary with date as key and percepation as value.

  3- "/api/v1.0/stations":
      * Retrieved all station names from the above analysis.
      * Returned a JSON list of stations from the dataset.

  4- "/api/v1.0/tobs":
      * From the above analysis retrieved temperature observations of the most-active station for the previous year of data.
      * Create a dictionary from the row data and append to a list of temp_list.
      * Returned a JSON list of temperature observations for the previous year.

  5- "/api/v1.0/<start>":
      * Calculated TMIN, TAVG, and TMAX for all the dates greater than or equal to the specified start date.
      * Created a dictionary from the row data and append to a list of temps_list.
      * Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date.

  6- "/api/v1.0/<start>/<end>":
      * Calculated TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
      * Created a dictionary from the row data and append to a list of temps_list.
      * Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for for the dates from the start date to the end date, inclusive.










