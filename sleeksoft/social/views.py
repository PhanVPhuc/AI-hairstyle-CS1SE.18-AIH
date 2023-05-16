from .models import *
from .serializers import *

import rest_framework.status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import  permissions


from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated   
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.conf import settings 
from rest_framework import status

from knox.models import AuthToken
from knox.settings import CONSTANTS

from django.http import HttpResponse
import requests
import time

import datetime
from django.db import models
from django.utils import timezone

# chức năng Đăng nhập
@api_view(['POST'])
def login(request):
	try:
		username = request.data['username']
		password = request.data['password']

		if  username != None and password != None:

			if  username.split() != [] and password.split() != []:

				if  list(username).count(' ') == 0 and list(password).count(' ') == 0:

					try:
						serializer = AuthTokenSerializer(data=request.data)
						serializer.is_valid(raise_exception=True)
						user = serializer.validated_data['user']
						__,token = AuthToken.objects.create(user)

						user.last_login = timezone.now()
						user.save(update_fields=['last_login'])

						message = {'Login information':'Logged in successfully !','id':user.id,'email':user.email,'username':user.username,'token':token}
						return Response(message,status=status.HTTP_200_OK)

					except:
						message = {'Error message English':'Thông tin đăng nhập không chính xác!'}
						return Response(message, status=status.HTTP_400_BAD_REQUEST)
				else:
					message = {'Error message English':'Thông tin đăng nhập phải là một dãy ký tự !'}
					return Response(message, status=status.HTTP_400_BAD_REQUEST)
			else:
				message = {'Error message English':'Thông tin đăng nhập không được để trống!'}
				return Response(message, status=status.HTTP_400_BAD_REQUEST)
		else:
			message = {'Error message English':'Thông tin đăng nhập không được để trống!'}
			return Response(message, status=status.HTTP_400_BAD_REQUEST)
	except:
		message = {'Error message English':'Thông tin đăng nhập không chính xác!'}
		return Response(message, status=status.HTTP_400_BAD_REQUEST)

# chức năng Duy trì đăng nhập
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def keep_login(request):
    try:
        id_user = request.data["id"]
        token = request.data["token"]
        data_user = User.objects.get(id=id_user,is_active=True)
        data_token = AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])

        if int(data_token.user_id) == int(data_user.id):
            data_user.last_login = timezone.now()
            data_user.save(update_fields=['last_login'])
            message = {'Login information':'Logged in successfully !',"id":data_user.id,"email":data_user.email,"username":data_user.username,'user_Member':MemberSerializer(data_user.user_Member).data,"token":token}
            return Response(message,status=status.HTTP_200_OK)
        else:
            message = {'Error message English': 'This account is Invalid !'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    except:
        message = {'Error message English': 'Invalid data !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST) 

# chức năng Tạo tài khoản mới
@api_view(['POST'])
def create_user(request):
	email = request.data['email']
	dk_email_1 = email.find("@")
	dk_email_2 = email.find(".")
	if int(dk_email_1) > 0 and int(dk_email_2) > 0:
		username = request.data['username']
		password = request.data['password']
		confirm_password = request.data['confirm_password']

		data_user_email = User.objects.filter(email=email)
		data_user_email_serializer = UserSerializer(data_user_email,many=True)

		data_user_username = User.objects.filter(username=username)
		data_user_username_serializer = UserSerializer(data_user_username,many=True)


		if email != None and username != None and password != None:

			if email.split() != [] and username.split() != [] and password.split() != []:

				if list(email).count(' ') == 0 and list(username).count(' ') == 0 and list(password).count(' ') == 0:

					if data_user_username_serializer.data == []:

						if password == confirm_password:
							if len(data_user_email_serializer.data) < 2:
								User.objects.create(email=email,username=username,password=password,is_active=True)
								data_user = User.objects.get(email=email,username=username,is_active=True)
								pw = data_user.password
								data_user.set_password(pw)
								data_user.save()

								Member.objects.create(user=data_user)
								message = {'Create account ':'Account successfully created !'}
								return Response(message,status=status.HTTP_200_OK)
							else:
								message = {'Error message English':'Email của bạn có tối đa 2 tài khoản !'}
								return Response(message, status=status.HTTP_400_BAD_REQUEST)
						else:
							message = {'Error message English':'Xác nhận lại mật khẩu sai!'}
							return Response(message, status=status.HTTP_400_BAD_REQUEST)

					else:
						message = {'Error message English':'Tên người dùng tài khoản đã tồn tại !'}
						return Response(message, status=status.HTTP_400_BAD_REQUEST)
				else:
					message = {'Error message English':'Thông tin đăng ký phải là một chuỗi ký tự đơn !'}
					return Response(message, status=status.HTTP_400_BAD_REQUEST)
			else:
				message = {'Error message English':'Thông tin đăng ký không được để trống !'}
				return Response(message, status=status.HTTP_400_BAD_REQUEST)
		else:
			message = {'Error message English':'Thông tin đăng ký không được để trống !'}
			return Response(message, status=status.HTTP_400_BAD_REQUEST)
	else:
		message = {'Error message English':'Email đăng ký không hợp lệ !'}
		return Response(message, status=status.HTTP_400_BAD_REQUEST)       

# chức năng Lấy thông tin của tài khoản User
@api_view(['GET'])
def Information_Member(request):
	username_id = request.query_params.get('username_id')
	data_user = User.objects.get(pk=username_id,is_active=True)

	data_information_user = Member.objects.filter(user=data_user)
	data_information_user_Json = MemberSerializer(data_information_user,many=True).data[0]
	message = {'Data':data_information_user_Json}
	return Response(message,status=status.HTTP_200_OK)

# chức năng Cập nhật Avatar User
@api_view(['POST'])
def Information_Member_Edit_Avatar(request):
	username_id = request.data['username_id']
	Avatar = request.data['Avatar']
	data_user = User.objects.get(pk=username_id,is_active=True)

	data_information_user = Member.objects.get(user=data_user)
	data_information_user.Avatar = Avatar
	data_information_user.save()

	# data_information_user_Json = MemberSerializer(data_information_user,many=True).data[0]
	message = {'Update':'Update Avatar successfully'}
	return Response(message,status=status.HTTP_200_OK)

# chưc năng cập nhật thông tin User
class MemberViewSet(viewsets.ViewSet,generics.UpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    parser_classes = [MultiPartParser,]


class Image_Post_ListViewSet(generics.ListCreateAPIView):
    queryset = Image_Post.objects.all()
    serializer_class = Image_PostSerializer
    parser_classes = [MultiPartParser,]

# chức năng Tạo bài đăng của User
class PostViewSet(generics.CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	parser_classes = [MultiPartParser,]


# chức năng Xóa bài đăng của User
@api_view(['GET'])
def Delete_Post(request):
	post_id = request.query_params.get('post_id')
	data_post_id = Post.objects.get(pk=post_id)
	data_post_id.delete()
	message = {'Information_Delete':'Delete post_id successfully' }
	return Response(message,status=status.HTTP_200_OK)

# chức năng Lấy tất cả bài đăng của User
@api_view(['GET'])
def List_Post_user(request):
	username_id = request.query_params.get('username_id')
	data_user = User.objects.get(pk=username_id,is_active=True)

	list_data = Post.objects.filter(user=data_user)
	list_data_Json = PostSerializer(list_data,many=True).data
	message = {'Data':list_data_Json }
	return Response(message,status=status.HTTP_200_OK)

# chức năng Lấy tất cả bài đăng của tất cả các User
@api_view(['GET'])
def List_Post(request):
	list_post = Post.objects.all()
	list_post_Json = PostSerializer(list_post,many=True).data

	for k in list_post_Json:
		k['user'] = UserSerializer(User.objects.get(pk=k['user'])).data

	message = {'Data':list_post_Json}
	return Response(message,status=status.HTTP_200_OK)

# chức năng Thêm bình luận vào bài đăng của User
@api_view(['POST'])
def add_comments(request):
	username_id = request.data['username_id']
	data_user = User.objects.get(pk=username_id,is_active=True)

	post_id = request.data['post_id']
	data_post = Post.objects.get(pk=post_id)

	body = request.data['body']

	Comment.objects.create(name=data_user,post=data_post,body=body)

	message = {'message':'successfully' }
	return Response(message,status=status.HTTP_200_OK)

# chức năng Xóa bình luận vào bài đăng của User
@api_view(['POST'])
@api_view(['GET'])
def Delete_comments(request):
	comment_id = request.query_params.get('comment_id')
	data_comment = Comment.objects.get(pk=comment_id)
	data_comment.delete()
	message = {'Information_Delete':'Delete Comment_id successfully' }
	return Response(message,status=status.HTTP_200_OK)