"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, flash, redirect, session

import hackbright

app = Flask(__name__)

app.secret_key = 'this-should-be-something-unguessable'

# @app.route("/")
# def show_homepage():
#     return render_template("homepage.html")

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("student-add.html", github=github)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades_list = hackbright.get_grades_by_github(github)

    # return "{} is the GitHub account for {} {}".format(github, first, last)

    html = render_template("student_info.html", first=first, last=last, github=github,
                            rows=grades_list)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
