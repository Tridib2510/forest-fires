Fire Weather Index (FWI) Prediction Model
A machine learning model to predict Fire Weather Index (FWI) for forest fire risk assessment in two Algerian regions: Sidi-Bel Abbes and Bejaia.

Model Overview
This model predicts the Fire Weather Index based on meteorological data and fire weather components for two specific regions in Algeria.

Input Parameters
The model requires the following input parameters:

Meteorological Variables
Temperature: Daily temperature in degrees Celsius (°C)
RH: Relative Humidity as a percentage (%)
Ws: Wind Speed in kilometers per hour (km/h)
Rain: Daily precipitation in millimeters (mm)
Fire Weather Index Components
FFMC: Fine Fuel Moisture Code - indicates moisture content of fine fuels
DMC: Duff Moisture Code - indicates moisture content of organic matter
ISI: Initial Spread Index - indicates the rate of fire spread
Classification Variables
Classes: Fire occurrence classification (numerical value)
Region: Geographic region selection
0 = Bejaia Region
1 = Sidi-Bel Abbes Region
Usage
The model takes these parameters as input and returns the predicted Fire Weather Index value for the specified region.

Regions Covered
Bejaia Region (Region = 0)
Sidi-Bel Abbes Region (Region = 1)
Both regions are located in Algeria and have different climate patterns that affect fire weather conditions.

