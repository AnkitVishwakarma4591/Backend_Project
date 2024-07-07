# Importing the Flask class from flask module
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# let's create the object of the Flask class
app = Flask(__name__)

# connecting the flask app (server) with SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'  # Adjust this as needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress warning

# creating an object of SQLAlchemy class
database = SQLAlchemy(app)

# writing python class which will be used to insert data into table
class Task(database.Model):
    sno = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.Text, nullable=False)
    enrollment = database.Column(database.Text, nullable=False)
    email = database.Column(database.Text, nullable=False)

# Initialize database and create tables if not exist
with app.app_context():
    database.create_all()

# First route: Index route/default route
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # fetch the values of title and description
        st_name = request.form.get('stu_name')
        st_enrollment = request.form.get('stu_enrollment')
        st_email = request.form.get('stu_email')

        # add it to the database
        task = Task(name=st_name, enrollment=st_enrollment, email=st_email)
        database.session.add(task)
        database.session.commit()

        # returning the home.html page
        return redirect('/')
    else:
        allTasks = Task.query.all()
        return render_template('home.html', allTasks=allTasks)

@app.route('/delete')
def delete():
    serial_number = request.args.get('sno')
    task = Task.query.filter_by(sno=serial_number).first()

    if task:
        database.session.delete(task)
        database.session.commit()

    # Reassign serial numbers
    allTasks = Task.query.order_by(Task.sno).all()
    for index, task in enumerate(allTasks, start=1):
        task.sno = index
    database.session.commit()

    return redirect("/")



@app.route("/update", methods=["GET", "POST"])
def update():
    serial_number = request.args.get('sno')
    reqTask = Task.query.filter_by(sno=serial_number).first()

    if request.method == "POST":
        updatedname = request.form.get('stu_name')
        updatedenrollment = request.form.get('stu_enrollment')
        updatedemail = request.form.get('stu_email')

        reqTask.name = updatedname
        reqTask.enrollment = updatedenrollment
        reqTask.email = updatedemail

        database.session.commit()

        return redirect('/')
    else:
        return render_template('update.html', reqTask=reqTask)

# let's run the flask application
if __name__ == "__main__":
    app.run(debug=True)
