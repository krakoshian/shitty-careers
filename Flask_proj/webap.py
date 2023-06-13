from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [{

    'id': 1,
    'Title': "shitty analytics",
    'location' : "Ankara, Türkiye",
    'salary' : "TL 20K"
},
{

    'id': 2,
    'Title': "shitty scientist",
    'location' : "Istanbul, Türkiye",
    'salary' : "TL 30K"},
{

    'id': 3,
    'Title': "shitty engineer",
    'location' : "İzmir, Türkiye",
    },

{

    'id': 4,
    'Title': "shitty manager",
    'location' : "Remote",
    'salary' : "$ 4K"}

]


@app.route("/")
def heyo():
    return render_template('home.html',jobs = JOBS, company_name = "Shitty")

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/learn")
def learn():
    return render_template('learn.html')
@app.route("/events")
def events():
    return render_template('events.html')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)