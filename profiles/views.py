from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
def profile(request):
    ''' Display the user's profile '''
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    order = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order': order,
    }

    return render(request, template, context)