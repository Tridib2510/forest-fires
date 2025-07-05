# Fire Weather Index (FWI) Prediction Model

🔥 **Machine Learning Model for Forest Fire Risk Assessment in Algeria**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Prediction-orange.svg)](https://scikit-learn.org/)

## 📋 Overview

This machine learning model predicts the Fire Weather Index (FWI) for forest fire risk assessment in two Algerian regions: **Sidi-Bel Abbes** and **Bejaia**. The model uses meteorological data and fire weather components to assess fire danger levels.

## 🌍 Regions Covered

- **Bejaia Region** (Region Code: 0)
- **Sidi-Bel Abbes Region** (Region Code: 1)

Both regions are located in Algeria and have distinct climate patterns that influence fire weather conditions.

## 📊 Input Parameters

The model requires the following input parameters:

### Meteorological Variables

| Parameter     | Description         | Unit  | Type  |
|---------------|---------------------|-------|-------|
| **Temperature** | Daily temperature   | °C    | Float |
| **RH**          | Relative Humidity   | %     | Float |
| **Ws**          | Wind Speed          | km/h  | Float |
| **Rain**        | Daily precipitation | mm    | Float |

### Fire Weather Index Components

| Parameter | Description                                         | Type  |
|-----------|-----------------------------------------------------|-------|
| **FFMC**  | Fine Fuel Moisture Code - moisture content of fine fuels | Float |
| **DMC**   | Duff Moisture Code - moisture content of organic matter  | Float |
| **ISI**   | Initial Spread Index - rate of fire spread              | Float |

### Classification Variables

| Parameter   | Description                    | Values                             | Type  |
|-------------|--------------------------------|------------------------------------|-------|
| **Classes** | Fire occurrence classification | Numerical value                    | Float |
| **Region**  | Geographic region              | 0 = Bejaia Region<br>1 = Sidi-Bel Abbes Region | Float |

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
Flask 2.0+
scikit-learn
pandas
numpy
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fwi-prediction-model.git
   cd fwi-prediction-model
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## 💻 Usage

### Web Interface

The model is deployed as a Flask web application. Users can input the required parameters through a web form and receive FWI predictions.

### API Endpoint

```python
# Example form data structure
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
```

### Region Encoding

- Input `'Bejaia Region'` → Model receives `0`
- Input `'Sidi-Bel Abbes Region'` → Model receives `1`

## 📁 Project Structure

```
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
```

## 🎯 Model Output

The model returns a predicted Fire Weather Index value that indicates the fire danger level for the specified region based on the input meteorological conditions.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact



**⚠️ Note**: This model is designed for research and educational purposes. For operational fire management decisions, consult with professional meteorologists and fire management authorities.
