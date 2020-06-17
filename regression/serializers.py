from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Image




class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','title','picture_target',"picture1","picture2","picture3","picture4","picture5","picture6", "picture_predicted" , 'beta',"uploaded"]
        
