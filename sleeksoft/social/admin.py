from django.contrib import admin
from django.contrib import auth

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import mark_safe
from social.models import *

from knox.auth import AuthToken

admin.site.unregister(AuthToken)

class UserAdmin(BaseUserAdmin):
    list_display = ('id','email', 'username',)
    search_fields = ('email', 'username',)

    # fieldsets = BaseUserAdmin.fieldsets
    # fieldsets[0][1]['fields'] = fieldsets[0][1]['fields'] + (
    #     'Money','Total_recharge_money','Total_amount_deducted','Avatar','OTP','Two_factor_authentication'
    # )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email','username', 'password1', 'password2','Avatar')}
    #     ),
    # )
admin.site.register(User,UserAdmin)
admin.site.unregister(auth.models.Group)

class Member_Admin(admin.ModelAdmin):
    list_display = ('id','Date_of_birth','Address','user')
    search_fields = ('Date_of_birth','Address','user__username',)

    readonly_fields = ["Show_Avatar"]
    def Show_Avatar(self,Member):
        return mark_safe("<img src='/{img_url}' alt='Image' style='width:120px;'/>".format(img_url=Member.Avatar.name))

admin.site.register(Member,Member_Admin)

class Post_Admin(admin.ModelAdmin):
    list_display = ('id','Content','Creation_time','user')
    search_fields = ('Content','Creation_time','user__username',)

admin.site.register(Post,Post_Admin)

class Image_Post_Admin(admin.ModelAdmin):
    list_display = ('id','Image_post','post')
    search_fields = ('Image_post','post__id',)

    readonly_fields = ["Show_Avatar"]
    def Show_Avatar(self,Image_Post):
        return mark_safe("<img src='/{img_url}' alt='Image' style='width:120px;'/>".format(img_url=Image_Post.Avatar.name))

admin.site.register(Image_Post,Image_Post_Admin)

class Comment_Admin(admin.ModelAdmin):
    list_display = ('id','post','name','body','body_admin')
    search_fields = ('body','body_admin','post__Content','name__username',)

admin.site.register(Comment,Comment_Admin)