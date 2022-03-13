from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=False, null=False)
    github = models.URLField(blank=False, null=False)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='profile_pics')

    def get_absolute_url(self):
        return reverse('blog_app:post_list')

    def __str__(self):
        return self.user

# class CategoryTag(models.Model):
#     tag = models.CharField(max_length=30)

#     def get_absolute

#     def __str__(self):
#         return self.tag

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    image = models.ImageField(blank=True, null=True, upload_to='profile_pics')
    text = models.TextField()
    tag = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now())
    date_published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Gets the time when the post is published."""
        self.date_published = timezone.now()
        self.save()

    # def approve_comments(self):
    #     return self.comments.filter(approved_comment=True)
        # self.comments = filter(approved_comment, self.comments)
        # return self.comments

    def get_absolute_url(self):
        return reverse("blog_app:detail", kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=128)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now())
    # approved_comment = models.BooleanField(default=False)

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.user.username +  " Comment: " + self.content
