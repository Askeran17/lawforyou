from django.shortcuts import render


def handler404(request, exception):
    """ Error 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler403(request, exception):
    """ Error 403 - Forbidden Error Permissions """
    return render(request, "errors/403.html", status=403)


def handler500(request):
    """ Error 500 - Server Error """
    return render(request, "errors/500.html", status=500)