import codecs

import markdown
from django.http import HttpResponse
from django.shortcuts import render
from ArticleModel.models import Article


def main_page(request):
    article_list = Article.objects.all()
    article_list_length = article_list.count()
    # article_path = "<a href=\'127.0.0.1:8000/article/"+"p1"+"\'>点击跳转</a>"

    item_list = []

    for index in range(article_list_length):
        model_object = Article.objects.get(id=index + 1)
        article_path = "<a href=\'/article/" + str(index + 1) + "\'>阅读完整文章 >></a>"
        item_title = model_object.getTitle
        item_subtitle = model_object.getTime
        item_about = model_object.getAbout
        item = {
            "title": item_title,
            "subtitle": item_subtitle,
            "about": item_about,
            "path": article_path
        }
        item_list.append(item)

    return render(request, 'main_page.html', {
        "article_list": item_list,
        "num_test": article_list_length,
        "article_path": article_path
    })


def article_page(request, article_path):
    if is_number(article_path):
        target_id = int(article_path)
        model_object = Article.objects.get(id=target_id)
        text = model_object.text
        text = str(text)

        html = markdown.markdown(text, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.abbr',
            'markdown.extensions.attr_list',
            'markdown.extensions.md_in_html',
            'markdown.extensions.nl2br',
            'markdown.extensions.codehilite'
        ])
        #
        # # 转为 html 文本
        # html = markdown.markdown(text)
        #
        # # 保存为文件
        # print(html)

        return render(request, 'article_page.html', {
            "text": html
        })
    else:
        response = render(request, '404.html', )
        response.status_code = 404
        return response


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
