from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import sqlite3
# Create your views here.
def home(request):
    return HttpResponse('Welcome to our site!')
def api(request):
    return JsonResponse(show_jokes())
def show_jokes():
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    sql = """
    SELECT * FROM blog_joke;
    """
    cursor.execute(sql)
    info = cursor.fetchall()
    id = []
    category = []
    joke = []
    published_time = []
    dic = {}
    for b in info:
        id.append(b[0])
        category.append(b[1])
        joke.append(b[2])
        published_time.append(b[3])
    for x,y,z,c in zip(id,category, joke, published_time):
        dic.update({x:{"category": y, "joke": z, "published time": c}})
    connection.commit()
    connection.close()
    return dic
    