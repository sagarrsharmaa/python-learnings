"""
Notes API — Phase 1 project starter.
Run from the backend/ folder:   uvicorn main:app --reload
Then open:                       http://localhost:8000/docs
"""

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# # The app object. `uvicorn main:app` looks for this exact name `app`.
# app = FastAPI(title="Notes API")


# # A Pydantic model = the shape of the data coming IN (like a Java DTO + Bean Validation).
# # FastAPI reads these type hints to validate requests automatically.
# class NoteIn(BaseModel):
#     title: str
#     body: str


# # What we send BACK (includes the id we assigned).
# class Note(NoteIn):
#     id: int


# # A fake in-memory "database" for now — just a list. (Real DB comes later.)
# notes: list[Note] = []
# next_id = 1


# # GET / — a health check / hello endpoint.
# @app.get("/")
# def read_root():
#     return {"message": "Notes API is running"}


# # GET /notes — list all notes.
# @app.get("/notes")
# def list_notes() -> list[Note]:
#     return notes


# # POST /notes — create a note. FastAPI validates the body against NoteIn.
# @app.post("/notes")
# def create_note(note_in: NoteIn) -> Note:
#     global next_id
#     note = Note(id=next_id, title=note_in.title, body=note_in.body)
#     notes.append(note)
#     next_id += 1
#     return note


# # GET /notes/{note_id} — fetch one note by id, or 404 if it doesn't exist.
# @app.get("/notes/{note_id}")
# def get_note(note_id: int) -> Note:
#     for note in notes:
#         if note.id == note_id:
#             return note
#     raise HTTPException(status_code=404, detail="Note not found")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# # The app object. `uvicorn main:app` looks for this exact name `app`.
app = FastAPI(title="Notes API")


# # A Pydantic model = the shape of the data coming IN (like a Java DTO + Bean Validation).
# # FastAPI reads these type hints to validate requests automatically.
class NoteIn(BaseModel):
    title: str
    body: str


# # What we send BACK (includes the id we assigned).
class Note(NoteIn):
    id: int


# # A fake in-memory "database" for now — just a list. (Real DB comes later.)
notes: list[Note] = []
next_id = 1


# # GET /notes — list all notes.
@app.get("/notes")
def list_notes() -> list[Note]:
    return notes


# # POST /notes — create a note. FastAPI validates the body against NoteIn.
@app.post("/notes")
def create_note(note_in: NoteIn) -> Note:
    global next_id
    note = Note(id=next_id, title=note_in.title, body=note_in.body)
    notes.append(note)
    next_id += 1
    return note


# # GET /notes/{note_id} — fetch one note by id, or 404 if it doesn't exist.
@app.get("/notes/{note_id}")
def get_note(note_id: int) -> Note:
    for note in notes:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")


# did we use sgi in this code , THE REAL TERM IS ASGI , ASYNCHRONOUS SERVER GATEWAY INTERFACE
# AND YES WE ARE USING IT RN THE UVICORN IS SGI JUST TLIKE TOMCAT IN JAVA OR SERVLET , AND FASTAPI IS EQUIVALENT TO SPRING BOOT
