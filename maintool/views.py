from django.shortcuts import redirect, render
from .slvfunction import returnlinks
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

def index(request):
    # all_albums = Album.objects.all()
    # # template=loader.get_template('firstapp/index.html')
    # context = {
    #     "all_albums": all_albums,
    # }
    # html = ''
    # for album in all_albums:
    #     path = '/firstapp/' + str(album.id) + '/'
    #     html+= '<a href="' + path + '">' +album.album_title+ '</a><br>'
    # return HttpResponse (template.render(context,request))
    return render(request, "maintool/index.html")

def take_input(request):
    # try:
    title = request.POST["our_title"]
    if not title:
        return render(request,"maintool/index.html", {'message':"Kindly Enter Title!"} )
    link_to_book = returnlinks(title)
    html = ""
    html+= '<p>' + str(title) + '</p><br>'
    # return HttpResponse (link_to_book)
    
    if (link_to_book=="NONE"):
        # We would like you to note that we use titles exactly from LibGen.
        return render(request,"maintool/index.html",{'message':"Sorry, we could not find any book! We suggest modifying the title and/or using a smaller part of the title and retrying. "})
    else:
        return redirect(link_to_book)
    # except (KeyError, Song.DoesNotExist):
    #     return render(request,"waste/detail.html",{
    #         'album' : album,
    #         'error_message' : "please select a valid song"
    #          })
    # else:
        # selected_song.is_favorite = True
        # selected_song.save()
        # return render(request,"maintool/slvfunction.html",{'title' : title}) 
def NoBook(request,message):
    context={
        'message':message
    }
    return render(request,"maintool/error.html",context)
# def index(request):
#     # all_albums = Album.objects.all()
#     # # template=loader.get_template('firstapp/index.html')
#     # context = {
#     #     "all_albums": all_albums,
#     # }
#     html = ''
#     all_albums=returnlinks("Pride and Prejudice")
#         # path = '/firstapp/' + str(album.id) + '/'
#     html+= '<p>' +all_albums + '</p><br>'
#     return HttpResponse (html)
#     # return render(request, "maintool/index.html")