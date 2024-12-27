from flask import Flask, render_template, request, redirect, url_for
import weather_api

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    units = weather_api.units
    if request.method == "POST":
        location = request.form["weather_location"]
        data = weather_api.get_weather_api(location)
        return render_template("home/index.html", data=data, units=units)  
    return render_template("home/index.html", data=None, units=None)       
        

if __name__ == "__main__":
    app.run(debug=True)