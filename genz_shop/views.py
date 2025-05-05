from django.shortcuts import redirect

def api_rootview(request):
    return redirect('api-root')