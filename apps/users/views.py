from django.views import View
from apps.users.service import *

class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'author/register.html', {"form":form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User succesfully registered")
            return redirect('author:login')
        messages.warning(request, "You`r registration is are not valid !")
        return render(request, "author/register.html", {"form":form})
    

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'author/login.html', {"form":form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                messages.success(request, F"{ username } you are logged ")
                return redirect('market:home')
            else:
                messages.warning(request, "Invalid username or password !")
                return redirect('author:login')
        return render(request, "author/login.html", {"form":form})
    

class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'author/logout.html')

    def post(self, request):
        logout(request)
        return redirect('market:home')
    
