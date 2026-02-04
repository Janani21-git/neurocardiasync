from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class StressData(models.Model):

    Gender = models.IntegerField()  # 0 = Female, 1 = Male
    Age = models.IntegerField()

    Heart_rate_BPM = models.IntegerField()
    Heart_rate_variability = models.FloatField()
    Respiratory_rate = models.IntegerField()

    Mental_Fatigue_level = models.FloatField()
    Reaction_time_delay = models.FloatField()

    Adrenaline = models.FloatField()
    Cortisol_level = models.FloatField()

    Stress_level = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
