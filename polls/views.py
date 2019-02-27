from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

# Create your views here.

#def index(request):
#    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)
#
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/cart_detail.html', {'question': question})
#
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})


#-- Codes for logging
import logging
logger = logging.getLogger(__name__)


#-- Class-based GenericView
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/cart_detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#--Function-based View
def vote(request, question_id):
    logger.debug("vote().question_id: %s"%question_id)
    question = get_object_or_404(Question, pk=question_id)

    try:
        seleceted_choice= question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        #설문투표 폼을 다시 보여준다.
        return render(request, 'polls/cart_detail.html', {
            'question':question,
            'error_message':"You didn't select a choice",

        })

    else:
        seleceted_choice.votes += 1
        seleceted_choice.save()
        #POST데이터를 정상적으로 처리하였으면,
        #항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

