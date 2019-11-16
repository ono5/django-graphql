from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', jwt_cookie(GraphQLView.as_view(graphiql=True))),
]

'''
# jwt_cookie

# 1. Do GetToken
mutation GetToken{
  tokenAuth(username:"admin", password:"Hiroki1029") {
    token
  }
}

# 2. Do Get AllMovies
query AllMovies {
  allMovies {
    title
  }
}
'''