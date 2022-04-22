from django.test import TestCase
from CALC.models import Operands
from django.urls import reverse

class Operands_test(TestCase):
	@classmethod
	def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
		Operands.objects.create(value_op1='Bigdsadasdasdasdasdaa', value_op2='Bob',operand='+')

	def test_length_op1(self) : 	
		op = Operands.objects.get(id=1)
		max_length = Operands._meta.get_field('value_op1').max_length
		op_v=op.value_op1
		print(op_v)
		self.assertEqual(max_length, 20)
		self.assertNotEqual(max_length,21)


class View_test(TestCase):
	@classmethod
	def setUpTestData(cls):
        # Create 13 authors for pagination tests
		Operands.objects.create(value_op1='Bigdsadasdasdasdasdaa', value_op2='Bob',operand='+')
	def test_url(self):
		response = self.client.get('/calculator/calc/')
		self.assertEqual(response.status_code, 200)
	def test_view_url_accessible_by_name(self):
		response= self.client.get(reverse('CALC:calc'))
		self.assertEqual(response.status_code, 200)