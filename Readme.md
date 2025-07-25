# 📈 Stock Market Forecasting & Signal Generator

This project demonstrates a complete AI-driven pipeline to forecast stock prices and generate trading signals using time series analysis and machine learning. It's designed to align with financial data science and ML internship roles, such as AI in Finance.

---

## 🚀 Features

- ✅ Download historical stock data using the `yfinance` API
- ✅ Apply technical indicators: RSI, MACD, Bollinger Bands using `ta`
- ✅ Forecast future stock prices using Facebook Prophet
- ✅ Generate buy/sell/hold signals based on predicted trends
- ✅ Visualize forecasts in a simple web app using Flask
- ✅ Modular and easy to extend to LSTM, backtesting, or dashboarding

---

## 📂 Project Structure

stock_forecast_project/
│
├── data_pipeline.py # Fetch stock data + add indicators
├── prophet_forecasting.py # Forecast prices using Prophet
├── signal_generator.py # Generate trading signals
├── app.py # Flask app to display forecast
├── templates/
│ └── index.html # HTML template for display
├── README.md # You're reading it

---

## 🛠️ Setup Instructions

### 🧪 Create a virtual environment (recommended)

```bash
conda create -n stock-forecast python=3.10
conda activate stock-forecast
```
### 📦 Install required packages

```bash
pip install yfinance pandas matplotlib ta flask prophet
```

If Prophet fails to install via pip, use conda:

```bash
conda install -c conda-forge prophet
```

---

## 📊 How to Run

### 1. Get the stock data & indicators

```bash
python data_pipeline.py
```

### 2. Forecast stock price (next 30 days)

```bash
python prophet_forecasting.py
```

### 3. Generate trading signal

```bash
python signal_generator.py
```

### 4. View the forecast in browser

```bash
python app.py
```

Then open http://localhost:5000 in your browser.

---

## 📉 Example Signal Output

```bash
Actual: 175.32,  Predicted: 179.58
Suggested Action: Buy
```

---

## 🔧 To Extend

- Add LSTM modeling in place of Prophet
- Add backtesting logic to evaluate strategies
- Use Streamlit or Dash for interactive dashboard
- Include portfolio optimization for multiple assets

---

## 📬 Author
### Pragya Vijay
BTech CSE | Machine Learning | Data Science | AI in Finance
