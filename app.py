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
    WHERE work_exp.job_category = {}
    """.format(job_cat_id)
    cursor.execute(sql)
    all_e_exp_unselect = cursor.fetchall()
    
    return render_template('all_exp_unselect.html', all_c_exp_unselect = all_c_exp_unselect, all_e_exp_unselect = all_e_exp_unselect)
    
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
    WHERE work_exp.job_level = {}
    """.format(job_level_id)
    cursor.execute(sql)
    all_e_exp_unselect = cursor.fetchall()
    return render_template('all_exp_unselect.html', all_c_exp_unselect = all_c_exp_unselect, all_e_exp_unselect = all_e_exp_unselect)
    
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
        WHERE work_exp.job_category = {} and work_exp.job_level = {}
        """.format(job_cat_id, job_level_id)
        cursor.execute(sql)
        all_e_exp_unselect = cursor.fetchall()
        return render_template("all_exp_unselect.html", all_c_exp_unselect = all_c_exp_unselect, all_e_exp_unselect = all_e_exp_unselect)
        
## search possbilities for user choosing to compare salary - from dropdown, user choose none, job cat only, job level only, or both
    elif exp_type == 'salary':
        if job_level_id == '-' and job_cat_id == '-':
            connection = connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            SELECT * FROM work_exp
            INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
            INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
            """
            cursor.execute(sql)
            salaries = cursor.fetchall()
            return render_template("salary_all.html", salaries = salaries)
        elif job_level_id == '-':
            connection = connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            SELECT * FROM work_exp
            INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
            INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
            WHERE job_category = {}
            """.format(job_cat_id)
            cursor.execute(sql)
            salaries = cursor.fetchall()
            return render_template("salary_all.html", salaries = salaries)
        elif job_cat_id == '-':
            connection = connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            SELECT * FROM work_exp
            INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
            INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
            WHERE job_level = {}
            """.format(job_level_id)
            cursor.execute(sql)
            salaries = cursor.fetchall()
            return render_template("salary_all.html", salaries = salaries)
        else:
            connection = connect()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            SELECT * FROM work_exp
            INNER JOIN job_category_list ON work_exp.job_category = job_category_list.id
            INNER JOIN job_level_list ON work_exp.job_level = job_level_list.id
            WHERE job_category = {} and job_level = {}
            """.format(job_cat_id, job_level_id)
            cursor.execute(sql)
            salaries = cursor.fetchall()
            return render_template('salary_all.html', salaries = salaries)
    else:
        return render_template('oops.html')

##route where user chose to view details of a specific entry in client experiences
@app.route('/view-c-exp/<c_exp_id>')
def show_c_exp(c_exp_id):
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
    WHERE work_exp.id = {}
    """.format(c_exp_id)
    cursor.execute(sql)
    displayclientexp = cursor.fetchall()
    return render_template('show_c_exp.html', displayclientexp = displayclientexp)
    
##route where user chose to view details of a specific entry in education experiences
@app.route('/view-e-exp/<e_exp_id>')
def show_e_exp(e_exp_id):
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
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
        WHERE work_exp.id = {}
    """.format(e_exp_id)
    cursor.execute(sql)
    displayeduexp = cursor.fetchall()
    return render_template('show_e_exp.html', displayeduexp = displayeduexp)
    
## route to display edit client experience template, allow users to see previous entry to make adjustments easier
@app.route('/edit-client-exp/<c_exp_id>')
def show_edit_client(c_exp_id):
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
    WHERE work_exp.id = {}
    """.format(c_exp_id)
    cursor.execute(sql)
    displayclientexp = cursor.fetchall()
    
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
    
    return render_template('edit_c_exp.html', displayclientexp = displayclientexp, job_categories = job_categories, job_levels = job_levels, gender_select = gender_select, age_ranges = age_ranges)

## route to submit form for editing client experience
@app.route('/edit-client-exp/<c_exp_id>', methods = ['POST'])
def edit_client(c_exp_id):

    job_categories = request.form.get("job_categories")
    job_level = request.form.get("job_level")
    salary = request.form.get("salary")
    title = request.form.get("client_exp_title")
    details = request.form.get("client_exp_details")
    date = request.form.get("date_created")
    date_format = date.replace("-", "")
    gender = request.form.get("client_gender")
    age_group = request.form.get("client_age_range")
    
    connection = connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql="""
    UPDATE work_exp SET job_category = {}, job_level= {}, salary = {}
    WHERE id = {}
    """.format(job_categories[0], job_level[0], salary, c_exp_id)
    cursor.execute(sql)
    connection.commit()
    
    sql="""
    UPDATE client_exp SET title = "{}", details = "{}", date= {}, gender_fk= {}
    WHERE work_fk = {}
    """.format(title, details, date_format, gender[0], c_exp_id)
    cursor.execute(sql)
    connection.commit()
    sql = """
    UPDATE client_age 
    INNER JOIN client_exp ON client_exp.id = client_age.client_age
    SET client_age.age_age = {}
    WHERE client_exp.work_fk = {}
    """.format(age_group[0], c_exp_id)
    print(sql)
    cursor.execute(sql)
    
    connection.commit()
    
    return redirect("/view-c-exp/{}".format(c_exp_id))
    


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
    INSERT INTO client_exp(title, details, date, work_fk, gender_fk) VALUES ("{}", "{}", {}, {}, {})
    """.format(title, details, date_format, last_id_work, gender[0])
    cursor.execute(sql)
    last_id_client_exp = cursor.lastrowid

## insert age separately from the rest due to separate client_exp and edu_exp tables linking to age_range table
    age_group = request.form.get("client_age_range")
    
    sql = """
    INSERT INTO client_age(client_age, age_age) VALUES ({},{})
    """.format(last_id_client_exp, age_group[0])
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
    INSERT INTO edu_exp(title, details, date, work_fk, role_fk, level_fk, topic_fk, institute_fk) VALUES ("{}", "{}", {}, {}, {}, {}, {}, {})
    """.format(title, details, date_format, last_id_work, role[0], edulevel[0], subject[0], institute[0])

    cursor.execute(sql)
    
    last_id_edu = cursor.lastrowid 
    
    connection.commit()
    
## insert age separately from the rest due to separate client_exp and edu_exp tables linking to age_range table
    
    age_group = request.form.get('edu_age_range')
    
    sql="""
    INSERT INTO edu_age(edu_age, age_age) VALUES ({},{})
    """.format(last_id_edu, age_group[0])
    
    cursor.execute(sql)
    connection.commit()
    
    
    return redirect('/')

if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)