from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/menu"
app.config["TEMPLATES_AUTO_RELOAD"] = True

db =   SQLAlchemy(app)

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    item = db.Column('ITEM', db.String(25), nullable=False)
    category = db.Column('Category', db.String(25), nullable=False)
    note = db.Column('Note', db.String(40))

@app.route('/')
def main(): 
    return render_template('index.html')


@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        item = request.form["item"]
        category = request.form["category"]
        note = request.form.get("note")

        new_item = Menu(item=item, category=category, note=note)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("order"))

    menu = Menu.query.all()

    return render_template("order.html", menu=menu)

@app.route("/kitchen", methods=["GET" , "POST"])
def menu():
    menu = Menu.query.all()
    return render_template("kitchen.html" , menu=menu)

@app.route("/delete/<int:item_id>" , methods=['GET','POST'])
def delete(item_id):
    item_to_delete = Menu.query.get(item_id)  # Get item by ID
    if item_to_delete:
        db.session.delete(item_to_delete)
        db.session.commit()
    return redirect(url_for("menu"))  