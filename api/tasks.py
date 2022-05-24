from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from api.models import UserVault
from demoApp.settings import EMAIL_HOST_USER

@shared_task(bind=True)
def send_mail_task(request):
    email_list = []
    data = UserVault.objects.all()
    
    for rec in data:
        email_list.append(rec.email)

    email_list =list(set(email_list))
    send_mail(
        subject ='Celery Testing',
        message = 'Enter New Password',
        from_email = EMAIL_HOST_USER,
        recipient_list = email_list,
        fail_silently = False  
    )
    
    return None
  

    