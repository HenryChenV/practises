from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        seleceted_choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('polls/detail.html',
                                  {'poll': p, 'error_message': "You didn't select a choice."},
                                  context_instance=RequestContext(request))
    else:
        seleceted_choice.votes += 1
        seleceted_choice.save()
        return HttpResponseRedirect(reverse('poll_results', args=(p.id, )))
