# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from django import template
from django.template import loader
from django.template import RequestContext

#GROUPS VIEWS
#Groupe List
def groups_list(request):
	groups = (
		{'id': 1,
		'name_group': u'МтМ-21',
		'leader': {'id': 1, 'leader_name': u'Струганець Володимир'}},
		{'id': 2,
		'name_group': u'Мтм-22',
		'leader': {'id': 2, 'leader_name': u'Струганець Марія'}},

		{'id': 3,
		'name_group': u'МтМ-23',
		'leader': {'id': 3, 'leader_name': u'Cтатуя Монументівна'}},
		)
	template = loader.get_template("students/groups_list.html")
	context = RequestContext(request, {'groups': groups, 'request':request})
	return HttpResponse(template.render(context))
#groups Add
def groups_add(request):
	return HttpResponse("<h1>Groupe Add Form</h1>")
#Edit Grouos
def groups_edit(request, gid):
	return HttpResponse("<h1>Edit Groups {}</h1>".format(gid))
#delete Groups
def groups_delete(request, gid):
	return HttpResponse("<h1>Delete Groups {}</h1>".format(gid))

#JOURNAL VIEWS
def journal(request):
	return HttpResponse("<h1>Journal</h1>")