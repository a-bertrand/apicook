from rest_auth.registration.views import RegisterView

#TODO MAKE AUTHTIFICATION SECURE ( CSRF)
class RegisterViewToken(RegisterView):
    authentication_classes = ()