from django.shortcuts import render

# Create your views here.
def home(request):
    """Home page with login and registration options"""
    # # Get all active doctors for display
    # active_doctors = User.objects.filter(
    #     user_type=User.UserType.DOCTOR,
    #     is_active=True
    # ).order_by('first_name')
    
    context = {
        'active_doctors': 'active_doctors'
    }
    return render(request, 'portfolio/home.html', context)
