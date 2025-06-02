from django.urls import path
from .views import home, about, show_get, form_get, submit_form_get, form_post


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('show_get/', show_get, name="show_get"),
    path('form_get/', form_get, name="form_get"),
    path('form_post/', form_post, name="form_post"),
    path('submit_form_get/', submit_form_get, name="submit_form_get"),
]