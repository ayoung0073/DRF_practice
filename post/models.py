from django.db import models

# Create your models here.
class Post(models.Model):
    no = models.AutoField(db_column='id', primary_key=True)
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']