from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    forecast = pd.read_csv("forecast_output.csv").tail(10)
    return render_template("index.html", tables=[forecast.to_html(classes='data', index=False)], titles=forecast.columns.values)

if __name__ == "__main__":
    app.run(debug=True)
