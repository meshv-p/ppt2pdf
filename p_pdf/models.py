from django.db import models

# Create your models here.
class files(models.Model):
    file_name=models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='files', max_length=100)
    extension = models.CharField( default='',max_length=50)
    
    def __str__(self):
        return self.file_name 
    
    @property
    def filename(self):
        return self.file.name # os.path.basename(self.audio_file.path)

