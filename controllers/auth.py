from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = 'postgresql://neondb_owner:npg_nrBGcb1aqu2T@ep-rapid-cell-apc922g9-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
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
