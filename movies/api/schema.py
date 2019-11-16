import graphene
from graphene_django.types import DjangoObjectType
from .models import Director, Movie
import graphql_jwt
from graphql_jwt.decorators import login_required


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

    """
    Custom Field Set
    
    query{
      allMovies{
        id
        title
        year
        movieAge
      }
    }
    """
    movie_age = graphene.String()

    def resolve_movie_age(self, info):
        return "Old movie" if self.year < 2000 else "New movie"


class DirectorType(DjangoObjectType):
    """
    query{
      allMovies{
        id
        title
        year
        movieAge
        director {
          name
          surname
        }
      }
    }
    """
    class Meta:
        model = Director


class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    # Add parameter
    movie = graphene.Field(MovieType,
                           id=graphene.Int(),
                           title=graphene.String())

    all_directors = graphene.List(DirectorType)

    @login_required
    def resolve_all_movies(self, info, **kwargs):
        # user = info.context.user
        # if not user.is_authenticated:
        #     raise Exception("Auth credentials were not provided")
        return Movie.objects.all()

    def resolve_all_directors(self, info, **kwargs):
        return Director.objects.all()

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Movie.objects.get(pk=id)

        if title is not None:
            return Movie.objects.get(title=title)

        return None


class MovieCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        year = graphene.Int(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, year):
        movie = Movie.objects.create(title=title, year=year)

        return MovieCreateMutation(movie=movie)


class MovieUpdateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        year = graphene.Int()
        id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, id, title, year):
        movie = Movie.objects.get(pk=id)
        if title is not None:
            movie.title = title
        if year is not None:
            movie.year = year
        movie.save()

        return MovieCreateMutation(movie=movie)


class MovieDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, id):
        movie = Movie.objects.get(pk=id)
        movie.delete()

        # To delete the movie, do pass "None" to movie
        return MovieCreateMutation(movie=None)


class Mutation:
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()

    create_movie = MovieCreateMutation.Field()
    update_movie = MovieUpdateMutation.Field()
    delete_movie = MovieDeleteMutation.Field()
