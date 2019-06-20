from django.shortcuts import render,HttpResponse
# Create your views here.

from FormsTest.register_valid import RegisterForms

def form_index(request):
    reg_forms = RegisterForms()
    error = ''
    if request.method == 'POST':
        reg_forms = RegisterForms(request.POST)
        # 4 调用forms的is_valid方法，完成校验，is_valid返回true或者false
        if reg_forms.is_valid():
            register = reg_forms.cleaned_data
            print(register)
            return HttpResponse('注册成功')
        else:
            from django.forms.utils import ErrorDict
            # 获取全局的error信息,只显示第一个
            if reg_forms.errors.get('__all__'):
                error = reg_forms.errors.get('__all__')[0]

    return render(request, 'FormsTest/forms_index.html',locals())