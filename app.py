from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

app = Flask(__name__)

def connect():
    connection = pymysql.connect(host="localhost",
    user="admini",
    password="71f08h3fnduweyg7",
    database="curiosityskills")
    return connection
    
## job categories is to the credit of recruiter.com, refer to readme file for more details
job_cat = ["Agriculture, Food and Natural Resources", "Architecture and Construction", "Arts, AudioVideo Technology and Communications",  "Business Management and Administration", "Education and Training", "Finance", "Government and Public Administration", "Health Science", "Hospitality and Tourism", "Human Services", "Information Technology", "Law, Public Safety, Corrections and Security", "Manufacturing", "Marketing, Sales and Service", "Science, Technology, Engineering and Mathematics", "Transportation, Distribution and Logistics"]

##referred types of job levels by bizfluent website, refer to readme file for more details
job_l = ["Intern", "Junior-Level", "Entry-Level", "Intermediate", "First-level Management", "Upper-Management","Top-Level Management"]

## display home route for basic search
@app.route('/')
def home():
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql="""
    SELECT * FROM job_category_list
    """
    cursor.execute(sql)
    job_categories = cursor.fetchall()
    
    sql="""
    SELECT * FROM job_level_list
    """
    cursor.execute(sql)
    job_levels = cursor.fetchall()
    
    return render_template("home.html", job_categories = job_categories)

## redirecting form depending on user selections
@app.route('/', methods = ['POST'])
def homeredirect():
    job_category = request.form.get("job_categories")
    job_category_id = job_category[0]
    experience = request.form.get("experience_type")
    if experience == 'all_exp':
        return redirect("/all-experiences/{}".format(job_category_id))
    elif experience == 'client_exp':
        return render_template("search_client_exp.html")
    elif experience == 'edu_exp':
        return render_template("search_edu_exp.html")
    elif experience == 'salary_only':
        return render_template('salary_compare.html')
    else:
        return render_template("oops.html")

## the route if user chose the 'all experiences' option
@app.route('/all-experiences/<job_category_id>')
def showall(job_category_id):
    
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = """
    SELECT * FROM work_exp
    INNER JOIN client_exp ON work_exp.id = client_exp.id
    INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    WHERE work_exp.job_category = {}
    """.format(job_category_id)
    cursor.execute(sql)
    client_exp_from_chosen_cat = cursor.fetchall()

    sql = """
    SELECT * FROM work_exp
    INNER JOIN edu_exp ON work_exp.id = edu_exp.id
    INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    WHERE work_exp.job_category = {}
    """.format(job_category_id)

    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    edu_exp_from_chosen_cat = cursor.fetchall()
    print(client_exp_from_chosen_cat)
    print(edu_exp_from_chosen_cat)
    
    return render_template("all_exp.html", client_results = client_exp_from_chosen_cat, edu_results = edu_exp_from_chosen_cat)

## route for customising client experiences
# @app.route('/client_exp')


if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)