"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .settings import MEDIA_ROOT, DEBUG



urlpatterns = patterns("",
	#Students urls
	url(r'^$', "students.views.students.students_list", name='home'),
	#Students Add Form
	url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
	#Student Edit Form
	url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students.students_edit', name='students_edit'),
	#Students Delete
	url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete', name='students_delete'),


	#Groups urls
    url(r'^groups/$', "students.views.groups.groups_list", name='groups'),
    #Groups Add Form
    url(r'^groups/add/$', 'students.views.groups.groups_add', name='groups_add'),
    #Groups Edit
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit', name='groups_edit'),
    #Groups delete
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete', name='groups_delete'), 

    #Journal urls
    url(r'^journal/$', 'students.views.groups.journal', name='journal'),

    #Admin side
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns ('', url(r'^media/(?P<path>.*)$', 
    'django.views.static.serve', {'document_root': MEDIA_ROOT}))