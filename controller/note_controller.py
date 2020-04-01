from controller import app, AlchemyEncoder
from flask import request
from model import db
from model.note import Note
import json

@app.route("/api/note", methods=["GET"])
def get_notes():
    notes = db.session.query(Note).all()
    print(notes)
    return json.dumps(notes, cls=AlchemyEncoder)

@app.route("/api/note/<notebook_id>", methods=["GET"])
def get_note_by_id(notebook_id):
    notes = db.session.query(Note).filter(Note.notebook_id == notebook_id).all()
    return json.dumps(notes, cls=AlchemyEncoder)

@app.route("/api/note", methods=["POST"])
def add_note():
    note_data = request.json
    note = Note(**note_data)
    db.session.add(note)
    db.session.commit()
    return json.dumps(note, cls = AlchemyEncoder)

@app.route("/api/note", methods=["PATCH"])
def update_note():
    note_data = request.json
    note = db.session.query(Note).filter(Note.id == note_data["id"]).first()
    note.text = note_data["text"]
    db.session.commit()
    return json.dumps(note, cls=AlchemyEncoder)

@app.route("/api/note/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = db.session.query(Note).filter(Note.id == note_id).first()
    db.session.delete(note)
    db.session.commit()
    return "deleted"
