from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from User.models import UserInfo


# Create your views here.

# 初始界面展示
def IndexView(request):
    return render(request,'User/index.html')


# 用户登录界面视图
def User_Login(request):
    warning = ""
    if 'login' in request.POST:
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        # 判断输入的用户信息和数据库中所保存数据是否匹配
        if username and password:
            res = UserInfo.objects.filter(username=username, password=password).count()
            if res != 0:
                return render(request, 'map_show/index.html')
            else:
                if UserInfo.objects.filter(username=username).count()!=0:
                    warning = "密码错误！请检查拼写"
                    return render(request, 'User/login.html',locals())
                else:
                    warning = "用户名不存在！请注册！"
                    return render(request, 'User/login.html',locals())
    return render(request, 'User/login.html')


# 用户注册界面视图
def User_Register(request):
    receiver = []
    warning = ""
    if 'confirm' in request.POST:
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        email_address = request.POST.get('mailbox')
        receiver.append(email_address)
        user_valid = UserInfo.objects.filter(username=username)
        if user_valid:
            warning = "该用户已存在！"
            return render(request,'User/register.html',locals())
        else:
            user = UserInfo.objects.create(username=username, password=password,email_address=email_address)
            user.save()
            send_mail('尊敬的用户！', '恭喜您注册成功！欢迎继续使用本系统', 'haxk1024@qq.com', receiver, fail_silently=False)
            warning = "恭喜你，注册成功！一封邮件已发送到你的邮箱请查收！请按“返回”回到登录页面使用本系统吧！"
            return render(request, 'User/register_success.html',locals())
    return render(request, 'User/register.html')
