from django.urls import reverse
from django.urls import reverse_lazy

from djangoapp.models import *
from django.shortcuts import render, HttpResponse
from jsignature.utils import draw_signature
from jsignature.utils import draw_signature
from jsignature.utils import draw_signature
from djangoapp.forms import SignatureForm
from .models import SignatureModel


def my_view(request):
    signature = SignatureModel.objects.filter(id=4)

    context = {}
    context['formss'] = SignatureForm()
    context['user_name'] = 'Sarwar'
    form = SignatureForm(request.POST or None)

    if form.is_valid():
        signature = form.cleaned_data.get('signature')
        if signature:
            # as an image
            signature_picture = draw_signature(signature)
            # or as a file
            signature_file_path = draw_signature(signature, as_file=True)
            SignatureModel.objects.create(signature=signature,
                                          signature_txt=signature)
            print('Successful!!')
        return render(request, "index.html", context)
    return render(request, "index.html", context)
    # return render(request, "signature.html", {'object_list': signature})

