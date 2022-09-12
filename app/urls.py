from django.urls import path
from app.views import home, login, signout, signup, add_todo, signout, delete_todo, change_todo, change_password

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('add-todo/', add_todo),
    path('delete-todo/<int:id>', delete_todo),
    path('change-status/<int:id>/<str:status>', change_todo),
    path('change_password/', change_password),
    path('logout/', signout),
]