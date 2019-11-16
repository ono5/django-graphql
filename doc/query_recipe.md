# All Movie

## schema
```bash
class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()
```

## Query
```bash
query {
  allMovies {
    title
  }
}
```

## data
```bash
{
  "data": {
    "allMovies": [
      {
        "title": "Titanic"
      }
    ]
  }
}
```

# Params

## schema
```bash
class Query(graphene.ObjectType):
    # Add parameter
    movie = graphene.Field(MovieType, id=graphene.Int())


    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Movie.objects.get(pk=id)

        return None
```

## Query

```bash
query {
  movie(id: 1) {
    title
    year
  }
}
```

## data

```bash
{
  "data": {
    "movie": {
      "title": "Titanic",
      "year": 1997
    }
  }
}
```