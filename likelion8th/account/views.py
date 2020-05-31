from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username") #form valid 통과한 애들을 cleand_data라 함
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm() # 빈 폼
        return render(request, "account.html", {"form": form}) #폼이 화면에 뜨는거


def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) #폼으로 받은 데이터로 유저를 만들어야되니까 request.POST 넣어줌
        
        if form.is_valid():
            user = form.save()
            login(request, user) #회원가입 하자마자 로그인된 상태 유지
            return redirect("home")
    else:
        form = UserCreationForm()
        return render(request, "account.html", {"form":form})
    
