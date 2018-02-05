import os

from flask import redirect
from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "addressBook.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Contact(db.Model):
    name = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)
    address = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    state = db.Column(db.String(20), unique=False, nullable=False)
    zip = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "<Name: %r>".format(self.name)

@app.route("/", methods=["GET", "POST"])
def home():
    contacts = None
    if request.form:
        try:
            contact = Contact(
                name=request.form.get("name"),
                address=request.form.get("address"),
                city=request.form.get("city"),
                state=request.form.get("state"),
                zip=request.form.get("zip"))
            db.session.add(contact)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Failed to add contact")
            print(e)
    contacts = Contact.query.all()
    return render_template("home.html",contacts=contacts)

@app.route("/update", methods=["POST"])
def update():
    newname = request.form.get("newname")
    oldname = request.form.get("oldname")
    newaddress = request.form.get("newaddress")
    oldaddress = request.form.get("oldaddress")
    newcity = request.form.get("newcity")
    oldcity = request.form.get("oldcity")
    newstate = request.form.get("newstate")
    oldstate = request.form.get("oldstate")
    newzip = request.form.get("newzip")
    oldzip = request.form.get("oldzip")
    contact = Contact.query.filter_by(name=oldname).first()
    contact.name = newname
    contact.address = newaddress
    contact.city = newcity
    contact.state = newstate
    contact.zip = newzip
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    contact = Contact.query.filter_by(name=name).first()
    db.session.delete(contact)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
