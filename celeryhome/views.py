from django.shortcuts import render , HttpResponse
# from .tasks import add, send_email
#from celeryhome.tasks import add, send_email
from .tasks import send_email_to_users

# Create your views here.

# def test(request):
#      add.delay(2,3)
#      return HttpResponse("Done")




# def your_view(request):
#     recipient_list = ['kamalpreetkaur@snakescript.com', 'avinash@snakescript.com']
#     subject = 'leave'
#     message = 'hie there'
    
#     for recipient in recipient_list:
#         send_email.delay([recipient], subject, message)
#     return HttpResponse('done sending mails')
    
    # ...




def send_email(request):
    send_email_to_users.delay()
    return HttpResponse('sending emails to model users')



