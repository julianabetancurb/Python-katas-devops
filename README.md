# Python Katas API

FastAPI deployed on AWS Lambda with API Gateway. A DevOps and cloud deployment practice project.

## Live API

Base URL:
```
https://<api-id>.execute-api.<region>.amazonaws.com/prod
```

Interactive documentation:
```
https://<api-id>.execute-api.<region>.amazonaws.com/prod/docs
```

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
curl -X POST <BASE_URL>/dictionary/new-entry \
  -H "Content-Type: application/json" \
  -d '{"word": "ephemeral", "definition": "lasting a very short time"}'
```

**Look up a word:**
```bash
curl <BASE_URL>/dictionary/look/ephemeral
```

**Calculate shopping total:**
```bash
curl -X POST <BASE_URL>/shopping/total \
  -H "Content-Type: application/json" \
  -d '{"costs": {"apple": 1.50, "bread": 2.00}, "items": ["apple", "apple", "bread"], "tax": 0.10}'
```

**Concatenate words:**
```bash
curl -X POST <BASE_URL>/words/concatenate \
  -H "Content-Type: application/json" \
  -d '{"words": ["hello", "world", "foo"]}'
```

## Project structure

```
├── api.py                  # FastAPI app and endpoints
├── src/
│   ├── dictionary.py       # Dictionary logic
│   ├── costs.py            # Shopping cart logic
│   └── concatenate.py      # Concatenation logic
├── tests/
│   └── test_api.py         # Endpoint tests
├── .github/
│   └── workflows/
│       └── ci-deploy.yml   # CI + automated deploy
├── Dockerfile              # Docker image for local development
├── requirements.txt
└── README.md
```

## Run locally

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Start the API
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000/docs`.

## Run with Docker

```bash
docker build -t python-katas .
docker run -p 8000:8000 python-katas
```

## Tests

```bash
pytest tests/ -v
```


## AWS Architecture

```
Client → API Gateway (HTTP API) → Lambda → FastAPI + Mangum
                                          ↓
                                    CloudWatch Logs
```

- **API Gateway:** receives public HTTPS requests and forwards them to Lambda
- **Lambda:** runs FastAPI using Mangum as the ASGI adapter
- **Mangum:** translates Lambda events into the format FastAPI understands
- **CloudWatch:** automatically stores all logs

## CI/CD

The GitHub Actions pipeline in `.github/workflows/ci-deploy.yml` runs automatically on every push:

**On `dev` branch:**
- Runs tests with pytest
- Checks code style with ruff
- Runs a smoke test against the server

**On `main` branch** (in addition to the above):
- Packages dependencies using the official Lambda Docker image
- Builds the deployment ZIP
- Automatically uploads the code to AWS Lambda

The deploy only runs if all tests pass.

## Required secrets

To enable automatic deploys, configure these secrets in GitHub → Settings → Secrets:

| Secret | Description |
|--------|-------------|
| `AWS_ACCESS_KEY_ID` | Access key for the IAM user with Lambda permissions |
| `AWS_SECRET_ACCESS_KEY` | Secret key for the IAM user |

## AWS resources

| Resource | Description |
|----------|-------------|
| Lambda function | Runs the FastAPI application |
| API Gateway | HTTP API that exposes the public endpoints |
| IAM Role | Execution role with basic Lambda permissions |
| Region | us-east-2 (Ohio) |