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
	return render(request, 'students/students_list.html', {'students': students})
	# (
	# 	{'id': 1, 
	# 	'firs_name': u'Марія',
	# 	'second_name': u'Струганець',
	# 	'ticket': 2123,
	# 	'img': 'static/img/16.jpg'},
	# 	{'id':2,
	# 	'firs_name': u'Володимир',
	# 	'second_name': u'Струганець',
	# 	'ticket': 254,
	# 	'img': 'static/img/39.jpg' 
	# 	},
	# 	{'id': 3,
	# 	'firs_name': u'Монументівна',
	# 	'second_name': u'Статуя',
	# 	'ticket': 2009,
	# 	'img': 'static/img/40.jpg'
	# 	},
	# 	)

	# template = loader.get_template("students/students_list.html")
	# context = RequestContext(request, {'students':students, 'request':request})
	# return HttpResponse(template.render(context))
#Students Add Form
def students_add(request):
	return HttpResponse("<h1>Students Add Form</h1>")
#Students edit
def students_edit(request, sid):
	return HttpResponse("<h1>Edit Students {}</h1>".format(sid))
#Students delete form
def students_delete(request, sid):
	return HttpResponse("<h1>Delete Students {}</h1>".format(sid))


