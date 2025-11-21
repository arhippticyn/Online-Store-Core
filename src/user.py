class User: 
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def set_name(self, new_name):
        if not new_name.strip():
            raise ValueError("Name cannot be empty")
        self.__name = new_name
    
    def set_email(self, new_email):
        if '@' not in new_email or '.' not in new_email:
            raise ValueError('Email is invalid')
        self.__email = new_email
    
    
    