import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv("processed_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df_prophet = df[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})

model = Prophet()
model.fit(df_prophet)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("forecast_output.csv", index=False)

model.plot(forecast)
plt.title("Stock Price Forecast (Next 30 Days)")
plt.xlabel("Date")
plt.ylabel("Predicted Price")
plt.tight_layout()
plt.show()
