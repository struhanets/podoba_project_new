# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.shortcuts import render
from django import template
from django.template import loader
from django.template import RequestContext

from ..models import Group

#GROUPS VIEWS
#Groupe List
def groups_list(request):
	groups = Group.objects.all()
	order_by = request.GET.get('order_by', '')


	if order_by in ('title', 'leader'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()


	paginator = Paginator(groups, 3)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		groups = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		groups = paginator.page(paginator.num_pages)



	return render(request, 'students/groups_list.html', {'groups': groups})
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