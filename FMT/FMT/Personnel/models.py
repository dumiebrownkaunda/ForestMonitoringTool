# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


# Create your models here.

class user(models.Model):
    user_id = models.IntegerField(default=0)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    website = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    # image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name_plural = "Users"


class Activity(models.Model):

        id = models.AutoField(primary_key=True)
        # trip_id = models.IntegerField()
        date = models.DateField()
        contractor = models.CharField(max_length=50)
        name = models.CharField(max_length=50)
        type = models.CharField(max_length=50)
        # user_id = models.CharField(max_length=20)
        # item_spend = models.IntegerField()
        # item_units = models.IntegerField()

        def publish(self):
            self.save()

        def __str__(self):
            return str(self.id)

        class Meta:
            verbose_name_plural = "Activity"


""" class SubscribeModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    status = models.CharField(max_length=64, null=False, blank=True)
    created_date = models.DateTimeField(null=False, blank=True)
    updated_date = models.DateTimeField(null=False, blank=True)

    class Meta:
        app_label = "Personnel"
        db_table = "Personnel_subscribe"

    def __str__(self):
        return self.email

    def save_email(email):

    try:
        subscribe_model_instance = SubscribeModel.objects.get(email=email)

    except ObjectDoesNotExist as e:
        subscribe_model_instance = SubscribeModel()
        subscribe_model_instance.email = email

    except Exception as e:
        logging.getLogger("error").error(traceback.format_exc())
        return False

    # does not matter if already subscribed or not...resend the email
    subscribe_model_instance.status = constants.SUBSCRIBE_STATUS_SUBSCRIBED
    subscribe_model_instance.created_date = utility.now()
    subscribe_model_instance.updated_date = utility.now()
    subscribe_model_instance.save()

    return True """
