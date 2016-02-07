from __future__ import absolute_import

import os

from flask import Flask, render_template, jsonify

from handlers.crime_maps_handler import CrimeMapsHandler


CRIME_MAPS_TOKEN = os.environ["CRIME_MAPS_TOKEN"]


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/crime")
def crime_view():
    cmh = CrimeMapsHandler(auth_token=CRIME_MAPS_TOKEN)
    return jsonify(ret=cmh._query("/crime", enddate="9/25/2015", lat=37.757815, long=-122.5076392, startdate="9/19/2015"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
