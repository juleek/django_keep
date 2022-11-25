import django.shortcuts as djsh
import django.contrib as djc

def chose_url_home(request):
    if request.user.is_authenticated:
        return djsh.reverse('home')
    else:
        return ""


def get_all_params(request):
    return {"url_home": chose_url_home(request)}
