Fire Weather Index (FWI) Prediction Model
🔥 Machine Learning Model for Forest Fire Risk Assessment in Algeria
Show Image
Show Image
Show Image
📋 Overview
This machine learning model predicts the Fire Weather Index (FWI) for forest fire risk assessment in two Algerian regions: Sidi-Bel Abbes and Bejaia. The model uses meteorological data and fire weather components to assess fire danger levels.
🌍 Regions Covered

Bejaia Region (Region Code: 0)
Sidi-Bel Abbes Region (Region Code: 1)

Both regions are located in Algeria and have distinct climate patterns that influence fire weather conditions.
📊 Input Parameters
The model requires the following input parameters:
Meteorological Variables
ParameterDescriptionUnitTypeTemperatureDaily temperature°CFloatRHRelative Humidity%FloatWsWind Speedkm/hFloatRainDaily precipitationmmFloat
Fire Weather Index Components
ParameterDescriptionTypeFFMCFine Fuel Moisture Code - moisture content of fine fuelsFloatDMCDuff Moisture Code - moisture content of organic matterFloatISIInitial Spread Index - rate of fire spreadFloat
Classification Variables
ParameterDescriptionValuesTypeClassesFire occurrence classificationNumerical valueFloatRegionGeographic region0 = Bejaia Region<br>1 = Sidi-Bel Abbes RegionFloat
🚀 Getting Started
Prerequisites
bashPython 3.8+
Flask 2.0+
scikit-learn
pandas
numpy
Installation

Clone the repository:

bashgit clone https://github.com/yourusername/fwi-prediction-model.git
cd fwi-prediction-model

Install required packages:

bashpip install -r requirements.txt

Run the application:

bashpython app.py
💻 Usage
Web Interface
The model is deployed as a Flask web application. Users can input the required parameters through a web form and receive FWI predictions.
API Endpoint
python# Example form data structure
data = {
    'Temperature': 25.5,
    'RH': 65.0,
    'Ws': 12.0,
    'Rain': 0.0,
    'FFMC': 85.2,
    'DMC': 15.4,
    'ISI': 8.3,
    'Classes': 1.0,
    'Region': 'Bejaia Region'  # Will be converted to 0
}
Region Encoding

Input 'Bejaia Region' → Model receives 0
Input 'Sidi-Bel Abbes Region' → Model receives 1

📁 Project Structure
fwi-prediction-model/
├── app.py                 # Flask application
├── model/
│   └── fwi_model.pkl     # Trained model file
├── templates/
│   └── index.html        # Web interface
├── static/
│   ├── css/
│   └── js/
├── requirements.txt
└── README.md
🎯 Model Output
The model returns a predicted Fire Weather Index value that indicates the fire danger level for the specified region based on the input meteorological conditions.
🤝 Contributing

Fork the repository
Create a feature branch (git checkout -b feature/improvement)
Commit your changes (git commit -m 'Add improvement')
Push to the branch (git push origin feature/improvement)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
📧 Contact
For questions or support, please contact:

Email: your.email@example.com
Project Link: https://github.com/yourusername/fwi-prediction-model


⚠️ Note: This model is designed for research and educational purposes. For operational fire management decisions, consult with professional meteorologists and fire management authorities.
