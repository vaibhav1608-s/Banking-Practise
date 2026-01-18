from fastapi import Header, HTTPException, APIRouter
import uuid

from app.storage import Access_Token

router = APIRouter()

@router.get("/balance")
def balance (authorization : str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401)
    
    token = authorization.replace("Bearer", "")

    if token not in Access_Token:
        raise HTTPException(status_code=401,detail="Token Not Found")
    
    user = Access_Token[token]

    return{
        "user":user, 
        "balance":500

    }