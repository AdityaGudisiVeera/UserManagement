from pydantic import BaseModel
# basemodel includes typecasting ,Automatic error responses,Data validation etc.,
class User(BaseModel):
    id:int
    name:str
    age:int
    relation:bool
    gender:str
    
    
