from django.core.mail import send_mail
from django.conf import settings as sett

CONFIRMATION_CODE_LEN = 7


def send_mail_to_user(email, confirmation_code):
    send_mail(
        subject='Код подтверждения YaMDB',
        message='Спасибо за регистрацию в нашем сервисе. '
                f'Код подтверждения: {confirmation_code}',
        from_email=sett.EMAIL_ADMIN,
        recipient_list=[email],
        fail_silently=False,
    )
