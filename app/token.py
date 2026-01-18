from fastapi import HTTPException, APIRouter
import uuid
from app.security import create_token,refresh_token
from app.storage import Auth_code
from app.model import TokenReq

router = APIRouter()

@router.post("/token")
def token(request:TokenReq):
    if request.code not in  Auth_code:
        raise HTTPException(status_code=401,detail="Invalide code")
    
    #we were generating a random token using uuid 
    
    # access_token = str(uuid.uuid4())\
        
    #we are getting username to which auth code is assosctaed with 
    username = Auth_code[request.code]
    #we gave jwt token to access_token by using create token which is a class in security 
    
    access_token = create_token(username)
    refesh_token = refresh_token(username)

    del Auth_code[request.code]

    return{
        "access_token":access_token,
        "refresh_toke":refesh_token,
        "token_type": "Bearer",
        "expire":300
    }