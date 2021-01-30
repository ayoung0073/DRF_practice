from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(db_column='id', primary_key=True) # 쓰지 않아도 장고는 자동 id 생성해줌
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return str(self.id) + ' ' + self.title

    class Meta:
        ordering = ['created_at']

class Comment(models.Model):
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comment')
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return str(self.id) + ' ' + self.content

    class Meta:
        ordering = ['created_at']

