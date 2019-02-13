from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/welcome/<string:student_name>')
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

@app.route('/roster/<int:grade_view>')
def roster(grade_view):
    class_roster = [("John", 88, "Freshman"), ("Herald", 92, "Junior"), ("Ann", 100, "Senior"), ("Peter", 85, "Sophomore"), ("Mary", 95, "Junior"), ("Jerry", 76, "Freshman"), ("Justin", 81, "Senior")]
    if (grade_view==1):
        return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)
    elif (grade_view==2):
        return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)
    else:
        return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)


if __name__ == "__main__":
    app.run()
