## Setup Note

- go to `backend`
- make a `backend.env`  
It should contain `pg_dsn=`.
- make a venv `python3 -m venv venv`


## How to run the backend:
- go to `backend`
- open the venv `source venv/bin/activate`
- update the venv `pip install --upgrade pip` `pip install -r requirements.txt`
- within the venv **WHILE BEING IN `backend`** run `uvicorn main:app --reload`