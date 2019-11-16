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

