from rest_framework import serializers,validators
from .models import *
from rest_framework.validators import ValidationError
from django.conf import settings 
from rest_framework.response import Response
from rest_framework import status
import requests


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('id','username','email','password','user_Member')
		extra_kwargs = {'password': {'write_only': True}}


# //////////////////////////////////////////////////////////////////////////////////////////////////

class MemberSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	class Meta:
	    model=Member
	    fields='__all__'

	# parser_classes = (MultiPartParser, FormParser)

class UserSerializer(serializers.ModelSerializer):
	user_Member = MemberSerializer()
	class Meta:
		model=User
		fields=('id','username','email','password','user_Member')
		extra_kwargs = {'password': {'write_only': True}}


class Image_PostSerializer(serializers.ModelSerializer):
	class Meta:
		model=Image_Post
		fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
	name = UserSerializer(read_only=True)
	class Meta:
		model=Comment
		fields='__all__'

class PostSerializer(serializers.ModelSerializer):
	# user = UserSerializer(read_only=True)
	post_image = Image_PostSerializer(many=True,read_only=True)
	uploaded_images = serializers.ListField(child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),write_only=True)
	comments_post = CommentSerializer(many=True,read_only=True)

	class Meta:
		model=Post
		fields='__all__'

	def create(self,validated_data):
		uploaded_images = validated_data.pop("uploaded_images")
		post = Post.objects.create(**validated_data)
		for image in uploaded_images:
		    newproduct_image = Image_Post.objects.create(post=post, Image_post=image)
		return validated_data


