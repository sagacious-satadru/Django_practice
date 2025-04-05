from django.shortcuts import render

# Create your views here.
def all_chai(request):
    return render(request, 'chaibreak/all_chai.html')