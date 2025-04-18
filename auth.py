from fastapi import FastAPI, Depends, HTTPException, Body
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer  

from fastapi.middleware.cors import CORSMiddleware

 
app = FastAPI()


 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],  
)

 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

 #dol 3shan n push on github bdel el key => .ev
import os
from dotenv import load_dotenv 
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

 
class User(BaseModel):
    username: str
    email: str

class UserInDB(User):
    hashed_password: str

 
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

 
fake_users_db = {}

 
def get_password_hash(password: str):
    return pwd_context.hash(password)

 
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

 
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

 
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

 
def get_user_from_db(username: str):
    return fake_users_db.get(username)

 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

 
@app.post("/signup")
def signup(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    fake_users_db[user.username] = UserInDB(username=user.username, email=user.email, hashed_password=hashed_password)
    return {"msg": "User created successfully"}

 
@app.post("/login")
def login(user: UserCreate):
    db_user = get_user_from_db(user.username)
    if db_user is None or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

 
@app.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):   
    token_data = verify_token(token)  
    return {"msg": "Welcome to the protected endpoint!", "token_data": token_data}
