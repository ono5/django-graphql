import React from 'react';
import gql from 'graphql-tag';
import { useQuery } from '@apollo/react-hooks';

const GET_MOVIES = gql`
{
    allMovies {
        edges {
          node {
            id
            title
          }
        }
      }
}`;

function Movies() {

    const { loading, error, data } = useQuery(GET_MOVIES);

    if (loading) return 'Loading...';
    if (error) return `Error. ${error.message}`;

    const movies = data.allMovies.edges;

    /*
            {
          "data": {
            "allMovies": {
              "pageInfo": {
                "startCursor": "YXJyYXljb25uZWN0aW9uOjA=",
                "hasNextPage": true,
                "hasPreviousPage": false
              },
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
                }
              ]
            }
          }
        }
    */

    return (
        <div>
            <h1>List of movies - React</h1>
            {
                movies.map(movie => {
                    return <h2 key={movie.node.id}>{movie.node.title}</h2>
                })
            }
        </div>
    )
}

export default Movies;