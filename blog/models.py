from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def attachment_directory_path(instance, filename):
    # The file will be uploaded to MEDIA_ROOT/posts/<post_id>_<filename>
    return f'posts/{instance.id}_{filename}'


class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=360)
    attachment = models.FileField(upload_to=attachment_directory_path)
    likes_count = models.BigIntegerField(default=0)
    comments_count = models.IntegerField(default=0)


class Like(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_like')
        ]


@receiver(post_save, sender=Like, dispatch_uid="update_likes_count")
def update_likes_count(sender, instance, **kwargs):
    instance.post.likes_count += 1
    instance.post.save()


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=360)


@receiver(post_save, sender=Comment, dispatch_uid="update_comments_count")
def update_comments_count(sender, instance, **kwargs):
    instance.post.comments_count += 1
    instance.post.save()
