from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# from django.contrib.auth.models import User
# from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     points = models.IntegerField(default=0)

#     def __str__(self):
#         return self.user.username

# class Item(models.Model):
#     CONDITION_CHOICES = [
#         ('new', 'New'),
#         ('good', 'Good'),
#         ('used', 'Used')
#     ]
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     category = models.CharField(max_length=50)
#     item_type = models.CharField(max_length=50)
#     size = models.CharField(max_length=20)
#     condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
#     tags = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='items/')
#     uploader = models.ForeignKey(User, on_delete=models.CASCADE)
#     available = models.BooleanField(default=True)
#     approved = models.BooleanField(default=False)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
# class SwapRequest(models.Model):
#     item = models.ForeignKey(Item, related_name='requested_item', on_delete=models.CASCADE)
#     requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     approved = models.BooleanField(default=False)
#     completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Redemption(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     points_used = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)