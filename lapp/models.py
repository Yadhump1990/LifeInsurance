from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    type=models.CharField(max_length=90)

class user(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=90)
    lname=models.CharField(max_length=90)
    gender=models.CharField(max_length=90)
    place=models.CharField(max_length=90)
    post=models.CharField(max_length=90)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=90)

class agent(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    name=models.CharField(max_length=90)
    place = models.CharField(max_length=90)
    pin = models.IntegerField()
    email = models.EmailField()
    experiance = models.CharField(max_length=90)
    commission_rate = models.BigIntegerField()

class complaint(models.Model):
    uid=models.ForeignKey(user,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    date=models.DateField()

class doubt(models.Model):
    uid=models.ForeignKey(user,on_delete=models.CASCADE)
    aid=models.ForeignKey(agent,on_delete=models.CASCADE)
    doubt=models.CharField(max_length=200)
    reply = models.CharField(max_length=200)
    date = models.DateField()

class policy(models.Model):
    # uid = models.ForeignKey(user, on_delete=models.CASCADE)
    aid = models.ForeignKey(agent, on_delete=models.CASCADE)
    policyNo=models.CharField(max_length=90)
    start_date=models.DateField()
    end_date=models.DateField()
    premium_amount=models.BigIntegerField()
    commission=models.BigIntegerField()

class user_request(models.Model):
    uid = models.ForeignKey(user, on_delete=models.CASCADE)
    pid = models.ForeignKey(policy, on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=90)

class feedback(models.Model):
    uid = models.ForeignKey(user, on_delete=models.CASCADE)
    aid = models.ForeignKey(agent, on_delete=models.CASCADE)
    feedback=models.TextField()
    rating=models.IntegerField()
    date=models.DateField()

class files(models.Model):
    aid = models.ForeignKey(agent, on_delete=models.CASCADE)
    file = models.FileField()
    date = models.DateField()
