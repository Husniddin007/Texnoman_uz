from .models import Category, Tag


def categories(request):
    categories = Category.objects.all()

    return {'categories': categories}


def tegs(request):
    tags = Tag.objects.all()
    return {'tags': tags}
