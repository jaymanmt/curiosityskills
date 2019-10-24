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
    
    return render_template("home.html", job_categories = job_categories)

## redirecting form depending on user selections on work-category and type of work experiences
@app.route('/', methods = ['POST'])
def homeredirect():
    experience = request.form.get("experience_type")
    job_category = request.form.get("job_categories")
    job_category_id = job_category[0]
    
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

## route for displaying: create work profile
@app.route('/create-workprofile')
def showcreateprofile():
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
    
    return render_template("create_workprofile.html", job_categories = job_categories, job_levels = job_levels)
    
# route for posting to create work profile  
@app.route('/create-workprofile', methods=["POST"])
def createprofile():
    job_categories = request.form.get("job_categories")
    job_categories_id = job_categories[0]
    job_level = request.form.get("job_level")
    job_level_id = job_level[0]
    salary = request.form.get("salary")
    date = request.form.get("date_created")
    date_format = date.replace("-", "")
    
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql="""
    INSERT INTO work_exp (job_category, job_level, salary, date) VALUES ({},{},{},{})
    """.format(job_categories_id, job_level_id, salary, date_format)
    print(sql)
    cursor.execute(sql)
    connection.commit()
    
    return render_template("choose_exp.html")

if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)