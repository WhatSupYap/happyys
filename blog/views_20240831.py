#from django.db import connection
from .models import Post, Reply, Category, Tag
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.exceptions import ValidationError

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

    page = request.GET.get('page', '1')  # 페이지
    post_list = Post.objects.order_by('-created_at')
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj}
    return render(request, f'{template_name}/post_list.html', context)

def detail(request, post_id):
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

def post_write_re(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    template_name = 'blog/post_write.html'    
    category_list = Category.objects.all()
    context = {'p_category_list': category_list}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        tags = request.POST.get('tags')
        images = request.FILES.getlist('images')
        context['p_title'] = title
        context['p_content'] = content
        context['p_category_id'] = category_id
        context['p_tags'] = tags
        context['p_images'] = images
        try:
            #raise Exception('테스트 에러 발생')
            if not category_id or not category_id.isdigit():
                raise ValidationError({'category': '카테고리를 선택해주세요.'})
            # 카테고리 객체 가져오기
            category = get_object_or_404(Category, id=category_id)
            # Post 객체 생성
            post = Post(
                title=title,
                content=content,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                category=category,
                author=request.user,
            )
            # 모델 유효성 검사 수행
            post.full_clean()
             # 유효성 검사 통과 시, Post 객체 저장
            post.save()
            # 새로 생성된 Post 객체의 ID 가져오기
            new_post_id = post.id
            # 태그 처리
            if tags:
                tags = tags.split('#')
                for tag_name in tags:
                    tag = Tag.objects.get_or_create(name=tag_name.strip())
                    post.tags.add(tag)
            # 이미지 처리
            if images:
                for image in images:
                    post.images.create(image=image)
            return redirect('blog:post_detail', post_id=new_post_id)
        except ValidationError as e:
            # 유효성 검사 실패 시, 오류 메시지와 함께 폼 다시 렌더링
            #context['errors'] = e.message_dict
            context['vaild_errors'] = e.message_dict
            return render(request, template_name, context )
        except Exception as e:
            context['error'] = str(e)
            return render(request, template_name, context )
    else:
        return render(request, template_name, context )

def post_write(request):
    template_name = 'blog/post_write.html'
    category_list = Category.objects.all()
    context = {'p_category_list': category_list}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        tags = request.POST.get('tags')
        images = request.FILES.getlist('images')
        context['p_title'] = title
        context['p_content'] = content
        context['p_category_id'] = category_id
        context['p_tags'] = tags
        context['p_images'] = images
        try:

            #raise Exception('테스트 에러 발생')
            if not category_id or not category_id.isdigit():
                raise ValidationError({'category': '카테고리를 선택해주세요.'})

            # 카테고리 객체 가져오기
            category = get_object_or_404(Category, id=category_id)
            # Post 객체 생성
            post = Post(
                title=title,
                content=content,
                created_at=timezone.now(),
                updated_at=timezone.now(),
                category=category,
                author=request.user,
            )
            # 모델 유효성 검사 수행
            post.full_clean()
             # 유효성 검사 통과 시, Post 객체 저장
            post.save()
            # 새로 생성된 Post 객체의 ID 가져오기
            new_post_id = post.id
            # 태그 처리
            if tags:
                tags = tags.split('#')
                for tag_name in tags:
                    tag = Tag.objects.get_or_create(name=tag_name.strip())
                    post.tags.add(tag)
            # 이미지 처리
            if images:
                for image in images:
                    post.images.create(image=image)
            return redirect('blog:post_detail', post_id=new_post_id)
        except ValidationError as e:
            # 유효성 검사 실패 시, 오류 메시지와 함께 폼 다시 렌더링
            #context['errors'] = e.message_dict
            context['vaild_errors'] = e.message_dict
            return render(request, template_name, context )
        except Exception as e:
            context['error'] = str(e)
            return render(request, template_name, context )
    else:
        return render(request, template_name, context )

@login_required(login_url='common:login')
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')
        images = request.FILES.getlist('images')
        post.title = title
        post.content = content
        post.updated_at = timezone.now()
        post.tags.all().delete()
        if tags:
            tags = tags.split(',')
            for tag in tags:
                post.tags.create(name=tag)
        post.images.all().delete()
        if images:
            for image in images:
                post.images.create(image=image)
        post.save()
        return redirect(f'{app_name}:post_detail', post_id=post_id)
    context = {'post': post}
    return render(request, f'{template_name}/write.html', context)

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