from django.db import models
class article(models.Model):
    title=models.CharField(max_length="10")
    author=models.CharField(max_length="10")
    public_date=models.DateField()
    cat=models.CharField(max_length="10")
    image=models.ImageField()
    optional_image=models.ImageField()
    body_text=models.TextField()
# Create your models here.
