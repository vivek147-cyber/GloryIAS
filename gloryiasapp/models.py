from django.db import models

# Create your models here.
# class bookfreeclass(models.Model):
#     name=models.CharField(default='',max_length=50)
#     email=models.EmailField(default='',max_length=100)
#     contactNumber=models.IntegerField(default='')
#     whatsappNumber=models.IntegerField(default='')


    # def __str__(self):
    #     return self.name

class contactform(models.Model):
    name=models.CharField(default='',max_length=50)
    email=models.EmailField(default='',max_length=100)
    contactNumber=models.IntegerField(default='')
    whatsappNumber=models.IntegerField(default='')
    query=models.TextField()


    def __str__(self):
        return self.name


# class feedbackform(models.Model):
#     name=models.CharField(default='',max_length=50)
#     classes=models.CharField(default='',max_length=100)
#     contactNumber=models.IntegerField(default='')
#     feedback=models.TextField()


#     def __str__(self):
#         return self.name


class featuredCourse(models.Model):
    name=models.CharField(default='',max_length=100)
    image=models.ImageField(default='', upload_to='attachments/')
    description1=models.CharField(default='',max_length=100)
    description2=models.CharField(default='',max_length=100)
 
    def __str__(self):
        return self.name


class popularCourse(models.Model):
    name=models.CharField(default='',max_length=100)
    image=models.ImageField(default='', upload_to='attachments/')
 
    def __str__(self):
        return self.name


class teacher(models.Model):
    name=models.CharField(default='',max_length=100)
    subject=models.CharField(default='',max_length=100)
 
    def __str__(self):
        return self.name

class gallery(models.Model):
    image=models.ImageField(default='', upload_to='attachments/')

 