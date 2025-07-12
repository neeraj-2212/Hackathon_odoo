from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

# Item model
class Item(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New - Never used'),
        ('like-new', 'Like New - Barely used'),
        ('good', 'Good - Some wear'),
        ('fair', 'Fair - Noticeable wear'),
        ('poor', 'Poor - Significant wear'),
    ]

    CATEGORY_CHOICES = [
        ('shirt','shirt'),
        ('t-shirt','t-shirt'),
        ('Track','Track'),
        ('Dress','Dress'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=50)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)# False = Unavailable, True = Available
    points = models.IntegerField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
class ItemImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return f"{self.user} has {self.item.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"