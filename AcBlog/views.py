from django.shortcuts import render


def main_page(request):
    # num = 10
    # context = {
    #     'article_num': num
    # }
    article_list = ["菜鸟教程", "菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, 'main_page.html', {"article_list": article_list})
