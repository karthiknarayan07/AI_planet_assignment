from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Hackathon(models.Model):
    hackathon_id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='uploads')
    hackathon_image = models.ImageField(upload_to='uploads')
    type_of_submission = (
        ('image', 'image'),
        ('file', 'file'),
        ('link', 'link'),
    )
    submission_type = models.CharField(max_length=10, choices=type_of_submission)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.IntegerField()

    def __str__(self):
        return self.title
    

class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    submission_title = models.CharField(max_length=255,blank=True)
    summary = models.TextField(blank=True)
    type_of_submission = (
        ('image', 'image'),
        ('file', 'file'),
        ('link', 'link'),
    )
    submission_type = models.CharField(max_length=10, choices=type_of_submission)
    file = models.FileField(blank=True, null=True,upload_to='uploads')
    image = models.ImageField(blank=True, null=True,upload_to='uploads')
    link = models.URLField(blank=True, null=True)

    enrolled_datetime = models.DateTimeField(auto_now_add=True)
    is_submitted = models.BooleanField(default=False,blank=False)
    submitted_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.hackathon)+" - "+str(self.submitted_by)
    



