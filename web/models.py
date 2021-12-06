from django.db import models


class Gallery(models.Model):
    image=models.ImageField(upload_to="gallery/")
    category=models.ForeignKey("web.Category",on_delete = models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.category)


class Category(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Detail(models.Model):
    image = models.FileField(upload_to="detail/")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title