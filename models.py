from django.db import models

class Students(models.Models):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    discipline = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    phone = models.IntegerField(Default=0)
    //interview_offer = models.BooleanField(null=True, default=None)
    //project_name = models.ForeignKey(Projects, on_delete=models.CASCADE, default=None)
    interview_offer = models.BooleanField(null=True)
    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE)

class Projects(models.Models):
    project_name = models.CharField(max_length=200, primary_key=True)
    not_for_profit_name = models.ForeignKey(notForProfit, on_delete=models.CASCADE)

class notForProfit(models.Models):
    not_for_profit_name.CharField(max_length=200, primary_key=True)
    email = models.CharField(max_length=200)
    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('not_for_profit_name', 'project_name'),)

class Teams(models.Models):
    team_member_id = models.IntegerField(primary_key=True)
    project_name = models.ForeignKey(Projects, on_delete = models.CASCADE)
    student_id = models.ForeignKey(Students, on_delete = models.CASCADE)
