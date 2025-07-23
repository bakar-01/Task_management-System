from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """
    Middleware to ensure users update their profile after login.
    Redirects to profile_update page if first name, last name, or email is missing.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            path = request.path_info
            profile_update_url = reverse('profile_update')
            logout_url = reverse('logout')
            if (not request.user.first_name or not request.user.last_name or not request.user.email):
                if path != profile_update_url and path != logout_url:
                    return redirect(profile_update_url)
        response = self.get_response(request)
        return response
