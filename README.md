# Python Katas API

FastAPI application for practicing Python katas behind HTTP endpoints.

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `POST` | `/dictionary/new-entry` | Add a word to the dictionary |
| `GET` | `/dictionary/look/{word}` | Look up the definition of a word |
| `POST` | `/shopping/total` | Calculate the total of a shopping cart |
| `POST` | `/words/concatenate` | Concatenate a list of words |

## Usage examples

**Add a word:**
```bash
curl -X POST http://localhost:8000/dictionary/new-entry \
  -H "Content-Type: application/json" \
  -d '{"word": "ephemeral", "definition": "lasting a very short time"}'
```

**Look up a word:**
```bash
curl http://localhost:8000/dictionary/look/ephemeral
```

**Calculate shopping total:**
```bash
curl -X POST http://localhost:8000/shopping/total \
  -H "Content-Type: application/json" \
  -d '{"costs": {"apple": 1.50, "bread": 2.00}, "items": ["apple", "apple", "bread"], "tax": 0.10}'
```

**Concatenate words:**
```bash
curl -X POST http://localhost:8000/words/concatenate \
  -H "Content-Type: application/json" \
  -d '{"words": ["hello", "world", "foo"]}'
```

## Project structure

```text
api.py
src/
tests/
.github/
  workflows/
    ci.yml
Dockerfile
requirements.txt
README.md
```

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn api:app --reload
```

The API documentation is available at `http://localhost:8000/docs`.

## Run with Docker

```bash
docker build -t python-katas .
docker run -p 8000:8000 python-katas
```

## Tests

```bash
pytest
ruff check .
```

## CI

The GitHub Actions workflow in `.github/workflows/ci.yml` runs on pushes to `main` and `dev`, and on pull requests. It runs pytest, checks code style with ruff, and performs a uvicorn smoke test.
