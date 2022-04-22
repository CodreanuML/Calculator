from django.db import models

# Create your models here.
class Operands(models.Model):

	value_op1=models.CharField(max_length=20) 
	value_op2=models.CharField(max_length=20) 
	operand=models.CharField(max_length=1) 