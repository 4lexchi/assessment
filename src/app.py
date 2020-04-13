from flask import Flask, request, render_template, url_for, g ,jsonify
from simplexml import dumps
from flask_restful import Resource, Api, reqparse
# from flask_sqlalchemy import SQLAlchemy
from estimator import estimator
import time

"""app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estimator.db'
db = SQLAlchemy(app)

class Add_entry(db.model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' %self.id

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        population = request.form['population']
        timeToElapse = request.form['timeToElapse']
        reportedCases = request.form['reportedCases']
        totalHospitalBeds = request.form['totalHospitalBeds']
        periodType = request.form['periodType']
        new_pop = Add_entry(content=population)
        new_time = Add_entry(content=timeToElapse)
        new_cases = Add_entry(content=reportedCases)
        new_beds = Add_entry(content=totalHospitalBeds)
        new_period = Add_entry(content=periodType)

        try:
            db.session.add(new_pop)
            db.session.add(new_time)
            db.session.add(new_cases)
            db.session.add(new_beds)
            db.session.add(new_period)
            db.session.commit()
        except:
            return "There was an issue adding your figures"
    else:
        data = Add_entry.query.all()
        return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
"""

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)


@app.before_request
def before_req():
    g.start = time.time() * 1000


@app.after_request
def after_req(response):
    f = open("logs.txt", "a+")
    req_method = request.method
    req_path = request.path
    res_status_code = response.status_code
    res_time = round(time.time() * 1000 - g.start)
    f.write("{}\t{}\t{}\t{} ms\n".format(req_method, req_path, res_status_code, res_time))
    f.close()
    return response


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/api/v1/on-covid-19", methods=["GET"])
def get_estimate_default():
    req_data = request.get_json()
    res = estimator(req_data)
    return jsonify(res)


@app.route("/api/v1/on-covid-19/json", methods=["GET"])
def get_estimate_json():
    return get_estimate_default()


@app.route("/api/v1/on-covid-19/xml", methods=["GET"])
def get_estimate_xml():
    req_data = request.get_json()
    res = dumps({"response": estimator(req_data)})
    return res

@app.route("/api/v1/on-covid-19/logs", methods=["GET"])
def get_logs():
    f = open("logs.txt", "r")
    contents = f.read()
    f.close()
    return contents


app.run()