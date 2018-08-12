"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, session

import hackbright

app = Flask(__name__)

app.secret_key = "Super Secret Secret Key"


@app.route("/student")
def get_student():
    """Show information about a student."""

    if session == None:
        github = request.args.get('github')
        first, last, github = hackbright.get_student_by_github(github)

    else:
        github = session["added_student"]['github']
        first = session["added_student"]['first_name']
        last = session["added_student"]['last_name']

    html = render_template('student_info.html', first=first, last=last, github=github)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

#step two

@app.route("/student_add", methods=['POST'])
def student_add():
    """Add new student."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    session["added_student"] = {'first_name': first_name,
                               'last_name': last_name,
                               'github': github}

    html = render_template('student_add.html', first=first_name, last=last_name, github=github)

    return html

@app.route("/student-add-form")
def get_new_student_form():
    """Show form for adding a student."""

    return render_template("student_add_form.html")

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
