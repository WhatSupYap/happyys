from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from common.forms import UserForm
from django.db.models import Q
from blog.views import post_list_core

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('blog:index')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:index')
        else:
            return redirect('common:login')
    else:
        return render(request, 'common/login.html')
    
def search(request):
    # 파라미터 받아와서 조회
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    post_list = post_list_core(kw, 10, page)

    context = {'post_list': post_list, 'kw': kw, 'page': page , 'suburl': 'blog:index'}
    return render(request, 'blog/post_list.html', context)