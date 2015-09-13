from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c), content_type='text/html; charset=UTF-8')
#    return render_to_response('polls/index.html', locals())

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
#    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/details.html', {'poll': p},
                              context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        seleceted_choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('polls/details.html',
                                  {'poll': p, 'error_message': "You didn't select a choice."},
                                  context_instance=RequestContext(request))
    else:
        seleceted_choice.votes += 1
        seleceted_choice.save()
        return HttpResponseRedirect(reverse('polls.polls_views.results', args=(p.id, )))
