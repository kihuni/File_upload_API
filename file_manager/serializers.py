from rest_framework import serializers
from .models import UploadedFile

class UploadedFileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'file_url', 'uploaded_at', 'file_size']
        read_only_fields = ['id', 'uploaded_at', 'file_size', 'file_url']

    def get_file_url(self, obj):
        return obj.file.url