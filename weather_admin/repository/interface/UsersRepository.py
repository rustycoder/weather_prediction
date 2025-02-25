from abc import ABC, abstractmethod

class UsersRepository(ABC):
  
    @abstractmethod
    def create(self, username, password):
        pass
    
    @abstractmethod
    def retrieve(self):
        pass

    @abstractmethod
    def update(self, id, password):
        pass

    @abstractmethod
    def delete(self, id):
        pass