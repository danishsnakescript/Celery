from django.urls import path 
from .views import send_email
#from .views import test,your_view
urlpatterns = [
    # path("sending/",your_view),    
    # path("test/",test),
    path('sendingModelmail/',send_email),

]