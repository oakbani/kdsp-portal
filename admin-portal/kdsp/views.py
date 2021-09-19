from django.shortcuts import redirect


def redirect_view(request):
    response = redirect("https://kdsp-web.herokuapp.com/")
    return response
