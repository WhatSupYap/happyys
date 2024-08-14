from django.shortcuts import render, redirect

# Create your views here.
from samples.forms import DocumentForm

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_upload_success')
    else:
        form = DocumentForm()
    return render(request, 'samples/fileupload.html', {'form': form})