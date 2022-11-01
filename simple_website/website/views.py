from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Gallery, Gallery360, Post
from .forms import GalleryForm
from django.shortcuts import render
from newsapi import NewsApiClient
from django.views import generic


# Create your views here.
class PostList(generic.ListView):  # post list
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):  # post detail
    model = Post
    template_name = 'post_detail.html'


def index(request):  # index
    return render(request, 'index.html')


def gallery(request):  # gallery
    galleries = Gallery.objects.all()
    context = {
        "galleries": galleries
    }
    return render(request, "galleries.html", context)


def gallery_retrieve(request, pk):  # retrieve gallery
    gallery = Gallery.objects.get(id=pk)
    context = {
        "gallery": gallery
    }
    return render(request, "gallery.html", context)


def gallery_create(request):  # create gallery
    form = GalleryForm()  # get form
    if request.method == "POST":  # if method is post
        form = GalleryForm(request.POST, request.FILES)  # get form
        if form.is_valid():  # if form is valid
            form.save()  # save form
            return redirect("/galleries/")  # redirect to gallery

        context = {  # context
            "form": form
        }
        return render(request, "gallery_create.html", context) # render

    context = {  # context
        "form": form
    }
    return render(request, "gallery_create.html", context)  # render


def gallery_update(request, pk):  # update gallery
    gallery = Gallery.objects.get(id=pk)  # get gallery
    form = GalleryForm(instance=gallery)  # get form

    if request.method == "POST":  # if method is post
        form = GalleryForm(request.POST, instance=gallery, files=request.FILES)  # get form
        if form.is_valid():  # if form is valid
            form.save()  # save form
            return redirect("/galleries/")  # redirect to gallery

        context = {  # context
            "form": form
        }
        return render(request, "gallery_create.html", context)  # render

    context = {  # context
        "form": form
    }
    return render(request, "gallery_update.html", context)  # render


def gallery_delete(requests, pk):  # delete gallery
    gallery = Gallery.objects.get(id=pk)
    gallery.delete()
    return redirect("/galleries/")


def about(request):  # about page
    return render(request, 'about.html')


def contact(request):  # contact form
    if request.method == 'POST':  # if method is post
        form = ContactForm(request.POST)  # get form
        if form.is_valid():  # if form is valid
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/contact")

    form = ContactForm()  # contact form
    return render(request, "contact.html", {'form': form})  # contact form


def degree(request):  # 360degree gallery
    images = Gallery360.objects.all()  # get all images
    return render(request, '360degree.html', {'images': images})  # render 360degree.html


def details(request, image_id):  # 360degree gallery details
    image = get_object_or_404(Gallery360, pk=image_id)  # get object or 404
    return render(request, 'details.html', {'image': image})  # render the details page


def faq(request):  # faq page
    return render(request, 'faq.html')


def news(request):  # news api

    newsapi = NewsApiClient(api_key='')  # api key take it from https://newsapi.org/
    top = newsapi.get_top_headlines(sources='techcrunch')  # source of news api

    l = top['articles']  # list of articles
    desc = []  # description
    news = []  # news
    img = []  # image

    for i in range(len(l)):  # loop for news api
        f = l[i]
        news.append(f['title'])  # title of news
        desc.append(f['description'])  # description of news
        img.append(f['urlToImage'])  # image of news
    mylist = zip(news, desc, img)  # zip all the news

    return render(request, 'news.html', context={"mylist": mylist})  # render the news api
