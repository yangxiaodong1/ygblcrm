from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import importlib
from ygbl_admin.utils import table_filter,table_sort,table_search
# Create your views here.
from ygbl_admin import ygbl_admin
from ygbl_admin.forms import create_model_form
#用于页面有些需要验证有些不需要登陆就可以看
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    return render(request, 'ygbl_admin/table_index.html',{'table_list':ygbl_admin.enable_admins})

@login_required
def display_table_objs(request,app_name,table_name):

    admin_class = ygbl_admin.enable_admins[app_name][table_name]
    if request.method=="POST": #action 来了
        selected_ids = request.POST.get("selected_ids")
        action = request.POST.get("action")
        if selected_ids :
            selected_objs = admin_class.model.objects.filter(id__in=selected_ids.split(','))
        else:
            raise KeyError("No object selected.")
        if hasattr(admin_class,action):
            action_func = getattr(admin_class,action)
            request._admin_action =action
            return action_func(admin_class,request,selected_objs)


    object_list,filter_conditions = table_filter(request,admin_class) # 过滤后的结果
    object_list = table_search(request,admin_class,object_list) # 查询
    object_list,orderby_key = table_sort(request,admin_class,object_list) # 排序后的结果

    paginator = Paginator(object_list, admin_class.list_per_page)  # Show 25 contacts per page

    page = request.GET.get('page')

    print("哈哈哈",paginator,'-------------',page)
    try:
        query_sets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_sets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_sets = paginator.page(paginator.num_pages)

    return render(request,"ygbl_admin/table_objs.html",{"admin_class":admin_class,
                                                         "query_sets":query_sets,
                                                        "filter_conditions":filter_conditions,
                                                        "orderby_key":orderby_key,
                                                        "previous_orderby":request.GET.get('o',''),
                                                        "search_text":request.GET.get('_q','')
                                                        })

@login_required
def table_obj_change(request,app_name,table_name,obj_id):
    admin_class = ygbl_admin.enable_admins[app_name][table_name]
    #动态生成modelform类
    model_form_class = create_model_form(request,admin_class)
    obj = admin_class.model.objects.get(id=obj_id)
    if request.method =="POST":
        form_obj = model_form_class(request.POST,instance=obj)# 跟新
        if form_obj.is_valid():
            form_obj.save()
    else:
        form_obj = model_form_class(instance =obj)

    return render(request,"ygbl_admin/table_obj_change.html",{"form_obj":form_obj,
                                                              "admin_class":admin_class,
                                                              "app_name":app_name,
                                                              "table_name":table_name
                                                              })

@login_required
def table_obj_add(request,app_name,table_name):
    admin_class = ygbl_admin.enable_admins[app_name][table_name]
    admin_class.is_add_form = True
    model_form_class = create_model_form(request,admin_class)

    if request.method == "POST":
        form_obj = model_form_class(request.POST)  #
        if form_obj.is_valid():
            form_obj.save()
            return  redirect(request.path.replace("/add/","/"))
    else:
        form_obj = model_form_class()

    return render(request, "ygbl_admin/table_obj_add.html", {"form_obj": form_obj,
                                                             "admin_class":admin_class
                                                             })

@login_required
def table_obj_delete(request,app_name,table_name,obj_id):
    admin_class = ygbl_admin.enable_admins[app_name][table_name]
    obj = admin_class.model.objects.get(id=obj_id)
    # 判断是不是只是可读的表
    if admin_class.readonly_table:
        errors = {"readonly_table":"table is read only ,obj [%s] cannot be deleted" %obj}
    else:
        errors = {}
    if request.method == "POST":
        if not admin_class.readonly_table:
            obj.delete()
            return redirect('/ygbl_admin/%s/%s' %(app_name,table_name))
    return render(request,"ygbl_admin/table_obj_delete.html",{"obj":obj,
                                                              "admin_class":admin_class,
                                                              "app_name":app_name,
                                                              "table_name":table_name,
                                                              "errors":errors
                                                              })

@login_required
def password_reset(request,app_name,table_name,obj_id):
    admin_class = ygbl_admin.enable_admins[app_name][table_name]
    model_form_class = create_model_form(request, admin_class)
    obj = admin_class.model.objects.get(id=obj_id)
    errors = {}
    if request.method == 'POST':
        _password1 = request.POST.get('password1')
        _password2 = request.POST.get('password2')
        if _password1 == _password2:
            if len(_password1)>5:
                obj.set_password(_password1)
                obj.save()
                redirect(request.path.rstrip("password/")) # 返回
            else:
                errors["password_too_short"] = "must not less than 6 letters"
        else:
            errors['invalid_password'] = "passwords are not the same"

    return render(request,'ygbl_admin/password_reset.html',{"obj":obj,
                                                            "errors":errors
                                                            })