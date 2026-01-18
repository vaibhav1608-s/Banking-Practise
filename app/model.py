from pydantic import BaseModel

class Authorize(BaseModel):
    username : str
    password : str

class TokenReq(BaseModel):
    code :str
    
class RefreshToken(BaseModel):
    refresh_token : str
     