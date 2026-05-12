from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = '3bba4b176f9a80420c6dd6636e97ec892fa77e4cecad60baf5404fde0c60c07a'
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha):
    return pwd_context.hash(senha)

def verificar_senha(senha_pura, senha_hash):
    return pwd_context.verify(senha_pura, senha_hash)

def criar_token(data: dict):
    payload = data.copy()
    expira = datetime.utcnow() + timedelta(minutes=60)
    payload.update({"exp": expira})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
