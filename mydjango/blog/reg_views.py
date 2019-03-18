from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .forms import UserProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Post, UserProfile

class RegistrationFormView(View):
    form_class = UserProfileForm
    template_name = 'registration_page.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        print(email,first_name,last_name,password)
        # Create user
        user, is_created = User.objects.get_or_create(username=email, email=email)
        if is_created:
            print(user.id)
            user.set_password(password)
            user.save()
        # Create User Profile now
        if user:
            up, is_created = UserProfile.objects.get_or_create(
                user=user,
                email=email,
                first_name=first_name,
                last_name = last_name
            )
            print(up.id,'================upid')
        return redirect('/')
        