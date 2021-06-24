from django.db import models

# Create your models here.
class SaveTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    currentUser = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    typeAction = models.TextField(max_length=30)
    numberOne = models.IntegerField()
    numberTwo = models.IntegerField()
    result = models.IntegerField()
    timeSolution = models.IntegerField(null=True)
    userResult = models.IntegerField(null=True)
    isTrue = models.BooleanField(null=True)
