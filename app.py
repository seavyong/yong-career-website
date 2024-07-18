from flask import Flask, render_template, jsonify

app = Flask(__name__)
Jobs = [
    {
        'id' : 1,
        'tittle': 'Data Analyst',
        'location': 'Bengaluru, India',
         'salary': '1000$'
    },
    {
        'id' : 2,
        'tittle': 'Data Science',
        'location': 'Phnom Penh, Cambodia',
        'salary': '1000$'
    }
]
@app.route("/")
def hello_world():
    return render_template('home.html', jobs = Jobs, company_name = 'Yong')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)