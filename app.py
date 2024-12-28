from flask import Flask, render_template, request, redirect, url_for
import weather_api
import caching

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    error_mssg = weather_api.error_message
    units = weather_api.units
    data = caching.get_cache_data()
    if request.method == "POST":
        location = request.form["weather_location"]
        weather_api.get_weather_api(location)
        data = caching.get_cache_data()
        return render_template("home/index.html", data=data, units=units, error_mssg=error_mssg)  
    return render_template("home/index.html", data=data, units=units, error_mssg=None)       


@app.route("/clear")
def clear_recent_forecast():
    caching.clear_recent_data()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)