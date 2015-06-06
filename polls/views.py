from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll, Choice
# Create your views here.

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	
	#output = ', '.join([p.question for p in latest_poll_list])	
	return render_to_response('polls/index.html', {'latest_poll_list' : latest_poll_list})
	
def detail(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/detail.html', {'poll': p})
	
def results(request, poll_id):

	return HttpResponse("Your are lookin' results of poll #  %s." % poll_id)
	
def vote(request, poll_id):

	return HttpResponse("Your are votin' on poll #  %s." % poll_id)
	
