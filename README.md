Fire Weather Index (FWI) Prediction Project
Project Overview
This project focuses on developing a machine learning model to predict forest fire occurrence using the Fire Weather Index (FWI) system and meteorological data from two regions in Algeria: Bejaia and Sidi-Bel Abbes. The goal is to create an accurate classification system that can distinguish between fire and non-fire conditions based on weather parameters and fire danger indices.

Dataset Description
The dataset contains daily meteorological observations and fire weather indices from two Algerian regions during the 2012 fire season (June-September):

Bejaia Region: 122 observations
Sidi-Bel Abbes Region: 122 observations
Total: 244 daily records
Features
Meteorological Variables
Temperature: Daily temperature (°C)
Relative Humidity (RH): Percentage of moisture in the air
Wind Speed (Ws): Wind velocity (km/h)
Rain: Daily precipitation (mm)
Fire Weather Index Components
FFMC (Fine Fuel Moisture Code): Moisture content of fine fuels
DMC (Duff Moisture Code): Moisture content of organic matter
DC (Drought Code): Moisture content of deep organic matter
ISI (Initial Spread Index): Rate of fire spread
BUI (Buildup Index): Fuel available for combustion
FWI (Fire Weather Index): Overall fire danger rating
Target Variable
Classes: Binary classification
"fire": Days with fire conditions
"not fire": Days without fire conditions
Data Characteristics
Time Period: June 1 - September 30, 2012
Geographic Coverage: Two distinct regions with different climate patterns
Data Quality: Complete daily records with no missing values
Class Distribution: Mixed distribution of fire and non-fire days across both regions
Project Applications
This predictive model can be utilized for:

Early Warning Systems: Alerting authorities of high fire risk days
Resource Planning: Optimizing firefighting resource allocation
Risk Assessment: Evaluating fire danger for outdoor activities
Climate Research: Understanding fire-weather relationships
Forest Management: Supporting decision-making for controlled burns
Technical Approach
The project involves:

Data Preprocessing: Cleaning and standardizing meteorological data
Feature Engineering: Creating derived features from FWI components
Model Development: Training classification algorithms (Random Forest, SVM, Neural Networks)
Validation: Cross-validation and performance evaluation
Deployment: Creating a real-time prediction system
Expected Outcomes
Accurate fire/non-fire classification model with high precision and recall
Identification of key meteorological factors influencing fire occurrence
Regional comparison of fire weather patterns
Practical tool for fire management authorities
This project contributes to fire prevention and management efforts by providing data-driven insights into fire weather conditions, ultimately helping protect forests, property, and human lives.

