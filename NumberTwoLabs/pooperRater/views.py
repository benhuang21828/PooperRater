from django.template import RequestContext
from pooperRater.models import User
from django.shortcuts import render, render_to_response

# Create your views here.
from rest_framework.generics import RetrieveAPIView, ListAPIView
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from pooperRater.serializers import UserSerializer
from pooperRater.models import User


def home(request):
   context = RequestContext(request,
                           {'user': request.user})
   return render_to_response('home.html', context_instance=context)


########################## user profiles ##########################
# @login_required
# def profile(request):
#     user_social_auth = request.user.social_auth.filter(provider='facebook').first()
#     graph = facebook.GraphAPI(user_social_auth.extra_data['access_token'])
#     profile_data = graph.get_object("me")
#     return render(request, 'profile.html', profile_data)
######################### user rest api view #######################

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer