# Author : July  Yang 

from django.utils.translation import ugettext as _
from django.forms import forms,ModelForm
from crm import models
from django.forms import ValidationError


def create_model_form(request,admin_class):
    '''动态生成MODEL FORM'''

    def __new__(cls, *args, **kwargs):

        # super(CustomerForm, self).__new__(*args, **kwargs)

        for field_name,field_obj in cls.base_fields.items():

            field_obj.widget.attrs['class'] = 'form-control'
            if not hasattr(admin_class,"is_add_form"): # 添加页面的时候不需要验证
                if field_name in admin_class.readonly_fields: # 用于前端页面补课修改
                    field_obj.widget.attrs['disabled'] = 'disabled'

            if hasattr(admin_class,"clean_%s" %field_name):
                field_clean_func = getattr(admin_class,"clean_%s" %field_name)
                setattr(cls,"clean_%s"%field_name,field_clean_func) #给这个form 添加上这样一个方法
        return ModelForm.__new__(cls)

    def default_clean(self):

        '''给所有的form默认增加一个clean验证'''
        # print("------running default clean",self)
        # print('==========pp===========pp==')
        #进行比较
        error_list = []

        if self.instance.id: #这是个修改的表单
            for field in admin_class.readonly_fields:
                field_val = getattr(self.instance,field) # val in db

                #针对多对多的情况
                if hasattr(field_val,"select_related"):
                    m2m_objs =getattr(field_val,"select_related")().select_related()
                    m2m_vals = [i[0] for i in m2m_objs.values_list('id')]
                    set_m2m_vals = set(m2m_vals) #from db
                    set_m2m_vals_from_frontend = set([i.id for i in self.cleaned_data.get(field)])
                    if set_m2m_vals != set_m2m_vals_from_frontend:
                        self.add_error(field,"readonly field")
                    # 字段就是分为多对多和不是多对多的，尽然经理了一个就不会往下走了
                    continue

                field_val_from_frontend = self.cleaned_data.get(field) #
                if field_val != field_val_from_frontend:
                    # raise ValidationError(_('Field %(field)s is readonly,data should be %(val)s'),
                    #                       code='invalid',
                    #                       params={'field':field,'val':field_val},
                    #                       )#  这一个的话只能管着一个
                    error_list.append(ValidationError(_('Field %(field)s is readonly,data should be %(val)s'),
                                          code='invalid',
                                          params={'field':field,'val':field_val},
                                          ))

        #readonly_table check
        if admin_class.readonly_table:
            raise ValidationError(
                _('Table is readonly,connot be modified or added'),
                code = 'invalid'
            )


        self.ValidationError =ValidationError
        response = admin_class.default_form_validation(self) # 验证后反过来的错误信息，添加到列表中
        if response:
            error_list.append(response)

        if error_list:
            raise ValidationError(error_list)

    class Meta:
        model = admin_class.model
        fields = "__all__"
        exclude = admin_class.modelform_exclude_fields    #把这个字段加 到admin_class 中
    attrs = {'Meta':Meta}
    _model_form_class =  type("DynamicModelForm",(ModelForm,),attrs)
    setattr(_model_form_class,'__new__',__new__)
    setattr(_model_form_class, 'clean', default_clean)

    # print("model form",_model_form_class.Meta.model )
    return _model_form_class







