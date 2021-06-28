from django.db import models

# Create your models here.
class Question(models.Model):
    questionname=models.CharField(max_length=200)
    question=models.TextField()
    questions_created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.questionname

class Choice(models.Model):
    question_c=models.ForeignKey(Question,on_delete=models.CASCADE)
    choic=models.CharField(max_length=200)
    votes=models.IntegerField(default=1)

    def __str__(self):
        return  self.choic



class Userprofile(models.Model):
    userprofile=models.FileField(upload_to="profile")

