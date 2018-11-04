from django.shortcuts import render

def wood(request):
    return render(request, 'blog/wood.html')

def jet_impact(request):
    return render(request, 'blog/jet_impact.html')
	
def MCP(request):
    return render(request, 'blog/MCP.html')
# Create your views here.
