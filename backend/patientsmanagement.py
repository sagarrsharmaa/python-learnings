import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from typing import Optional


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


app = FastAPI(title="PATIENT MANAGEMENT APP")


@app.get("/about")
def about():
    return {"message": "A fully functional fast api"}


@app.get("/patient")
def view():
    data = load_data()

    return data


@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    data = load_data()

    for patient in data:
        if patient["id"] == patient_id:
            return patient
    raise HTTPException(status_code=404, detail=f"patient '{patient_id}' not found")


@app.get("/sort")
def sortview(sort_by: str, order: str = "asc"):
    valid_fields = ["age", "height_m", "weight_kg", "bmi"]
    data = load_data()

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. choose from {valid_fields}",
        )
    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Use 'asc' or 'desc'",
        )
    sorted_data = sorted(
        data,
        key=lambda patient: patient[sort_by],
        reverse=(order == "desc"),
    )
    return sorted_data


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=2)


class Patient(BaseModel):
    id: str
    name: str
    city: str
    age: int
    gender: str
    height_m: float
    weight_kg: float
    bmi: float
    verdict: str


@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()

    # reject if already exists
    for existing in data:
        if existing["id"] == patient.id:
            raise HTTPException(
                status_code=400, detail=f"patient '{patient.id}' already exists"
            )

    data.append(patient.model_dump())
    save_data(data)
    return {"message": "patient created", "patient": patient}


@app.delete("/patient/{patient_id}")
def del_patient(patient_id: str):
    data = load_data()
    for existing in data:
        if existing["id"] == patient_id:
            data.remove(existing)
            save_data(data)
            return {"message": "patient deleted", "patient": patient_id}
    raise HTTPException(status_code=404, detail="patient not found")


class patientupdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    height_m: Optional[float] = None
    weight_kg: Optional[float] = None
    bmi: Optional[float] = None
    verdict: Optional[str] = None


@app.put("/patient/{patient_id}")
def update_patient(patient_id: str, patient_update: patientupdate):
    data = load_data()

    for existing in data:
        if existing["id"] == patient_id:
            updates = patient_update.model_dump(exclude_unset=True)
            existing.update(updates)
            save_data(data)
            return {"message": "patient updated", "patient": existing}
    raise HTTPException(status_code=404, detail=f"patient not found")


# @app.get("/patient/{patient_id}")
# def get_patient(patient_id: str):
#     data = load_data()

#     for patient in data:
#         if patient["id"] == patient_id:
#             return patient

#     raise HTTPException(status_code=404, detail=f"Patient '{patient_id}' not found")
