from django.shortcuts import render
from django.http import HttpResponse
from . models import Registration

# Create your views here.


def fn_index(request):
    return render(request,'index.html')

def fn_adminLog( request):
    admin_name = request.POST['admin']
    password = request.POST['password']
    try:
        if admin_name == 'admin' and password=='12345678':
            return render(request,'register.html')
        return render(request,'index.html', {'msg':'oops!!! Try Again'})
    except:
        return render(request,'index.html', {'msg':'oops!!! Enter valid Username'})


def fn_reg(request):
    return render(request,'register.html')

def fn_empreg(request):
        if request.method == 'POST':
            email   = request.POST['email']
            user_exist = Registration.objects.filter(email=email).exists()
            if not user_exist:
                emp_id  = request.POST['empid']
                name    = request.POST['name']
                phone   = request.POST['phone']
                gender  = request.POST['gender']
                job     = request.POST['job']
                pro_pic = request.FILES['image_upload']
                try:
                    reg_obj = Registration(employee_id=emp_id, name=name, email=email,phone=phone, gender=gender, job=job, image=pro_pic)
                    print(reg_obj.email)
                    reg_obj.save()
                    return render(request, 'register.html')
                except Exception as e:
                    print(str(e))
                    return render(request, 'register.html')
            return render(request,'register.html',{'msg':'Cadidate Already registered'} )
            
def fn_reglog(request):
    profile = Registration.objects.filter().order_by('id')
    return render(request, 'profiles.html', {'profiles': profile})

def fn_trash(request):
    tid = request.GET['id']
    trash_obj = Registration.objects.get(id=tid)
    # print(trash_obj.id)
    trash_obj.delete()
    return render(request,'profiles.html')

def fn_edit(request):
    pid = request.GET['id']
    edit_obj = Registration.objects.get(id=pid)
    request.session['user_id'] = edit_obj.id
    # u_id = request.session['user_id']
    # print(u_id)
    return render(request,'editprofile.html', {'pro':edit_obj})

def fn_editprofile(request):
    u_id = request.session['user_id']
    reg = Registration.objects.get(id=u_id)
    try:
        if request.method == 'POST':
            empid = request.POST['empid']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            job = request.POST['job']
            reg.employee_id = empid
            reg.name = name
            reg.email = email
            reg.phone = phone
            reg.job = job
            if request.FILES:
                myfile = request.FILES['image_upload']
                reg.image = myfile
                reg.save()
            reg.save()
        return render(request,'editprofile.html', {'pro':reg})
    except Exception as e:
        print('error')
        print(str(e))
        return HttpResponse('error')




