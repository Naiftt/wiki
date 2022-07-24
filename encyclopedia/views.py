from django.shortcuts import render
from . import util
from django.http import HttpResponse
import markdown
import sys
import numpy as np 
import json
from django.shortcuts import redirect
from django.utils.translation import get_language
from django.contrib import messages


# util.list_entries is a list ['CSS', 'Django', 'Git', 'HTML', 'Python']
from django import forms






def index(request):
    if request.method == "POST":

         if 'edit' in request.META.get('HTTP_REFERER'):
             
            new_name = request.POST['T']
            content = request.POST['con']
            f = open(f"entries/{new_name}.md", 'w')
            f.write(content)
            f.close()
         elif 'create' in request.META.get('HTTP_REFERER'):
             title = request.POST['T']
             content = request.POST['con']
             
             if title in util.list_entries():
                return render(request, 'new/error.html')
             else:
                f = open(f"entries/{title}.md", 'w')
                f.write(content)
                f.close()
                 




    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "random": util.list_entries()[np.random.randint(0, len(util.list_entries()))]
    })


def ency(request, name):
    text = "<!DOCTYPE html>"
    if name in util.list_entries():
        with open(f"/Users/naif_tayseer/Desktop/Summer_courses/CS50_WEB/wiki/entries/{name}.md", "r", encoding="utf-8") as input_file:
            text = text + input_file.read()

        # home page button
        text = text + f"<title>{name}</title>"
        text = text + f"<form  action='http://127.0.0.1:8000/wiki/{name}/edit'> <input style='font-weight: bold; color: brown;' type='submit' value='Edit Page' />   </form>"
        text = text + "\n \n  [Click to Go Back to Home Page](/wiki)"
        # convert to html
        html = markdown.markdown(text)    
        response = HttpResponse()
        # Adding the title to the html file 
        response.write(html)
        # ading the edit button 

        return response
    else: 
        return render(request, "notexist/index.html")
    

def search(request, name):
    if request.method == "POST":
        print("POST")
    else:
        print("GET")
    search_results = []
    for w in util.list_entries(): 
        if name.lower() in w.lower(): 
            search_results.append(w)
    print(search_results)
    return render(request, "search/search_ven.html", 
   {"search_results":search_results})



def create(request): 
    class TitleForm(forms.Form):
        T = forms.CharField(label = "Title") 
        

    class ContentForm(forms.Form):
        con = forms.CharField(label = "",
        widget = forms.Textarea(attrs={'rows':2, 'cols':10, 
        'style': 'height: 25em;'})
        )
        

    return render(request, "new/create.html", 
    {"Title": TitleForm(), 
    "Content": ContentForm()  } )

def new_page(request): 
    if request.method == "POST":
        pass

def edit(request, name):
    content = util.get_entry(name)
    class TitleForm(forms.Form):
        T = forms.CharField(label = "Title", initial = name) 
        

    class ContentForm(forms.Form):
        con = forms.CharField(label = "", initial = content, 
        widget = forms.Textarea(attrs={'rows':2, 'cols':10, 
        'style': 'height: 25em;'})
        )
        

    return render(request, "new/edit.html", 
    {"title": name,
    "Title": TitleForm(), 
    "Content": ContentForm()  } )