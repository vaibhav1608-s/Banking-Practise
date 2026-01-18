from jose import jwt , JWTError
import time

security_key = "Super-key"
Algo = "HS256"

Access_token_expire_seconds=300
Refresh_token_expire_seconds=1800

def create_token(username : str):
    payload = {
        "sub":username,
        "type":"access",
        "exp": int(time.time())+Access_token_expire_seconds
    }
    return jwt.encode(payload,security_key,algorithm=Algo)

# Converts JSON → JWT string => eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...


def refresh_token(username: str):
    payload = {
        "sub":username,
        "type":"refresh",
        "exp":int(time.time())+Refresh_token_expire_seconds
    }
    return jwt.encode(payload,security_key,algorithm=Algo)

#decode token will verify and  decode it 
def decode_token(token:str, token_type : str):
    try:
        payload = jwt.decode(token,security_key,algorithm=[Algo])
        #v   token_type -> 'access' or 'refresh'
        if payload.get("type") != token_type:
            return None
        return payload.get("sub")
    except JWTError:
        return None
                