from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import MovieForm
from myapp.models import Movies
from django.contrib import messages

# Create your views here.

# view for creating movie add

class MovieCreateView(View):
    def get(self,request,*args,**kwargs):

        form_instance=MovieForm()
        return render(request,"movieadd.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data
            Movies.objects.create(**data)
            messages.success(request,"movie added successfully")

            return redirect("movie-list")
        else:
            messages.error(request,"failed to add movie")
            return render(request,"movieadd.html",{"form":form_instance})

class MovieListView(View):
    def get(self,request,*args,**kwargs):
        qs=Movies.objects.all()
        return render(request,'movielist.html',{"movies":qs})

class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movies.objects.get(id=id)
        return render(request,'movie_detail.html',{"movie":qs})

class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movies.objects.get(id=id).delete()
        return redirect("movie-list")

class MovieUpdateView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        movie_obj=Movies.objects.get(id=id)
        movie_dict={
            "title":movie_obj.title,
            "genre":movie_obj.genre,
            "language":movie_obj.language,
            "year":movie_obj.year,
            "run_time":movie_obj.run_time,
            "director":movie_obj.director
        }
        form_instance=MovieForm(initial=movie_dict)
        return render(request,'movieedit.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data
            id=kwargs.get("pk")
            Movies.objects.filter(id=id).update(**data)

            messages.success(request,"movie has been changed!")
            return redirect('movie-list')
        else:
             messages.error(request,"movie failed to change!")
             return render(request,'movieedit.html',{"form":form_instance})

class HomeView(View):
    def get(self,request,*args,**kwargs):

        return render(request,'home.html')
