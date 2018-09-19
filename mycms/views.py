from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Articles

# Create your views here.
class IndexView(generic.ListView):
  template_name = 'index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """Return the last five published questions."""
    return Articles.objects.order_by('id')[:5]


class ListView(generic.ListView):
  template_name = 'list.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """Return the last five published questions."""
    return Articles.objects.order_by('id')[:5]


class DetailView(generic.ListView):
  template_name = 'detail.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """Return the last five published questions."""
    return Articles.objects.order_by('id')[:5]