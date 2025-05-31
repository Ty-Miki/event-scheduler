from django.shortcuts import render

def home(request):
    """
    Render the home page of the event scheduler application.
    
    Args:
        request: The HTTP request object.
        
    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'accounts/home.html')
