#from django.db import connection
from .forms import PostForm
from .models import Post, Reply, Category, Tag
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

app_name = 'blog'
template_name = "blog"

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data)

def get_post_list():
    """게시글 전체 리스트를 가져온다."""
    post_list = Post.objects.prefetch_related('images', 'tags').order_by('-created_at')
    return post_list

def index(request):
    # post_list = get_post_list()
    # context = {'post_list': post_list}
    # return render(request, f'{template_name}/index.html', context)
    page = request.GET.get('page', '1')  # 페이지
    post_list = Post.objects.order_by('-created_at')
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj}
    return render(request, f'{template_name}/post_list.html', context)

def post_list(request):
    # post_list = get_post_list()
    # context = {'post_list': post_list}
    where = {'show_yn': True, 'deleted_at': None}

    page = request.GET.get('page', '1')  # 페이지
    post_list = Post.objects.filter(**where).order_by('-created_at')
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj}
    return render(request, f'{template_name}/post_list.html', context)

def detail(request, post_id):
    """게시글 상세 내용을 가져온다."""
    post = get_object_or_404(Post, id=post_id)
    images = post.images.all()
    tags = post.tags.all()
    context = {
        'post': post,
        'images': images,
        'tags': tags,
    }
    return render(request, f'{template_name}/post_detail.html', context)

tag_delimiter = '#'

def post_write_core(request, post=None):
    """게시글을 작성/수정한다."""
    form = PostForm(instance=post)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        # 태그를 먼저 저장하고 그 결과를 폼에 넣어줍니다.
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_at = timezone.now()
            post.author = request.user
            post.save()
            tags = form.cleaned_data.get('tags')
            if tags:
                post.tags.clear()
                #post.tags.all().delete()
                for tag_name in tags:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)            
            if form.files:
                images = form.files.getlist('images')
                post.images.all().delete()
                for image in images:
                    post.images.create(uploaded_path=image)
            return redirect(f'{app_name}:post_detail', post_id=post.id)
        else:
            return render(request, 'blog/post_write.html', {'form': form, 'categories': categories})
    else:
        return render(request, 'blog/post_write.html', {'form': form, 'categories': categories})

@login_required(login_url='common:login')
def post_write_re(request, post_id):
    """게시글을 수정한다."""
    post = get_object_or_404(Post, id=post_id)
    return post_write_core(request, post)

@login_required(login_url='common:login')
def post_write(request):
    """게시글을 작성한다."""
    return post_write_core(request)


@login_required(login_url='common:login')
def post_remove(request, post_id):
    """게시글을 삭제한다."""
    post = get_object_or_404(Post, id=post_id)
    post.show_yn = False
    post.deleted_at = timezone.now()
    post.save()
    return redirect(f'{app_name}:post_list')


@login_required(login_url='common:login')
def reply_write(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        reply = Reply.objects.create(
            content=content,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            post=post,
            author=request.user,
        )
        return redirect(f'{app_name}:post_detail', post_id=post_id)
    return redirect(f'{app_name}:post_detail', post_id=post_id)

@login_required(login_url='common:login')
def reply_write_re(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    post_id = reply.post.id
    if request.method == 'POST':
        content = request.POST.get('content')
        #create는 새로 만드는거 아닌가? save를 사용해야 하는거 아닌가?
        reply = Reply.objects.create(
            content=content,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            post=reply.post,
            author=request.user,
        )
        return redirect(f'{app_name}:post_detail', post_id=post_id)
    return redirect(f'{app_name}:post_detail', post_id=post_id)