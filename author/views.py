from django.shortcuts import render

# Create your views here.




def author(request, pk):
    return render(request, 'author.html')
