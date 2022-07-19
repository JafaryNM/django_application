from django.urls  import path
from .views import example_view,variable_view,all_list

urlpatterns = [
    path("", example_view, name='examplepage'),
    path("variables/",variable_view, name='varibale_template'),
    path("lists",all_list, name='all_list_inloop'),
]
