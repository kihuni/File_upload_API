from django.test import TestCase
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import UploadedFile

class FileUploadTests(TestCase):
    def setUp(self):
        self.client = APIClient()  # No authentication needed
        
    def test_upload_file(self):
        file_content = b'Test content'
        test_file = SimpleUploadedFile('test.txt', file_content)
        response = self.client.post('/api/upload/', {'file': test_file}, format='multipart')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(UploadedFile.objects.count(), 1)
        self.assertEqual(UploadedFile.objects.first().file_size, len(file_content))
        
    def test_list_files(self):
        file_content = b'Test content'
        test_file = SimpleUploadedFile('test.txt', file_content)
        UploadedFile.objects.create(file=test_file)
        
        response = self.client.get('/api/files/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        
    def test_retrieve_file(self):
        file_content = b'Test content'
        test_file = SimpleUploadedFile('test.txt', file_content)
        uploaded_file = UploadedFile.objects.create(file=test_file)
        
        response = self.client.get(f'/api/files/{uploaded_file.id}/')
        self.assertEqual(response.status_code, 200)
        # Read streaming content for FileResponse
        content = b''.join(response.streaming_content)
        self.assertEqual(content, file_content)
        
    def test_delete_file(self):
        file_content = b'Test content'
        test_file = SimpleUploadedFile('test.txt', file_content)
        uploaded_file = UploadedFile.objects.create(file=test_file)
        
        response = self.client.delete(f'/api/files/{uploaded_file.id}/delete/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(UploadedFile.objects.count(), 0)