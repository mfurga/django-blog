from django.utils.text import slugify

import random
import string


def random_string(length=4):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def slug_generator(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug:
        slug = new_slug
    Post = instance.__class__
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        new_slug = '{slug}-{random}'.format(slug=slug, random=random_string())
        return slug_generator(instance, new_slug=new_slug)
    return slug
