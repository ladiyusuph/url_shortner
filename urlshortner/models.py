from django.db import models
import random
import string


class UrlShortner(models.Model):
    url = models.URLField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.slug} - {self.url}"

    def save(self, *args, **kwargs):
        self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        slug = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        while UrlShortner.objects.filter(slug=slug).exists():
            slug = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        return slug
