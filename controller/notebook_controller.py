from controller import app, AlchemyEncoder
from flask import request
from model import db
from model.notebook import Notebook
import json

@app.route("/api/notebook", methods=["GET"])
def get_notebooks():
    notes = db.session.query(Notebook).all()
    print(notes)
    return json.dumps(notes, cls=AlchemyEncoder)

@app.route("/api/notebook", methods=["POST"])
def add_notebook():
    notebook_data = request.json
    notebook = Notebook(**notebook_data)
    db.session.add(notebook)
    db.session.commit()
    return json.dumps(notebook, cls = AlchemyEncoder)

@app.route("/api/notebook", methods=["PATCH"])
def update_notebook():
    notebook_data = request.json
    notebook = db.session.query(Notebook).filter(Notebook.id == notebook_data["id"]).first()
    notebook.title = notebook_data["title"]
    db.session.commit()
    return json.dumps(notebook, cls=AlchemyEncoder)

@app.route("/api/notebook/<notebook_id>", methods=["DELETE"])
def delete_notebook(notebook_id):
    notebook = db.session.query(Notebook).filter(Notebook.id == notebook_id).first()
    db.session.delete(notebook)
    db.session.commit()
    return "deleted"
