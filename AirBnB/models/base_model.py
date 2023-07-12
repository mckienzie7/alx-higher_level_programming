import uuid
import datetime

class BaseModel():
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = created_at


    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "]"
        string += self.created_at + self.__dict__

        return string
    
    def save(self):
        self.updated_at = self.created_at

    def to_dict(self):
        objj = {
            "__class__" : self.__class__.__name__,
            "updated_at" : self.updated_at.isoformat(),
            "created_at" : self.created_at.isoformat(),
            "id" : self.id
        }
        return objj
    
    
