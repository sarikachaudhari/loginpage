from django import models

class UserLoginform(models.model):
	username = models.CharField(max_length=10)
	mob_no = models.IntegerField(null=True)
	email = models.TextField(max_length=10)
	password = models.PasswordField(max_length=8)

	def __unicode__(self):
		return str(self.username)