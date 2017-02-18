from django.shortcuts import render
import random
from models import PickUpLine



def index(request):
	#line = PickUpLine.objects.get()

	return render(request,'sendLine/lol.html',{})
