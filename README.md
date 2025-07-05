Fire Weather Index (FWI) Prediction Project
🔥 A machine learning approach to forest fire prediction using meteorological data and fire weather indices
Show Image
Show Image
Show Image
📋 Project Overview
This project develops a machine learning model to predict forest fire occurrence using the Fire Weather Index (FWI) system and meteorological data from two regions in Algeria: Bejaia and Sidi-Bel Abbes. The goal is to create an accurate binary classification system that can distinguish between fire and non-fire conditions based on weather parameters and fire danger indices.
🌍 Dataset Description
The dataset contains daily meteorological observations and fire weather indices from two Algerian regions during the 2012 fire season:

Bejaia Region: 122 observations
Sidi-Bel Abbes Region: 122 observations
Total: 244 daily records
Time Period: June 1 - September 30, 2012
Data Quality: Complete daily records with no missing values

🔢 Features
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
Binary classification:

fire: Days with fire conditions
not fire: Days without fire conditions

🚀 Getting Started
Prerequisites
bashPython 3.8+
pip (Python package manager)
Installation

Clone the repository:

bashgit clone https://github.com/yourusername/fwi-prediction.git
cd fwi-prediction

Create a virtual environment:

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required packages:

bashpip install -r requirements.txt
Required Dependencies
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
📁 Project Structure
fwi-prediction/
├── data/
│   ├── raw/
│   │   └── algeria_fires_2012.csv
│   └── processed/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_development.ipynb
│   └── 04_model_evaluation.ipynb
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── prediction.py
├── models/
│   └── saved_models/
├── results/
│   ├── figures/
│   └── reports/
├── requirements.txt
├── README.md
└── LICENSE
🔬 Technical Approach
1. Data Preprocessing

Data cleaning and standardization
Handling categorical variables
Feature scaling and normalization

2. Feature Engineering

Creating derived features from FWI components
Temporal feature extraction
Regional feature analysis

3. Model Development

Random Forest: Ensemble learning approach
Support Vector Machine (SVM): Non-linear classification
Neural Networks: Deep learning approach
Gradient Boosting: Advanced ensemble method

4. Model Validation

Cross-validation techniques
Performance evaluation metrics
Regional model comparison

📊 Usage
Running the Complete Pipeline
bashpython src/main.py
Individual Components
bash# Data preprocessing
python src/data_preprocessing.py

# Feature engineering
python src/feature_engineering.py

# Model training
python src/model_training.py

# Make predictions
python src/prediction.py --input data/new_data.csv
Jupyter Notebooks
Launch Jupyter and explore the analysis notebooks:
bashjupyter notebook
📈 Model Performance
Expected performance metrics:

Accuracy: >85%
Precision: >80%
Recall: >80%
F1-Score: >80%

🎯 Applications
This predictive model can be utilized for:

Early Warning Systems: Alerting authorities of high fire risk days
Resource Planning: Optimizing firefighting resource allocation
Risk Assessment: Evaluating fire danger for outdoor activities
Climate Research: Understanding fire-weather relationships
Forest Management: Supporting decision-making for controlled burns

🔍 Key Insights

Identification of critical meteorological factors influencing fire occurrence
Regional comparison of fire weather patterns between Bejaia and Sidi-Bel Abbes
Seasonal trends in fire danger indices
Correlation analysis between weather variables and fire risk

🤝 Contributing

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
📚 References

Canadian Forest Service Fire Weather Index System
Algerian National Weather Service
Forest Fire Research and Management Studies

👥 Authors

Your Name - Initial work - YourGitHub

🙏 Acknowledgments

Algerian Meteorological Service for providing the dataset
Canadian Forest Service for the FWI system methodology
Open source community for the tools and libraries used

📧 Contact
For questions or collaboration opportunities, please reach out:

Email: your.email@example.com
LinkedIn: Your LinkedIn Profile
Project Link: https://github.com/yourusername/fwi-prediction


⚠️ Disclaimer: This model is intended for research and educational purposes. For operational fire management decisions, please consult with professional meteorologists and fire management authorities.
