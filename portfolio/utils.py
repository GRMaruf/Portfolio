# for cache control
# from django.core.cache import cache
from portfolio.models import Profile

def get_user_profile(username):
    if username:
        return Profile.objects.filter(user__username=username).first()

def get_current_username(request):
    return request.user.username

# def get_client_ip(request):
#     ip = request.META.get('REMOTE_ADDR')
#     return ip

# cache.set('var', value, timeout=60*15) # time set is 15 minutes
# var = cache.get('var', 0) # default value is 0
# cache.delete('total_users')
# cache.clear()
