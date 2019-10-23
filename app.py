from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

app = Flask(__name__)

##job categories is to the credit of recruiter.com, refer to readme file for more details
job_categories = ["Agriculture, Food and Natural Resources", "Architecture and Construction", "Arts, Audio/Video Technology and Communications",  "Business Management and Administration", "Education and Training", "Finance", "Government and Public Administration", "Health Science", "Hospitality and Tourism", "Human Services", "Information Technology", "Law, Public Safety, Corrections and Security", "Manufacturing", "Marketing, Sales and Service", "Science, Technology, Engineering and Mathematics", "Transportation, Distribution and Logistics"]

##referred types of job levels by bizfluent website, refer to readme file for more details
job_levels = ["Intern", "Junior-Level", "Entry-Level", "Intermediate", "First-level Management", "Upper-Management","Top-Level Management"]

@app.route('/')
def home():
    return render_template("home.html", job_categories = job_categories)


if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)