# python-learnings

Hands-on projects from my transition into AI engineering (coming from Java backend). Each piece is built by writing the code myself, not copy-pasting tutorials.

## Projects

| Path | What it is |
|------|------------|
| [`backend/patientsmanagement.py`](backend/patientsmanagement.py) | **Patient Management API** — a full CRUD REST API in FastAPI (documented below) |
| [`backend/main.py`](backend/main.py) | Notes API (FastAPI) |
| [`backend/callanllm.py`](backend/callanllm.py) | CLI chatbot talking to an LLM over an API, with conversation memory |

---

## Patient Management API

A FastAPI service exposing full CRUD over a JSON file of patient records. Demonstrates path params, query params, Pydantic request-body validation, partial updates, and proper HTTP error codes.

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi "uvicorn[standard]" pytest httpx
```

### Run

```bash
cd backend
uvicorn patientsmanagement:app --reload
```

Then open the interactive API docs at **http://127.0.0.1:8000/docs**.

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/patient` | List all patients |
| `GET` | `/patient/{patient_id}` | Get one patient by id (404 if missing) |
| `GET` | `/sort?sort_by=<field>&order=<asc\|desc>` | Sort by `age`, `bmi`, `height_m`, or `weight_kg` |
| `POST` | `/create` | Create a patient (400 if id already exists) |
| `PUT` | `/patient/{patient_id}` | Partial update — send only the fields you want to change |
| `DELETE` | `/patient/{patient_id}` | Delete a patient (404 if missing) |

### Example

```bash
# create
curl -X POST http://127.0.0.1:8000/create \
  -H "Content-Type: application/json" \
  -d '{"id":"p006","name":"Sarah Connor","city":"Seattle","age":35,
       "gender":"Female","height_m":1.70,"weight_kg":65.0,
       "bmi":22.5,"verdict":"Normal weight"}'

# partial update — only the city changes
curl -X PUT http://127.0.0.1:8000/patient/p006 \
  -H "Content-Type: application/json" \
  -d '{"city":"Boston"}'
```

### Data model

Each patient record (`backend/patients.json`):

```json
{
  "id": "p001",
  "name": "John Doe",
  "city": "New York",
  "age": 40,
  "gender": "Male",
  "height_m": 1.75,
  "weight_kg": 72.5,
  "bmi": 23.7,
  "verdict": "Normal weight"
}
```

### Tests

```bash
cd backend
pytest
```
