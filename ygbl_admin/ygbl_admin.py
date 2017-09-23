# Author : July  Yang
from crm import models
# 用于注册事件
# 先写一个基类后面的都来继承就好
from django.shortcuts import render,redirect,HttpResponse
enable_admins = {}# 开启的admin

class BaseAdmin(object):
    list_display = []
    list_filter = []
    list_per_page = 20
    ordering=None
    filter_horizontal = []
    search_fields = []
    readonly_fields = []
    readonly_table = False
    modelform_exclude_fields = []

    actions = ["delete_selected_objs",]
    def delete_selected_objs(self,request,querysets):
        app_name = self.model._meta.app_label
        table_name = self.model._meta.model_name
        if self.readonly_table:
            errors = {"readonly_table": "This table is readonly ,cannot be deleted or modified!" }
        else:
            errors = {}
        if request.POST.get("delete_confirm") == "yes":
            querysets.delete()
            return redirect("/ygbl_admin/%s/%s" %(app_name,table_name))
        selected_ids =  ''.join([str(i.id) for i  in querysets])
        return render(request,'ygbl_admin/table_obj_delete.html',{"obj":querysets,
                                                                  "admin_class":self,
                                                                  "app_name":app_name,
                                                                  "table_name":table_name,
                                                                  "selected_ids":selected_ids,
                                                                  "action":request._admin_action,
                                                                  "errors":errors
                                                                  })

    def default_form_validation(self):
        '''用户可以在这里进行自定义的表单验证，相当于django form的clean方法,可以在每一个的下面进行重写就行了'''
        pass


class CustomerAdmin(BaseAdmin):
    list_display = ['id','qq','name','source','consult_course','date','status','enroll']
    list_filters = ['source','consultant','consult_course','status','date']
    #由于这里consultant 是外键，要用两个下划线关联到那个name
    search_fields = ['qq', 'name', "consultant__name"]
    filter_horizontal = ('tags',)
    #model = Customer  # 下面的admin_class.model = model_class 和这句话等价
    list_per_page = 2
    ordering = "qq"
    actions = ["delete_selected_objs","test"]
    readonly_fields = ["qq", "consultant","tags"]
    readonly_table = False


    def test(self,request,querysets):
        print("in test")
    test.display_name = "测试动作"

    def enroll(self):
        '''报名注册'''
        # 返回什么值就显示什么值，配置，这里以后就可以自定义
        return '''<a href="/crm/customer/%s/enrollment/">报名</a>''' %self.instance.id
    enroll.display_name = "报名链接"

    def default_form_validation(self):
        # print('----------customer Validation',self)
        consult_content = self.cleaned_data.get("content",'')
        if len(consult_content)<15:
            return self.ValidationError(('Field %(field)s 咨询内容记录不能少于15个字符'),
                                        code='invalid',
                                        params={'field':'content',},
                                        )
    def clean_name(self):
        if not self.cleaned_data["name"]:
            self.add_error('name','cannot be null')


class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ('customer','consultant','date')


class UserProfileAdmin(BaseAdmin):
    #list_display = ("user","name")
    list_display = ("email","name")
    readonly_fields = ('password',)
    modelform_exclude_fields = ["last_login",]
    filter_horizontal = ('user_permissions','groups')

def register(model_class,admin_class=None):
    '''注册方法'''
    #上面传进来model_class, admin_class是要定义展示的类的字段格式等
    if model_class._meta.app_label not in enable_admins:
        #这个app没有在里面的话，加进去并且生成空字典
        enable_admins[model_class._meta.app_label] = {}

    #怎么样将admin 将model对象关联呢？
    # 相当于给admin_class 加了一个属性，让着两者产生联系，这样取值的时候就不许要再使用反射了，直接用这个值就行了
    admin_class.model = model_class
    #将表名再封装到里面
    enable_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class


class CourseRecordAdmin(BaseAdmin):
    list_display = ['from_class','day_num','teacher','has_homework','homework_title','date']


    def initialize_studyrecords(self, request, queryset):
        print('--->initialize_studyrecords',self,request,queryset)
        if len(queryset) > 1:
            return HttpResponse("只能选择一个班级")


        print(queryset[0].from_class.enrollment_set.all())
        new_obj_list = []
        for enroll_obj in queryset[0].from_class.enrollment_set.all():


            new_obj_list.append(models.StudyRecord(
                student = enroll_obj,
                course_record = queryset[0] ,
                attendance = 0 ,
                score = 0 ,
            ))

        try:

            models.StudyRecord.objects.bulk_create(new_obj_list) #批量创建

        except Exception as e:
            return HttpResponse("批量初始化学习记录失败，请检查该节课是否已经有对应的学习记录")
        return redirect("/ygbl_admin/crm/studyrecord/?course_record=%s"%queryset[0].id )
    initialize_studyrecords.display_name = "初始化本节所有学员的上课记录"
    actions = ['initialize_studyrecords',]

class StudyRecordAdmin(BaseAdmin):
    list_display = ['student','course_record','attendance','score','date']
    list_filters = ['course_record','score','attendance','student']
    list_editable = ['score','attendance']


register(models.Customer,CustomerAdmin)
register(models.CustomerFollowUp,CustomerFollowUpAdmin)
register(models.UserProfile,UserProfileAdmin)
register(models.CourseRecord,CourseRecordAdmin)
register(models.StudyRecord,StudyRecordAdmin)




