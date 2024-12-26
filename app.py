from flask import Flask, render_template, request, redirect, url_for
import weather_api

app = Flask(__name__)

@app.route("/")
def home():
    units = weather_api.units
    return render_template("home/index.html", data=None, units=units)

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        location = request.form["weather_location"]
        data = weather_api.get_weather_api(location=location)
        return redirect(url_for("home"))
        
        

if __name__ == "__main__":
    app.run(debug=True)