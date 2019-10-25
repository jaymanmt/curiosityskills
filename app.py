from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

app = Flask(__name__)

def connect():
    connection = pymysql.connect(host="localhost",
    user="admini",
    password=os.environ["MYSQLPW"],
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
@app.route('/create-client-experience')
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
    
    sql= """
    SELECT * FROM age_range_list
    """
    cursor.execute(sql)
    age_ranges = cursor.fetchall()
    
    sql= """
    SELECT * FROM gender_list
    """
    cursor.execute(sql)
    gender_select = cursor.fetchall()
    
    return render_template("create_work_client.html", job_categories = job_categories, job_levels = job_levels, gender_select = gender_select, age_ranges = age_ranges)
    
## route for user to create work profile + client exp on database
@app.route('/create-client-experience', methods=["POST"])
def createclientexp():
    job_categories = request.form.get("job_categories")
    job_categories_id = job_categories[0]
    job_level = request.form.get("job_level")
    job_level_id = job_level[0]
    salary = request.form.get("salary")
    
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql="""
    INSERT INTO work_exp (job_category, job_level, salary) VALUES ({},{},{})
    """.format(job_categories_id, job_level_id, salary)
    print(sql)
    cursor.execute(sql)
    
    last_id_work = cursor.lastrowid 
    
    connection.commit()
    
    print(last_id_work)
    
    title = request.form.get("client_exp_title")
    details = request.form.get("client_exp_details")
    date = request.form.get("date_created")
    date_format = date.replace("-", "")
    
    sql= """
    INSERT INTO client_exp(title, details, date, work_fk) VALUES ('{}', '{}', {}, {})
    """.format(title, details, date_format, last_id_work)
    cursor.execute(sql)
    last_id_client_exp = cursor.lastrowid
    connection.commit()
    
    age_group = request.form.get("client_age_range")
    gender = request.form.get("client_gender")
    
    sql="""
    INSERT INTO age_range(age_group) VALUES ('{}')
    """.format(age_group)
    cursor.execute(sql)
    last_id_age_range = cursor.lastrowid
    connection.commit()
    
    sql = """
    INSERT INTO client_age(client_age, age_age) VALUES ({},{})
    """.format(last_id_client_exp, last_id_age_range)
    cursor.execute(sql)
    connection.commit()
    
    return redirect('/')
    
## route to display from for creating education experience 
@app.route("/create-edu-experience")
def create_eduexp():
    
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    
    return render_template("create_work_edu.html")



## route for user to create education experience onto database



if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)