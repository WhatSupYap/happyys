import json, os
from .models import SampleDoc, UploadFile
from common.utils import fileUtils as fs, convert_dt_to_str, rename_keys
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from samples.forms import filetestForm
from django.db import transaction, IntegrityError


def goto_sample(request, sample_no):
    if sample_no == 1:
        form = filetestForm()
        return render(request, 'samples/fileupload.html', {'form': form})
    elif sample_no == 2:
        return render(request, 'samples/fileupload2.html')
    else:
        return redirect('/error/404')

# Create your views here.
def upload_file(request):
    """Upload a file"""
    
    if request.method == 'POST':
        form = filetestForm(request.POST, request.FILES)
        if form.is_valid():
            saved_file = form.save()
            return render(request, 'samples/fileupload.html', {'form': form, 'saved_file': saved_file})
    else:
        form = filetestForm()
    return render(request, 'samples/fileupload.html', {'form': form})

@csrf_exempt
def upload_file2(request):
    if request.method == 'POST':
        new_file_name = ""
        try:
            file = request.FILES['file']  # Assuming the file input field name is 'file'
            save = fs.save_file(file)

            return render(request, 'samples/fileupload2.html')  # Replace 'success_url' with the URL to redirect after saving the file
        except Exception as e:
            return render(request, 'samples/error.html', {'error_message': str(e)})  # Replace 'error.html' with the template for displaying the error message
    else:
        return render(request, 'samples/fileupload2.html')  # Replace 'error_url' with the URL to redirect if the request method is not POST

@csrf_exempt
def add_sampledoc(request):
    try:
        with transaction.atomic():
            if request.method == 'POST':
                title_ = request.POST.get('title')
                content_ = request.POST.get('content')
                sampledoc = SampleDoc(title=title_, content=content_)
                sampledoc.save()

                file = request.FILES['file']
                save = fs.save_file(file)
                
                uploadfile = UploadFile(sampledoc=sampledoc, file=save['new_file_Path'], original_file_name=save['orginal_file_name'])
                uploadfile.save()
                rtn = json.dumps({'status': 'ok', 'message': ''})
            else:
                rtn = json.dumps({'status': 'ok', 'message': 'GET method is not allowed'})
    except IntegrityError as e:
        # 데이터베이스 관련 예외 처리
        rtn = json.dumps({'status': 'error', 'message': str(e)})
    except Exception as e:
        rtn = json.dumps({'status': 'error', 'message': str(e)})
    finally:
        return HttpResponse(rtn, content_type='application/json')    

def get_sampledoc(request):
    tb_name = 'uploadfile'
    columns = [
        "title",
        "content",
        "uploaded_at",
        f'{tb_name}__file',
        f'{tb_name}__original_file_name'
    ]
    key_map = {
        "title": "title",
        "content": "content",
        "uploaded_at": "uploaded_at",
        f"{tb_name}__file": "file_name",
        f"{tb_name}__original_file_name": "ori_file_name" 
    }
    where = {f'{tb_name}__idx': 0}

    sampledoc = SampleDoc.objects.filter(**where).select_related(tb_name).values(*columns)
    data = list(sampledoc)
    # Convert datetime objects to strings
    data = convert_dt_to_str(data)
    # Rename keys
    data = rename_keys(data, key_map)
    # Convert the List to JSON
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
