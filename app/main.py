from fastapi import FastAPI
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app.database import engine
import app.models as models
from app.config import settings
from app.routers import products, users, auth
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://www.google.com"]

#Handle CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', 
                                user='postgres', password='password', 
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connection stablished with PostgreSQL")
        break
    except Exception as error:
        print(f"Error {error}")
        time.sleep(3000)



app.include_router(products.router)
app.include_router(users.router)
app.include_router(auth.router)