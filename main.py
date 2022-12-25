from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
main = Flask(__name__)

@main.route("/")
def hello_jovian():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs = jobs, company_name = 'Jovian')

@main.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@main.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  return jsonify(job)
  
if __name__ == "__main__":
  main.run(host='0.0.0.0', debug=True)