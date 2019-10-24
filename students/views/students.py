# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from django import template
from django.template import loader
from django.template import RequestContext

from ..models import Student

# Create your views here.


#STUDENTS VIEWS
#Students List
def students_list(request):
	students = Student.objects.all()

	order_by = request.GET.get('order_by', '')

	if order_by in ('first_name', 'last_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	return render(request, 'students/students_list.html', {'students': students})
#Students Add Form
def students_add(request):
	return HttpResponse("<h1>Students Add Form</h1>")
#Students edit
def students_edit(request, sid):
	return HttpResponse("<h1>Edit Students {}</h1>".format(sid))
#Students delete form
def students_delete(request, sid):
	return HttpResponse("<h1>Delete Students {}</h1>".format(sid))


