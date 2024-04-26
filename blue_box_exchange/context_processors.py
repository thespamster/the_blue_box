from products.models import Category
from home.models import Doctors



def add_variable_to_context(request):

    categories = Category.objects.all()
    doctors = Doctors.objects.all()

    return {
        'categories': categories,
        'doctors': doctors,
    }