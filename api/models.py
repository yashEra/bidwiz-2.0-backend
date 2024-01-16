from django.db import models
from django.contrib.auth.models import AbstractUser


# upload file and rename
def upload_to(instance, filename):
    return 'items/{filename}.{ext}'.format(filename=instance.pk , ext = filename.split('.')[-1])

# user model : its override the djangp abstract user
class User(AbstractUser):
    email= models.EmailField(max_length=200 , primary_key=True)
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=1024)
    birth_date = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to=upload_to , default="users/default_user.svg")
    username = None
    first_name = None
    last_name = None
    is_staff = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [name , email , password]

# items
class Book(models.Model):
    item_id = models.CharField(max_length = 50 , primary_key = True)
    item_name = models.CharField(max_length = 256)
    category = models.CharField(max_length = 256)
    start_bid_price = models.CharField(max_length = 10)
    current_max_bid = models.CharField(max_length = 10)
    end_date = models.CharField(max_length = 10)
    description = models.DateField(max_length = 1024)
    reviews = models.PositiveSmallIntegerField(default = 0)
    reviews_score = models.PositiveSmallIntegerField(default = 0)
    cover_image = models.ImageField(upload_to=upload_to , default="items/default.png")
    imageone = models.ImageField(upload_to=upload_to , default="items/default.png")
    imagetwo = models.ImageField(upload_to=upload_to , default="items/default.png")
    imagethree = models.ImageField(upload_to=upload_to , default="items/default.png")

    REQUIRED_FIELDS = [item_name , item_name , start_bid_price , category , end_date , cover_image , description]
