from django.db import models
from django.http.response import Http404
from django.urls import reverse


class Activeable(models.Model):
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Nameable(models.Model):
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        abstract = True


class ObjectManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

    def get_object_or_404(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            raise Http404(
                'No %s matches the given query.' %
                self.model._meta.object_name)

    def get_list_or_404(self, **kwargs):
        obj_list = list(self.filter(**kwargs))
        if not obj_list:
            raise Http404(
                'No %s matches the given query.' %
                self.model._meta.object_name)
        return obj_list


class Permalinkable(models.Model):
    slug = models.SlugField(blank=True, max_length=500)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse(self.url_name, args=[str(self.slug)])


class Publishable(models.Model):
    publish_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    def publish_on(self, date=None):
        from django.utils import timezone
        if not date:
            date = timezone.now()
        self.publish_date = date
        self.save()

    @property
    def is_published(self):
        from django.utils import timezone
        return self.publish_date < timezone.now()


class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
