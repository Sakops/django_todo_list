from django.urls import path
from .views import index, about, login_user, logout_user, todo_list, todo_detail, todo_delete, home
from . import views as logic

# тут только "маршруты" - адрес страницы
urlpatterns = [
    path('', home, ""),

    path('home/', home, name="home"),
    path('user_create/', view=logic.user_create, name="user_create"),
    path('index/', index, name="index"),
    path('about/', about, name="about"),
    path('login_user/', login_user, name="login_user"),
    path('todo_detail/<int:todo_id>/', view=todo_detail, name="todo_detail"),
    path(route='todo_list/', view=todo_list, name="todo_list"),
    path(route='todo_create/', view=logic.todo_create, name="todo_create"),
    path(route='todo_delete/<int:todo_id>', view=todo_delete, name="todo_delete"),
    path(route='todo_update/<int:todo_id>', view=logic.todo_update, name="todo_update"),
    path(route='todo_change_data/<int:todo_id>/', view=logic.todo_change_data, name="todo_change_data"),
    path('logout_user', view=logout_user, name="logout_user")
    #users
]