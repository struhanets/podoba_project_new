from .settings import PORTAL_URL

def students_proc(request):
	return {'PORTAL_URL': 'http://' + request.get_host()}