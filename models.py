from django.db import models

class Students(models.Models):
    student_id = models.IntegerField(primary_key = TRUE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    discipline = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    phone = models.IntegerField(Default=0)
    interview_offer = models.BooleanField(null=TRUE, default=NULL)
    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE, default=NULL)

class Projects(models.Models):
    project_name = models.CharField(max_length=200, primary_key = TRUE)
    not_for_profit_name = models.CharField(max_length=200)
