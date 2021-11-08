from typing import Optional
from . import meta

class Config(metaclass=meta.Singleton):
    
    def __init__(self, token: Optional[str] = None):
        if token is not None:
            self.token = token
            
    def config(self, token: str):
        self.token = token
        
    def get_token(self):
        return {'token': self.token}