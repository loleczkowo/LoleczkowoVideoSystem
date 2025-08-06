## Setup Note

Make sure to place a `backend.env` file in the `backend/` directory.  
It should contain `pg_dsn=`.


## How to run the backend:
use `uvicorn backend.main:app --reload`