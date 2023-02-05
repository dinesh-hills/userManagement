from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage
from .models import User


@receiver([post_save], sender=User)
def send_welcome_email_to_new_user(sender, **kwargs):
    if kwargs["created"]:
        user = kwargs["instance"]
        try:
            message = BaseEmailMessage(
                template_name="email/welcome.html",
                context={"first_name": user.first_name, "last_name": user.last_name},
            )
            message.send([user.email])

        except BadHeaderError:
            print(f"There is an error sending welcome email to {user.email}.")
