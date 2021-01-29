from django.db import models

# Create your models here.
class User(models.Model):
    no = models.AutoField(db_column='id', primary_key=True)
    user_id = models.CharField(db_column='user_id', max_length=30, null=False)
    name = models.CharField(db_column='name', max_length=20, null=False)
    age = models.IntegerField(db_column='age')

    def __str__(self): # 객체를 표현할 때, user_id로 표현(User.objects.all())
        return self.user_id

