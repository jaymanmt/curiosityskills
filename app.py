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
    
    sql="""
    SELECT * FROM job_level_list
    """
    cursor.execute(sql)
    job_levels = cursor.fetchall()
    
    return render_template("home.html", job_categories = job_categories, job_levels = job_levels)

## redirecting form depending on possibilties of user search selections on work-category and type of work experiences
@app.route('/', methods = ['POST'])
def homeredirect():
    job_level = request.form.get("level")
    job_category = request.form.get("job_categories")
    experience = request.form.get("experience_type")
    

    if experience == 'all_exp' and job_level[0] == '-' and job_category[0] == '-':
        return redirect('/all-experiences')
    elif experience == 'all_exp' and job_category[0] == '-':
        return redirect('/all-experiences/{}/{}'.format('any-category', job_level[0]))
    elif experience == 'all_exp' and job_level[0] == '-':
        return redirect('/all-experiences/{}/{}'.format('any-level', job_category[0]))
    else:
        return redirect("/{}/{}/{}".format(job_category[0], job_level[0], experience))

## route: user did not choose any job level or job category but selected for all exp
@app.route('/all-experiences')
def allexpsearch():
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql="""
    SELECT * FROM work_exp
    INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
    INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    INNER JOIN client_exp ON work_exp.id = client_exp.work_fk
    INNER JOIN gender_list ON client_exp.gender_fk = gender_list.id
    INNER JOIN client_age ON client_exp.id = client_age.client_age
    INNER JOIN age_range_list ON client_age.age_age = age_range_list.id
    
    """
    cursor.execute(sql)
    all_c_exp_unselect = cursor.fetchall()
    
    sql="""
    SELECT * FROM work_exp
    INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
    INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    INNER JOIN edu_exp ON work_exp.id = edu_exp.work_fk
    INNER JOIN edu_age ON edu_exp.id = edu_age.edu_age
    INNER JOIN age_range_list ON edu_age.age_age = age_range_list.id
    INNER JOIN edu_role_list ON edu_exp.role_fk = edu_role_list.id
    INNER JOIN edu_level_list ON edu_exp.level_fk = edu_level_list.id
    INNER JOIN edu_institute_list ON edu_exp.institute_fk = edu_institute_list.id
    INNER JOIN topic_list ON edu_exp.topic_fk = topic_list.id
    
    """
    cursor.execute(sql)
    all_e_exp_unselect = cursor.fetchall()
    
    return render_template('all_exp_unselect.html', all_c_exp_unselect = all_c_exp_unselect, all_e_exp_unselect = all_e_exp_unselect)

## route: user did not choose any job level but selected a job category and selected for all exp
@app.route('/all-experiences/any-level/<job_cat_id>')
def catexpsearch(job_cat_id):
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql="""
    SELECT * FROM work_exp
    INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
    INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    INNER JOIN client_exp ON work_exp.id = client_exp.work_fk
    INNER JOIN gender_list ON client_exp.gender_fk = gender_list.id
    INNER JOIN client_age ON client_exp.id = client_age.client_age
    INNER JOIN age_range_list ON client_age.age_age = age_range_list.id
    WHERE work_exp.job_category = {}
    """.format(job_cat_id)
    cursor.execute(sql)
    all_c_exp_select = cursor.fetchall()
    
    sql="""
    SELECT * FROM work_exp
    INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
    INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    INNER JOIN edu_exp ON work_exp.id = edu_exp.work_fk
    INNER JOIN edu_age ON edu_exp.id = edu_age.edu_age
    INNER JOIN age_range_list ON edu_age.age_age = age_range_list.id
    INNER JOIN edu_role_list ON edu_exp.role_fk = edu_role_list.id
    INNER JOIN edu_level_list ON edu_exp.level_fk = edu_level_list.id
    INNER JOIN edu_institute_list ON edu_exp.institute_fk = edu_institute_list.id
    INNER JOIN topic_list ON edu_exp.topic_fk = topic_list.id
    WHERE work_exp.job_category = {}
    """.format(job_cat_id)
    cursor.execute(sql)
    all_e_exp_select = cursor.fetchall()
    
    return render_template('job_cat_all_exp.html', all_c_exp_select = all_c_exp_select, all_e_exp_select = all_e_exp_select)
    
## route: user did not choose any job category but selected a job level and selected for all exp
@app.route('/all-experiences/any-category/<job_level_id>')
def levelexpsearch(job_level_id):
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql="""
    SELECT * FROM work_exp
    INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
    INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    INNER JOIN client_exp ON work_exp.id = client_exp.work_fk
    INNER JOIN gender_list ON client_exp.gender_fk = gender_list.id
    INNER JOIN client_age ON client_exp.id = client_age.client_age
    INNER JOIN age_range_list ON client_age.age_age = age_range_list.id
    WHERE work_exp.job_level = {}
    """.format(job_level_id)
    cursor.execute(sql)
    all_c_exp_select = cursor.fetchall()
    
    sql="""
    SELECT * FROM work_exp
    INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
    INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    INNER JOIN edu_exp ON work_exp.id = edu_exp.work_fk
    INNER JOIN edu_age ON edu_exp.id = edu_age.edu_age
    INNER JOIN age_range_list ON edu_age.age_age = age_range_list.id
    INNER JOIN edu_role_list ON edu_exp.role_fk = edu_role_list.id
    INNER JOIN edu_level_list ON edu_exp.level_fk = edu_level_list.id
    INNER JOIN edu_institute_list ON edu_exp.institute_fk = edu_institute_list.id
    INNER JOIN topic_list ON edu_exp.topic_fk = topic_list.id
    WHERE work_exp.job_level = {}
    """.format(job_level_id)
    cursor.execute(sql)
    all_e_exp_select = cursor.fetchall()
    return render_template('job_level_all_exp.html', all_c_exp_select = all_c_exp_select, all_e_exp_select = all_e_exp_select)
    
## route: user chose an experience, a job category and a job level
@app.route('/<job_cat_id>/<job_level_id>/<exp_type>')
def fullsearch(job_cat_id, job_level_id, exp_type):
    if exp_type == 'all_exp':
        connection = connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql="""
        SELECT * FROM work_exp
        INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
        INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
        INNER JOIN client_exp ON work_exp.id = client_exp.work_fk
        INNER JOIN gender_list ON client_exp.gender_fk = gender_list.id
        INNER JOIN client_age ON client_exp.id = client_age.client_age
        INNER JOIN age_range_list ON client_age.age_age = age_range_list.id
        WHERE work_exp.job_category = {} and work_exp.job_level = {}
        """.format(job_cat_id, job_level_id)
        cursor.execute(sql)
        all_client_exp = cursor.fetchall()
        
        sql="""
        SELECT * FROM work_exp
        INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
        INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
        INNER JOIN edu_exp ON work_exp.id = edu_exp.work_fk
        INNER JOIN edu_age ON edu_exp.id = edu_age.edu_age
        INNER JOIN age_range_list ON edu_age.age_age = age_range_list.id
        INNER JOIN edu_role_list ON edu_exp.role_fk = edu_role_list.id
        INNER JOIN edu_level_list ON edu_exp.level_fk = edu_level_list.id
        INNER JOIN edu_institute_list ON edu_exp.institute_fk = edu_institute_list.id
        INNER JOIN topic_list ON edu_exp.topic_fk = topic_list.id
        WHERE work_exp.job_category = {} and work_exp.job_level = {}
        """.format(job_cat_id, job_level_id)
        cursor.execute(sql)
        all_edu_exp = cursor.fetchall()
        return render_template("all_exp_select.html", all_client_exp = all_client_exp, all_edu_exp = all_edu_exp)
        
    elif exp_type == 'salary':
        if job_level_id == '-' and job_cat_id == '-':
            connection = connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            SELECT * FROM work_exp
            """
            cursor.execute(sql)
            all_salary = cursor.fetchall()
            return render_template("salary_all.html", all_salary = all_salary)
        elif job_level_id == '-':
            connection = connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            SELECT * FROM work_exp WHERE job_category = {}
            """.format(job_cat_id)
            cursor.execute(sql)
            jobcat_salary = cursor.fetchall()
            return render_template("salary_job_cat.html", jobcat_salary = jobcat_salary)
        elif job_cat_id == '-':
            connection = connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            SELECT * FROM work_exp WHERE job_category = {}
            """.format(job_level_id)
            cursor.execute(sql)
            joblevel_salary = cursor.fetchall()
            return render_template("salary_job_level.html", joblevel_salary = joblevel_salary)
        else:
            return render_template('salary_select.html')
    else:
        return render_template('oops.html')

## route: user chose all experiences + 'any' for job-category + 'any' for job levels
@app.route('/all-experiences')
def show_allexp():
    return 'show all experiences'

## route: user chose all experiences and a job-level + 'any' for job category
@app.route('/all-experiences/any-level/<job_category_id>')
def show_allexp_jobcat(job_category_id):
    return 'show all experiences + a selected job category'

## route: user chose all experiences and a job-category + 'any' for job levels
@app.route('/all-experiences/any-category/<job_level_id>')
def showall_joblevel(job_level_id):
    return 'show all experiences + a selected job level'
    
    # connection = connect()
    # cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    # sql = """
    # SELECT * FROM work_exp
    # INNER JOIN client_exp ON work_exp.id = client_exp.id
    # INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    # WHERE work_exp.job_category = {}
    # """.format(job_category_id)
    # cursor.execute(sql)
    # client_exp_from_chosen_cat = cursor.fetchall()

    # sql = """
    # SELECT * FROM work_exp
    # INNER JOIN edu_exp ON work_exp.id = edu_exp.id
    # INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
    # WHERE work_exp.job_category = {}
    # """.format(job_category_id)

    # cursor = connection.cursor(pymysql.cursors.DictCursor)
    # cursor.execute(sql)
    # edu_exp_from_chosen_cat = cursor.fetchall()
    # print(client_exp_from_chosen_cat)
    # print(edu_exp_from_chosen_cat)
    
    # return render_template("all_exp.html", client_results = client_exp_from_chosen_cat, edu_results = edu_exp_from_chosen_cat)

## route to display form for creating client experience 
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
    ## insert into work-profile portion on database
    job_categories = request.form.get("job_categories")
    job_level = request.form.get("job_level")
    salary = request.form.get("salary")
    
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql="""
    INSERT INTO work_exp (job_category, job_level, salary) VALUES ({},{},{})
    """.format(job_categories[0], job_level[0], salary)
    
    cursor.execute(sql)
    
    last_id_work = cursor.lastrowid 
    
    title = request.form.get("client_exp_title")
    details = request.form.get("client_exp_details")
    date = request.form.get("date_created")
    date_format = date.replace("-", "")
    gender = request.form.get("client_gender")
    
    sql= """
    INSERT INTO client_exp(title, details, date, work_fk, gender_fk) VALUES ('{}', '{}', {}, {}, {})
    """.format(title, details, date_format, last_id_work, gender[0])
    cursor.execute(sql)
    last_id_client_exp = cursor.lastrowid

## insert age separately from the rest due to separate client_exp and edu_exp tables linking to age_range table
    age_group = request.form.get("client_age_range")
    
    sql="""
    INSERT INTO age_range_list(age_range_listings) VALUES ('{}')
    """.format(age_group)
    cursor.execute(sql)
    last_id_age_range = cursor.lastrowid
    connection.commit()
    
    sql = """
    INSERT INTO client_age(client_age, age_age) VALUES ({},{})
    """.format(last_id_client_exp, last_id_age_range)
    print(sql)
    cursor.execute(sql)
    
    connection.commit()
    
    return redirect('/')
    
## route to display form for creating education experience 
@app.route("/create-edu-experience")
def display_create_eduexp():
    
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
    SELECT * FROM edu_role_list
    """
    cursor.execute(sql)
    edu_role_select = cursor.fetchall()
    
    sql= """
    SELECT * FROM topic_list
    """
    cursor.execute(sql)
    edu_topics = cursor.fetchall()
    
    sql= """
    SELECT * FROM edu_institute_list
    """
    cursor.execute(sql)
    edu_institute_select = cursor.fetchall()
    
    sql = """
    SELECT * FROM edu_level_list
    """
    cursor.execute(sql)
    edu_level_select = cursor.fetchall()
    
    return render_template("create_work_edu.html", job_categories = job_categories, job_levels = job_levels, age_ranges = age_ranges, edu_role_select = edu_role_select, edu_topics = edu_topics, edu_institute_select = edu_institute_select, edu_level_select = edu_level_select)



## route for user to create work profile + education exp on database
@app.route("/create-edu-experience", methods = ['POST'])
def create_eduexp():
    
## insert into work-profile portion on database
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

    cursor.execute(sql)
    
    last_id_work = cursor.lastrowid 
    
    connection.commit()
    
## insert into rest of edu_exp table
    title = request.form.get("edu_exp_title")
    details = request.form.get("edu_exp_details")
    date = request.form.get("date_created")
    date_format = date.replace("-", "")
    role = request.form.get('edu_role')
    institute = request.form.get('edu_institute')
    edulevel = request.form.get('edu_level')
    subject = request.form.get('edu_subject')
    
    sql = """
    INSERT INTO edu_exp(title, details, date, work_fk, role_fk, level_fk, topic_fk, institute_fk) VALUES ('{}', '{}', {}, {}, {}, {}, {}, {})
    """.format(title, details, date_format, last_id_work, role[0], edulevel[0], subject[0], institute[0])
    cursor.execute(sql)
    
    last_id_edu = cursor.lastrowid 
    
    connection.commit()
    
## insert age separately from the rest due to separate client_exp and edu_exp tables linking to age_range table
    
    age_group = request.form.get('edu_age_range')
    sql="""
    INSERT INTO age_range_list(age_range_listings) VALUES ('{}')
    """.format(age_group)
    cursor.execute(sql)
    last_id_age_range = cursor.lastrowid
    
    sql="""
    INSERT INTO edu_age(edu_age, age_age) VALUES ({}, {})
    """.format(last_id_edu, last_id_age_range)
    
    cursor.execute(sql)
    connection.commit()
    
    
    return redirect('/')

if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)