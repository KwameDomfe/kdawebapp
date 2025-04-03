from django.contrib.auth.models import User
from django.db import models
# from django.db.models.query import QuerySet
from django.utils import timezone

class Category(models.Model):
    name=models.CharField(
        max_length=128
    )

    def __str__(self):
        return self.name
    
class Post(models.Model):
    # Custom Manager
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    # Options
    options=(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # Variables
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        default=1
    )
    
    title = models.CharField(
        max_length = 250
    )
    excerpt = models .TextField(null=True)
    content = models .TextField(null=True)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='published'
    )
    published= models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    status = models.CharField(
        max_length=32,
        choices=options,
        default='published'
    )
    objects = models.Manager() # default Manager
    postobjects = PostObjects() # Custom Manager
    
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title