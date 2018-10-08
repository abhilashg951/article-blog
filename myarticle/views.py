from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from social.tests.models import User

from myarticle.models import Signup, Article


def signup_get(request):
    return render(request, 'registration.html')


def base_get(request):
    return render(request, 'base.html')

def login_get(request):
    return render(request, 'login.html')

@csrf_exempt
def signup_post(request):
    print('-------------------------------------------------------')
    if request.method == "POST":
        try:
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            first_name = request.POST.get('first_name')
            print('first_name', first_name)
            last_name =  request.POST.get('last_name')
            phone_no = request.POST.get('phone_no')
            email = request.POST.get('email')
            dob = request.POST.get('dob')
            password = request.POST.get('password')
            User.objects.create(username=email, password=password)
            Signup.objects.create(first_name=first_name, last_name=last_name, phone_no=phone_no, email=email, dob=dob,
                                  password=password)
            return JsonResponse({'success':True})
        except Exception as e:
            return JsonResponse({'success': False})

def article_dashboard(request):
    article_set = Article.objects.all()
    article_list = []
    for i in article_set:
        data = {}
        image = request.scheme+"://"+request.get_host()+"/"+"media/" + str(i.img)
        data['article_name'] = i.article_name
        data['article_desc'] = i.article_desc
        data['category'] = i.category
        data['tag'] = i.tag
        data['image'] = image
        data['id'] = i.id
        article_list.append(data)
    return render(request, 'article_dashboard.html', {'article_list': article_list})

@csrf_exempt
def login_post(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Signup.objects.get(email=email,password=password):
            request.session['email'] = email
            return JsonResponse({'success':True, 'email': email})
        elif Signup.objects.get(phone_no=email,password=password):
            request.session['email'] = email
            return JsonResponse({'success': True, 'email': email})
        else:
            return JsonResponse({'success': False})

@csrf_exempt
def add_article_post(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        tag = request.POST.get('tag')
        img = request.FILES.get('img')
        Article.objects.create(article_name=name, article_desc=description, category=category, tag=tag, img=img)
        return JsonResponse({'success': True})
    else:
        print('llllllllllllllllllllllllllllllllllllllllllllllll')
        return JsonResponse({'success':False})
def add_article_get(request):
    return render(request, 'add_article.html')

@csrf_exempt
def del_article(request):
    if request.method =="POST":
        article_id = request.POST.get('id')
        obj = Article.objects.get(id=article_id)
        obj.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({ 'success': False})

@csrf_exempt
def edit_article_get(request):
    if request.method == "GET":
        edit_id = request.GET.get('id')
        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        print(edit_id)
        print(type(id))
        ob = Article.objects.get(id=int(edit_id))
        data = {}
        data['article_name'] = ob.article_name
        data['article_desc'] = ob.article_desc
        data['category'] = ob.category
        data['tag'] = ob.tag
        data['id'] = ob.id
        # data['img'] = ob.img
        print(data)
        return JsonResponse({ 'success': True, 'data': data})

    elif request.method == "POST":
        edit_id = request.POST.get('id')
        print(type(id))
        ob = Article.objects.get(id=int(edit_id))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        tag = request.POST.get('tag')
        img = request.FILES.get('img')
        if img!= '':
            ob.article_name = name
            ob.description = description
            ob.category = category
            ob.tag = tag
            ob.save()
            return JsonResponse({'success':True})
        else:
            ob.article_name = name
            ob.description = description
            ob.category = category
            ob.tag = tag
            ob.img = img
            ob.save()
            return JsonResponse({'success': True})

def logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return render(request, 'base.html')