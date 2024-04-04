from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db_with_id

app = Flask(__name__)  # creating an object of the class Flask

@app.route("/")
def hello_world():
      return render_template('home.html', jobs=load_jobs_from_db())

@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_jobs_from_db())

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db_with_id(id)  
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)