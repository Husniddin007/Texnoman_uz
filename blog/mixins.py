from .models import Comment, Category, Tag


class Base:

    def category(self):
        return Category.objects.all()

    def tag(self0):
        return Tag.objects.all()
