from products.models import Category



def add_variable_to_context(request):

    categories = Category.objects.all()

    doctors = [
        "William Hartnell", "Patrick Troughton",
        "Jon Pertwee", "Tom Baker", "Peter Davison",
        "Colin Baker", "Sylvester McCoy", "Paul McGann",
        "Christopher Eccleston", "David Tennant", "Matt Smith",
        "Peter Capaldi", "Jodie Whittaker", "Ncuti Gatwa"
    ]  

    return {
        'categories': categories,
        'doctors': doctors,
    }