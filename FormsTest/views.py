from django.shortcuts import render,HttpResponse

# Create your views here.
from FormsTest.register_valid import RegisterForms

def form_index(request):
    reg_forms = RegisterForms()
    if request.method == 'POST':
        reg_forms = RegisterForms(request.POST)
        if reg_forms.is_valid():
            return HttpResponse('注册成功')

    return render(request, 'FormsTest/forms_index.html',locals())