import pandas as pd

df = pd.read_csv("forecast_output.csv")
actual_price = pd.read_csv("processed_data.csv")['Close'].iloc[-1]
predicted_price = df['yhat'].iloc[-1]

def generate_signal(actual, predicted):
    if predicted > actual * 1.02:
        return "Buy"
    elif predicted < actual * 0.98:
        return "Sell"
    else:
        return "Hold"

signal = generate_signal(actual_price, predicted_price)
print(f"📉 Actual: {actual_price:.2f}, 🔮 Predicted: {predicted_price:.2f}")
print(f"🚦 Signal: {signal}")
