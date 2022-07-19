from django.urls  import path
from .views import example_view,variable_view

urlpatterns = [
    path("", example_view, name='examplepage'),
    path("variables/",variable_view, name='varibale_template'),
]
