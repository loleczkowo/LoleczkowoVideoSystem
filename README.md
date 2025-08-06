## Setup Note

Make sure to place a `backend.env` file in the `backend/` directory.  
It should contain `pg_dsn=`.


## How to run the backend:
- go to `backend`
- make a venv `python3 -m venv venv`
- open the venv `source venv/bin/activate`
- update the venv `pip install --upgrade pip` `pip install -r requirements.txt`
- within the venv **WHILE BEING IN `backend`** run `uvicorn main:app --reload`