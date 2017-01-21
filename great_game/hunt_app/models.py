from django.db import models

class Team(models.Model):
	team_name = models.CharField(max_length = 20)
	#team_id = models.PositiveIntegerField()
	team_member_1 = models.CharField(max_length = 20)
	team_member_2 = models.CharField(max_length = 20)
	team_member_3 = models.CharField(max_length = 20, null = True, blank = True)
	team_member_4 = models.CharField(max_length = 20, null = True, blank = True)
	team_photo = models.ImageField(upload_to='team_pics/', null = True, blank = True)
	team_score = models.PositiveIntegerField(default=0)
	team_status=models.BooleanField(default=True)
	tasks_completed = models.PositiveIntegerField(default=0)
	team_rank = models.PositiveIntegerField(null = True, blank = True)
	team_hint_count=models.PositiveIntegerField(default=0)

	#team_location =

	def __str__(self):
		return self.team_name

class Task(models.Model):
	task_name = models.CharField(max_length = 10)
	task_description = models.CharField(max_length = 50)
	task_picture = models.ImageField(upload_to ='task_pics/', null = True, blank = True)
	task_hint = models.CharField(max_length = 10)
	task_time = models.DurationField()
	task_score = models.PositiveIntegerField()
	task_nextid = models.PositiveIntegerField()

	def __str__(self):
		return self.task_name
