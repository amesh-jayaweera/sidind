from django.shortcuts import render
import pymongo
from django.http import HttpResponseRedirect

client = pymongo.MongoClient("mongodb+srv://testuser:123@cluster0.ntwjz.mongodb.net/socialmedia?retryWrites=true&w=majority")
db = client.socialmedia

def init():
    # DB Connection
    # serverStatusResult = db.command("serverStatus")
    # print(serverStatusResult)
    posts = db["linkedin_posts"]
    return posts.find()

def index(request):
    return render(request,'index.html',{'data' : init()})


def addComment(request):
    comment = request.POST['comment']
    id = request.POST['id']
    posts = db["linkedin_posts"]
    posts.update({'id' : id},{'$push' : {'comments' : comment}})
    #return render(request, 'index.html', {'data': init()})
    return HttpResponseRedirect('/')