from django.urls import path

from .views import login_view, logaut_view, sign_up

app_name = 'accaunt'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logaut/', logaut_view, name='logaut_view'),
    path('register/', sign_up, name='sign_up')

]
