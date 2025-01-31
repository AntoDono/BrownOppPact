# Brown Opp Pact
A full-stack application in which user answers a series of question to find someone with the exact opposite qualities as them.

## Setup Backend
```bash
cd backend
python -m venv venv
```

### Setup environment
```bash
source ./venv/bin/activate # if you are on linux
.\venv\Scripts\activate # if you are on windows
```

### Install dependencies
```bash
pip install poetry
poetry install
```

Then, create a .env file with the following parameters:
```
LLM_ENDPOINT="...."
```
**Note**: The llm endpoint might take different parameters, adjust in the code as you see fit.

## Setup Frontend
```bash
cd frontend
npm i
```

Then, create a .env file with the following parameters:
```
BACKEND_URL="...."
```