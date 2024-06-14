import typing


class Personal:
    train_type = ["Super Sonic", "Carbon"]
    
    def __init__(self, name: str, id: int, train_type: str, hours: float):
        self._name = name
        self._id = id
        self._train_type = train_type
        self._hours = hours 
        self._pay = 60 if train_type == "Super Sonic" else 30
        self._total = int
    
    @property
    def name(self):
        return self._name
    @property
    def id(self):
        return self._id
    @property
    def train_type(self):
        return self._train_type
    @property
    def hours(self):
        return self._hours
        
    @name.setter
    def set_name(self, new_name):
        self._name = new_name
        
    @id.setter
    def set_id(self,new_id):
        self.id = new_id 
        
    @train_type.setter
    def set_train_type(self,new_train_type):
        self.id = new_train_type
        
    @train_type.setter
    def set_hours(self, new_hours):
        self.id = new_hours 
        
    def get_id(self):
        return self._id 
    
    def get_train_type(self):
        return self._train_type
    
    def calculate_pay(self):
        self.total = 0
        base_pay = self.hours * self._pay 
        if self._hours > 8:
            plus_pay = base_pay * 30 / 100
            self._total = base_pay + plus_pay
        return self._total
            
    def get_data(self):
        return {
            "id": self._id,
            "train_type": self._train_type,
            "total_pay": self._total
        }
