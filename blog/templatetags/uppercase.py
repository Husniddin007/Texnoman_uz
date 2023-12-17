from django import template

register = template.Library()


@register.filter
def title_to_uppercase(value):
    return value.lower()


@register.filter
def count_blog(vlue):
    return Blog.objects.filter(category__pk=value).count()