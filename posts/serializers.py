from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta :
        model = Post
        fields = "__all__"

        # # 특정 필드 갖고오기
        # fields = ['writer','content']

        # # 특정 필드 제외하기
        # exclude = ['category']

        # # 읽기 전용 필드 지정
        # read_only_fields = ['writer']    