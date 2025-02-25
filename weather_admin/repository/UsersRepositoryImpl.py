from weather_admin.repository.interface import UsersRepository
from weather_admin.models import Users

class UsersRepositoryImpl(UsersRepository):

    def create(self, username, password):
        user = Users(username=username, password=password)
        user.save()
    
    def retrieve(self):
        return Users.objects.all().values()

    def update(self, id, password):
        user = Users.objects.all()[id]
        user.password = password
        user.save()

    def delete(self, id):
        user = Users.objects.all()[id]
        user.delete()
