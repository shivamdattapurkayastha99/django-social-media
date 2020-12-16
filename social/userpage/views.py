from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.views.generic import ListView
# Create your views here.
def userhome(request):
    posts=Post.objects.all()
    data={'posts':posts}
    return render(request,'postfeed.html',data)
def post(request):
    if request.method=='POST':
        image=request.FILES.get("image")
        captions=request.POST.get('captions')
        
        user=request.user
        post_obj=Post(user=user,captions=captions,image=image)
        post_obj.save()
        return redirect('/userpage')
    else:
        return redirect('/userpage')
def delPost(request,post_id):
    post_=Post.objects.filter(pk=post_id)
    image_path=post_[0].image.url 
    post_.delete()
    return redirect('/userpage')      
def userProfile(request,username):
    user=User.objects.filter(username=username)
    if user:
        profile=Profile.objects.get(user=user[0])
        post=getPost(user[0])
        bio=profile.bio
        userImage=profile.userImage
        connection=profile.connections
        following=profile.following
        follower=profile.followers
        data={'userobj':user,'bio':bio,'con':connection,'follower':follower,'following':following,'posts':post,'userImage':userImage}
    return render(request,'userProfile.html',data)
    # return HttpResponse("User doesnot exist")
def getPost(user):
    post_obj=Post.objects.filter(user=user)
    imgList=[
        post_obj[i:i+3] for i in range(0,len(post_obj),3)
    ]
    return imgList

def likepost(request):
    post_id = request.GET.get("likeId", "")
    post = Post.objects.get(pk=post_id)
    user = request.user
    like = Like.objects.filter(post = post, user=user)
    liked = False

    if like:
        Like.dislike(post, user)
    else:
        liked = True
        Like.like(post, user)

    resp = {
        'liked':liked
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type = "application/json")
def comment(request):
    comment_=request.GET.get('comment')
    return render(request,'comment.html')
# def follow(request,username):
#     pass
class Search_User(ListView):
    model = User
    template_name = "search.html"
    paginate_by = 5 
    def get_queryset(self):
        username = self.request.GET.get("username", None)
        queryset = User.objects.filter(username__icontains = username).order_by('-id')
        return queryset
    