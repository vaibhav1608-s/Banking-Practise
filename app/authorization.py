from fastapi import Header , HTTPException, APIRouter
import uuid

from app.model import Authorize
from app.storage import Auth_code

router = APIRouter()

@router.post("/authorize")
#Authorize is a base model that will check user and pass and convert into py object
def authorize(request: Authorize):
    if request.username != "Vaibhav" or request.password != "Single":
        raise HTTPException(status_code=401, detail="Invalid Username or password")
    
    #if ok, generate auth code using uuid
    auth_code = str(uuid.uuid4())

    #store the auth_code in Auth_code and link it to the user 
    Auth_code[auth_code]=request.username

    #return authorizattion code in header, it will be a string 
    return{
    "authorization_code":Auth_code
    }