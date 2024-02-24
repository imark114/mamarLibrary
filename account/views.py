from django.shortcuts import render
from .forms import SignUpForm,ChangeUserData
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView
from django.contrib.auth.forms import  PasswordChangeForm
from .models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from book.models import SoldBook
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'account/form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request,'Account Created Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Sign Up'
        return context

class UserLoginView(LoginView):
    template_name = 'account/form.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged In Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Given informations are incorrect')
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs) -> dict[str]:
            context = super().get_context_data(**kwargs)
            context["type"] = 'Login'
            return context


class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

@login_required
def ProfileView(request):
    books = SoldBook.objects.filter(buyer=request.user)
    return render(request, 'account/profile.html', {'books': books})

@login_required          
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserData(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = ChangeUserData(instance=request.user)
        return render(request,'account/form.html', {'form': profile_form,'type':'Update'})

@method_decorator(login_required,name='dispatch')
class PassChangeView(PasswordChangeView):
    template_name = 'account/form.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Change Password'
        return context