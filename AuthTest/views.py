from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from AuthTest.commonTools import requestJSON


@requestJSON
def index(request):
    if request.method == 'POST':
        dict = {'status': 100, 'msg': None}
        # 获取post信息
        userName = request.POST.get('name')
        password = request.POST.get('pwd')
        user = authenticate(username=userName,password=password)
        if user:
            dict['status'] = 200
            dict['msg'] = '登陆成功'
            #把user对象放到request对象中，所有的request对象都拥有这个对象
            login(request,user)
            return JsonResponse(dict)
        else:
            dict['status'] = 100
            dict['msg'] = '用户名或密码不正确'
            return JsonResponse(dict)
    else:
        return render(request,'AuthTest/index_page.html')



@login_required(login_url='/index/')
def login_success(request):
    print(request.user)
    # 这个判断由装饰器实现了
    if request.user.is_authenticated:
        return render(request, 'AuthTest/login_success.html')
    else:
        return render(request, 'AuthTest/index_page.html')

def auth_logout(request):
    logout(request)
    return render(request, 'AuthTest/index_page.html')