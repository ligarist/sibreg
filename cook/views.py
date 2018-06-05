from django.shortcuts import render, get_object_or_404
from .models import Cook

# Страница с товарами
def CookList(request, ):
    recipes = Cook.objects.filter()
    return render(request, 'recipe/post.html', {
        'recipes': recipes
    })


# Страница товара
def CookDetail(request, id, slug):
    recipe = get_object_or_404(Cook, id=id, slug=slug)
    return render(request, 'recipe/postpod.html', {'recipe': recipe})



