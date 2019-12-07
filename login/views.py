from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from .models import gender_display2value
from .InfoGrasp import Spider
# from .forms import UserForm



# 爬虫工具人
spider = Spider()
def get_CAPTCHA():
    spider.get_CAPTCHA()

def get_personal_info(user_id, password, captcha):
    spider.get_personal_info(user_id, password, captcha)
    return spider

# Create your views here.
def index(request):
    pass
    return render(request,'index.html')


# 不使用表单登陆
def login(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id', None)
        password = request.POST.get('password', None)
        captcha = request.POST.get('captcha', None)

        # 爬虫获取个人信息
        spider = get_personal_info(user_id, password, captcha)
        # 根据爬虫的message判断是否登陆成功
        if spider.message == '验证码错误！':
            return render(request, 'login.html', {"message": spider.message})
        elif spider.message == '用户名或密码错误！':
            return render(request, 'login.html', {"message": spider.message})
        # 成功登陆，如果之前未登陆过，注册写入数据库，如果登陆过，则提示登陆成功
        elif spider.message == '成功登陆':
            # 判断用户之前是否登陆过
            try:
                user = models.User.objects.get(user_id=user_id)
                request.session['is_login'] = True
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.name
                
            except:
                new_user = models.User.objects.create()
                new_user.name = spider.student_info.name
                new_user.user_id = spider.student_info.student_id
                new_user.major = spider.student_info.major
                new_user.college = spider.student_info.college
                new_user.degree = spider.student_info.degree
                new_user.grade = spider.student_info.grade
                new_user.gender = gender_display2value(spider.student_info.gender)
                new_user.native_place = spider.student_info.native_place
                new_user.email = spider.student_info.email
                new_user.phone  = spider.student_info.phone
                new_user.save()
                request.session['is_login'] = True
                request.session['user_id'] = new_user.user_id
                request.session['user_name'] = new_user.name
            return redirect('/index/')
    else:
        # 第一次登陆界面，没有提交表单，就爬虫连接教务处网站，获取验证码
        get_CAPTCHA()
    return render(request, 'login.html')



def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")