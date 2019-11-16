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

## Relation

## Schema

```bash
class DirectorType(DjangoObjectType):
    class Meta:
        model = Director
```

## Query
```bash
query{
  movie(id: 4){
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
```

## Data
```bash
{
  "data": {
    "movie": {
      "id": "4",
      "title": "The terminator",
      "year": 1984,
      "movieAge": "Old movie",
      "director": {
        "name": "James",
        "surname": "Cameron"
      }
    }
  }
}
```

# Aliases

Normally, we can not set  the same query name in it.
However, we can do it by using aliases.

```bash
# firstMovie and secondMovie are aliases.

query{
  firstMovie: movie(id: 4){
    id
    title
    year
    movieAge
    director {
      name
      surname
    }
  }
  secondMovie: movie(id: 2) {
    id
    title
    director {
      name
      surname
    }
  }
}
```

# Fragments

## Query 

```bash
{
  firstMovie: movie(id: 4) {
    ...movieData
  }
  secondMovie: movie(id: 2) {
    ...movieData
  }
}

fragment movieData on MovieType {
  id
  title
  director {
    name
    surname
  }
}
```

## Data

```bash
{
  "data": {
    "firstMovie": {
      "id": "4",
      "title": "The terminator",
      "director": {
        "name": "James",
        "surname": "Cameron"
      }
    },
    "secondMovie": {
      "id": "2",
      "title": "Avatar",
      "director": {
        "name": "James",
        "surname": "Cameron"
      }
    }
  }
}
```

# And Query

```
query MoviesAndDirector{
  allMovies {
    title 
  	year
    director {
      surname
    }
  }
}

query MoviesAndDirector{
  movie(id: 1) {
    title 
  	year
    director {
      surname
    }
  }
}
```

# query param $

See the image of the img dir.

```
query MoviesAndDirector($id: Int){
  movie(id: $id) {
    title 
  	year
    director {
      surname
    }
  }
}
```


```bash
{
  "id": 1
}
```

# Query confidence

```bash
query MoviesAndDirector($id: Int, $showdirector: Boolean = true){
  movie(id: $id) {
    id
    title 
  	year
    director @include(if: $showdirector){
      surname
    }
  }
}
```

```bash
{
  "id": 4,
  "showdirector": false
}
```

# Mutation

## Create Mutation

```
mutation CreateMovie {
  createMovie(title: "Test", year: 2002) {
    movie {
      id
      title
      year
    }
  }
}

query AllMovies {
  allMovies {
    id
    title
    year
  }
}

```

## Update Mutation

```bash
mutation UpdateMovie {
  updateMovie(id: 5, title: "Test 2", year: 1900) {
    movie {
      id
      title
      year
    }
  }
}
```

## Delete Mutation

```bash
mutation DeleteMovie {
  deleteMovie(id: 5) {
    movie {
      id
    }
  }
}
```

# Get Authentication

## Query

```bash
mutation {
  tokenAuth(username:"admin", password:"XXXX") {
    token
  }
}
```

## Data
```bash
{
  "data": {
    "tokenAuth": {
      "token": "eyJ0eXAiOiJKV1QiLCbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTczODkwOTQ1LCJvcmlnSWF0IjoxNTczODkwNjQ1fQ.FZvgdL0mO0ctcE30NhnGPRoc8ZEtRdeFyGcm_kS3MOc"
    }
  }
}
```

# VerifyToken

# Query
```bash
mutation VerifyToken {
  verifyToken(token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTczODkyMzg5LCJvcmlnSWF0IjoxNTczODkyMDg5fQ.ZMMmuB_dJFGBeY5fLec7FaGkMTaTsrOmRD0sGckBi1c") {
    payload
  }
}
```

# Data
```bash
{
  "data": {
    "verifyToken": {
      "payload": {
        "username": "admin",
        "exp": 1573892389,
        "origIat": 1573892089
      }
    }
  }
}
```

## Relay

## Query
```bash
query AllMovies {
  allMovies {
		edges {
      node{
        id
        title
        director {
          name
          surname
        }
      }
    }
  }
}
```

## Data

```bash
{
  "data": {
    "allMovies": {
      "edges": [
        {
          "node": {
            "id": "TW92aWVOb2RlOjE=",
            "title": "Titanic",
            "director": {
              "name": "James",
              "surname": "Cameron"
            }
          }
        },
        {
          "node": {
            "id": "TW92aWVOb2RlOjI=",
            "title": "Avatar",
            "director": {
              "name": "James",
              "surname": "Cameron"
            }
          }
        },
        {
          "node": {
            "id": "TW92aWVOb2RlOjM=",
            "title": "Million Dollar Baby",
            "director": {
              "name": "James",
              "surname": "Cameron"
            }
          }
        },
        {
          "node": {
            "id": "TW92aWVOb2RlOjQ=",
            "title": "The terminator",
            "director": {
              "name": "James",
              "surname": "Cameron"
            }
          }
        }
      ]
    }
  }
}
```