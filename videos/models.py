from django.db import models

class Category(models.Model):
    # for handling subcategories i do this below technique 
    parent = models.ForeignKey('self',
                               verbose_name='parent',
                               blank=True,
                               null=True,
                               on_delete=models.CASCADE)
    # if we delete the parent categories the child will be deleted too 
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='categories')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'categories' # name of the table in database
         verbose_name = 'Category' # name in admin 
         verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
         


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='vidoes/')
    is_enable = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, verbose_name='categories', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)    

    class Meta:
         db_table = 'vidoes' # name of the table in database
         verbose_name = 'Video' # name in admin 
         verbose_name_plural = 'Videos'
    def __str__(self):
        return self.title


# i have created this because we may have several videos that are related to each other
# i assumed we have series like rick and morty which have the same avatar and title
class File(models.Model): 
    video = models.ForeignKey(
        Video,
        verbose_name='video',
        related_name='files',
        on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)    
    
    class Meta:
         db_table = 'files' # name of the table in database
         verbose_name = 'File' # name in admin 
         verbose_name_plural = 'Files'
    def __str__(self):
        return self.title