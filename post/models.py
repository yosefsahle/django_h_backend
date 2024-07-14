from django.db import models
from user.models import User


class Post(models.Model):
    CATEGORY_CHOICCES=(
        ('FE','Feeds'),
        ('NW','News'),
        ('MP','Market Place')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICCES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='post_image/')

    def __str__(self):
        return f"Image for {self.post.title}"
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.fullname} on {self.post.title}"