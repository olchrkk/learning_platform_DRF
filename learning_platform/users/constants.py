from .models import CustomUser

USER_DATA = {'email': 'test@email.com', 'first_name': 'fist_name', 'last_name': 'last_name', 'password': 'pass'}


def create_user():
    user = CustomUser.objects.create_user(email='test@email.com', password='pass', first_name='fist_name', last_name='last_name')
    return user


"""
1) написать аннотауии сложных типо для наших методов
2) миксины еще, прокинуть во все можели
3) закончит ендпоинт для рекомендаций

"""