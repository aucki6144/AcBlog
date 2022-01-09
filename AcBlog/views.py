import codecs

import markdown
from django.http import HttpResponse
from django.shortcuts import render

import SiteConfig
from ArticleModel.models import Article
from SiteConfig.models import AboutSite, HeaderNotice, Contact, FriendUrl


def main_page(request):
    # Notice:
    notice_list = HeaderNotice.objects.all()
    notice_list_length = notice_list.count()
    notice_object = HeaderNotice.objects.get(id=notice_list_length)
    notice_show = notice_object.is_show
    notice_content = notice_object.content

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
        "article_path": article_path,
        "notice_show": notice_show,
        "notice_content": notice_content
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

        return render(request, 'article_page.html', {
            "text": html
        })
    else:
        response = render(request, '404.html', )
        response.status_code = 404
        return response


def about_page(request):
    about_text_list = AboutSite.objects.all()
    about_text_list_length = about_text_list.count()
    model_object = AboutSite.objects.get(id=about_text_list_length)
    text = model_object.content
    text = str(text)

    html = markdown.markdown(text, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.abbr',
        'markdown.extensions.attr_list',
        'markdown.extensions.md_in_html',
        'markdown.extensions.nl2br',
    ])

    return render(request, 'about_page.html', {
        "text": html
    })


def contact_page(request):
    contact_list = Contact.objects.all()
    contact_list_length = contact_list.count()

    item_list = []

    for index in range(contact_list_length):
        model_object = Contact.objects.get(id=index + 1)
        item_title = model_object.title
        item_linkSrc = model_object.linkSrc
        item = {
            "title": item_title,
            "path": item_linkSrc,
            "imgsrc":model_object.imageSrc
        }
        item_list.append(item)

    return render(request, 'contact.html', {
        "contact_list": item_list,
    })


def furl_page(request):
    fUrl_list = FriendUrl.objects.all()
    fUrl_list_length = fUrl_list.count()

    item_list = []

    for index in range(fUrl_list_length):
        model_object = FriendUrl.objects.get(id=index + 1)
        item = {
            "imageSrc": model_object.imageSrc,
            "title": model_object.title,
            "subtitle": model_object.subtitle,
            "url": model_object.url
        }
        item_list.append(item)

    return render(request, 'furl_page.html', {
        "furl_list": item_list,
    })


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
