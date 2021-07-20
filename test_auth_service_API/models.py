from django.db import models

class Perm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='perms', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        

class Role(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='roles', on_delete=models.CASCADE)
    perms = models.ManyToManyField('Perm', related_name='roles',blank=True)

    class Meta:
        verbose_name_plural = 'roles'