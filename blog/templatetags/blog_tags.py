from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=3):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

