from flask import Flask, render_template,jsonify
from database import load_jobs_from_db
app = Flask(__name__) #creating an object of the class Flask
  
@app.route("/") 
#creating a function 
def hello_world():
    return render_template('home.html', jobs=load_jobs_from_db())
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_jobs_from_db())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug = True)