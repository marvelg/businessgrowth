from .models import Link
from .models import Address
from .models import Detail

def add_variable_to_context(request):
    return {
        'Link': Link.objects,
        'Address': Address.objects,
        'Detail': Detail.objects
    }
