from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,reverse
from django.http import HttpResponse
# Create your views here.
from .models import Question,Choice
from django.views import  generic

    
class QuestionClass(generic.ListView):
    template_name="index.html"
    context_object_name="all_qq"

    def get_queryset(self):
        return Question.objects.all().order_by('-id')[2:]

class SingleQuestion(generic.DetailView):
    template_name="singledata.html"
    context_object_name="single_q"
    model = Question
    

def choice_view(request):
    all_c=Choice.objects.all()
    context={
        'all_c':all_c
    }
    return render(request,"choice.html",context)


def vote(request,question_id):
    question=get_object_or_404(Question,id=question_id)
    try:
        selected_answer=question.choice_set.get(id=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        context={
            "single_q":question,
            "error":"then message does not exist"


        }
        return render(request,'singledata.html',context)
    else:
        selected_answer.votes +=1
        selected_answer.save()
    return HttpResponseRedirect(reverse('DjangoBanglaApp:result', args=(question.id,)))
















def results_showing(request,question_id):
    resutls=get_object_or_404(Question,pk=question_id)
    return render(request,"resutls.html",{'resutls':resutls})