from django.shortcuts import render
from .models import Operands
from django.contrib import messages
# Create your views here.


def main(request):

	obj=Operands.objects.get(pk=1)
	operator1=obj.value_op1
	operator2=obj.value_op2
	operand=obj.operand

	displayed_value=operator1

	val=0
	opd=""

	if request.method=="GET":

			

		if "DEL" in request.GET:
			val=request.GET["DEL"]

		elif "%" in request.GET:
			val=request.GET["%"]

		elif "AC" in request.GET:
			val=request.GET["AC"]

		elif "7" in request.GET:
			val=request.GET["7"]

		elif "8" in request.GET:
			val=request.GET["8"]

		elif "9" in request.GET:
			val=request.GET["9"]

		elif "4" in request.GET:
			val=request.GET["4"]

		elif "5" in request.GET:
			val=request.GET["5"]

		elif "6" in request.GET:
			val=request.GET["6"]

		elif "*" in request.GET:
			val=request.GET["*"]

		elif "1" in request.GET:
			val=request.GET["1"]

		elif "2" in request.GET:
			val=request.GET["2"]

		elif "3" in request.GET:
			val=request.GET["3"]

		elif "-" in request.GET:
			val=request.GET["-"]

		elif "0" in request.GET:
			val=request.GET["0"]

		elif "." in request.GET:
			val=request.GET["."]

		elif "eq" in request.GET:
			val=request.GET["eq"]

		elif "+" in request.GET:
			val=request.GET["+"]

	if val == 0 :
			obj.value_op1=""
			obj.value_op2=""
			obj.operand=""
			obj.save()
	elif val in ["1","2","3","4","5","6","7","8","9","."]:

		if len(obj.value_op1)>=20 :
			messages.add_message(request, messages.INFO, 'Error : Limit exceeded !')
		else:	
			displayed_value=displayed_value+val
			obj.value_op1=displayed_value
			obj.save()


	elif val in ["+","-","%","*"]:
		
		if obj.operand == "" :
			obj.value_op2=obj.value_op1
			obj.value_op1=""
			obj.operand=val
			opd=obj.operand
			obj.save()


	elif val == "eq" :


		if obj.operand=="+":
			if ("." in obj.value_op1) or ("." in obj.value_op2) :
				obj.value_op1=str(float(obj.value_op1)+float(obj.value_op2))
				obj.operand=""
				obj.save()
				
			else :
				obj.value_op1=str(int(obj.value_op1)+int(obj.value_op2))
				obj.operand=""
				obj.save()
							

		if obj.operand=="-":
			if ("." in obj.value_op1) or ("." in obj.value_op2) :
				obj.value_op1=str(float(obj.value_op2)-float(obj.value_op1))
				obj.operand=""
				obj.save()
				
			else :
				obj.value_op1=str(int(obj.value_op2)-int(obj.value_op1))
				obj.operand=""
				obj.save()
							


		if obj.operand=="*":
			if ("." in obj.value_op1) or ("." in obj.value_op2) :
				obj.value_op1=str(float(obj.value_op2)*float(obj.value_op1))
				obj.operand=""
				obj.save()
				
			else :
				obj.value_op1=str(int(obj.value_op2)*int(obj.value_op1))
				obj.operand=""
				obj.save()
					

		if obj.operand=="%":
			if ("." in obj.value_op1) or ("." in obj.value_op2) :
				obj.value_op1=str(float(obj.value_op2)//float(obj.value_op1))
				obj.operand=""
				obj.save()
				
			else :
				obj.value_op1=str(int(obj.value_op2)/int(obj.value_op1))
				obj.operand=""
				obj.save()
						


	elif val == "AC":
		obj.value_op1=""
		obj.value_op2=""
		obj.operand=""
		obj.save() 

	elif val=="DEL" :
		len_str=len(obj.value_op1)
		new_str=""
		
		new_str=obj.value_op1[0:len_str-1]
		obj.value_op1=new_str
		obj.save()

	display=obj.value_op1

		



	return render(request,'calc_template.html',{"val":val,"display":display,"opd":opd})

