from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from codes.models import problem

def home( req ):
    #problem.objects.all().delete()
    problems = problem.objects.all()
    return render_to_response( 'base.html', locals() )

def add( req ):
    if req.method == 'POST':
        problem(number=req.POST[ 'number' ], 
                comment=req.POST[ 'comment' ]).getDescription().getSolution().save()
        return HttpResponse('You ded it')
    return render_to_response( 'add.html', csrf( req ) )

