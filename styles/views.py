from django.shortcuts import render_to_response

def stylesheet(request):
    return render_to_response('style.css', mimetype='text/css')
