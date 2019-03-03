# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


#STUDENTS VIEWS
#Students List
def students_list(request):
	return render(request, "students/students_list.html", {})
#Students Add Form
def students_add(request):
	return HttpResponse("<h1>Students Add Form</h1>")
#Students edit
def students_edit(request, sid):
	return HttpResponse("<h1>Edit Students {}</h1>".format(sid))
#Students delete form
def students_delete(request, sid):
	return HttpResponse("<h1>Delete Students {}</h1>".format(sid))


#GROUPS VIEWS
#Groupe List
def groups_list(request):
	return HttpResponse("<h1>Groups listing</h1>")
#groups Add
def groups_add(request):
	return HttpResponse("<h1>Groupe Add Form</h1>")
#Edit Grouos
def groups_edit(request, gid):
	return HttpResponse("<h1>Edit Groups {}</h1>".format(gid))
#delete Groups
def groups_delete(request, gid):
	return HttpResponse("<h1>Delete Groups {}</h1>".format(did))
