# 📘 Project Overview: Stock Market Forecasting & Signal Generator

This project demonstrates a complete AI-driven pipeline to forecast stock prices and generate trading signals using time series analysis and machine learning. It's built to align with internship and entry-level roles in machine learning, data science, and AI in financial markets.

---

## ✅ What This Project Does

- 📥 Downloads historical stock data (e.g., AAPL) from Yahoo Finance
- 📊 Applies technical indicators: RSI, MACD, Bollinger Bands using `ta`
- 🔮 Forecasts the next 30 days of prices using `Facebook Prophet`
- 🚦 Generates trading signals (Buy/Sell/Hold) based on predictions
- 🌐 Displays forecast output in a Flask-based web dashboard

---

## 💡 Why This Project Matters

- Financial markets are rich in time series data — making them ideal for ML forecasting.
- Traders, investors, and analysts rely on indicators and prediction tools.
- Automating signal generation helps simulate real-world trading scenarios.
- Demonstrates end-to-end skills required for AI in finance roles.

---

## 🛠 Technologies & Tools Used

| Tool/Library     | Reason for Use |
|------------------|----------------|
| Python           | Industry standard for ML & finance |
| yfinance         | Simple API to pull real-time historical stock data |
| pandas, numpy    | Data cleaning, manipulation, and analysis |
| ta               | Calculate technical indicators like RSI, MACD |
| Prophet          | Time series forecasting with seasonality/trend detection |
| matplotlib       | Plotting predicted trends |
| Flask            | Lightweight web framework for displaying forecasts |

---

## 🔍 Model Choice: Why Prophet?

| Prophet                     | LSTM                           |
|-----------------------------|--------------------------------|
| Quick and easy to implement | Requires complex setup         |
| Transparent & interpretable | Black box model                |
| Handles trends & holidays   | Needs heavy tuning             |
| Good for prototyping        | Better for deep forecasting    |

> Prophet is ideal for internship projects that require explainability and business-friendly output.

---

## ⚙️ Signal Generation Logic

```python
if predicted > actual * 1.02:
    return "Buy"
elif predicted < actual * 0.98:
    return "Sell"
else:
    return "Hold"
```

This reflects simple rule-based decision logic that can be extended to more advanced strategies later.


---

## 🧠 Built by: Pragya Vijay

**BTech CSE | Machine Learning Enthusiast | AI in Finance Aspirant**  
GitHub: [PragyaVijay1222](https://github.com/PragyaVijay1222)
