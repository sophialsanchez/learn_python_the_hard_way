from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import FormView
from django.utils import timezone

from polls.models import Room
from polls.forms import ResponseForm

class IndexView(generic.ListView):
	model = Room # tells the generic view which model to act upon
	template_name = 'polls/index.html'
	context_object_name = 'rooms'
	def get_queryset(self):
		rooms = Room.objects.all()
		return rooms
		
	
class DetailView(generic.DetailView):
	model = Room # tells the generic view what model to act upon
	template_name = 'polls/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['form'] = ResponseForm
		return context

def Response(request, slug):
	response = request.POST.get("response")
	form = ResponseForm
	room = Room.objects.get(slug=slug)
   
    # redisplay the room with an error message if form blank
	if(response == ""):
		return render(request, 'polls/detail.html', {'form': form, 'room': room, 'error': "You have to enter a response!", 'slug': slug})
	# check if the response matches a key in the dictionary
	else:
		room_dictionary = Room.objects.get(slug=slug).dictionary
		if (response.lower() in room_dictionary):
			next_room = room_dictionary[response.lower()]
			return HttpResponseRedirect(reverse('polls:detail', kwargs={'slug': next_room}))
		else:
			return render(request, 'polls/detail.html', {'form': form, 'room': room, 'error': "Hmm, that doesn't look quite right. Try something else!", 'slug': slug})

		
		
		