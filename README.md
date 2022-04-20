# Integrate with Star Wars API
API: https://swapi.dev

Documentation: https://swapi.dev/documentation

Doc. People: https://swapi.dev/documentation#people

## Excercise
Build a python-based API that connects to the Star Wars API, with one endpoint named “skywalker“ and returns the below response:

```json
{
    "status": 200,
    "description": "Luke Skywalker participated in A New Hope, The Empire Strikes Back, Return of the Jedi and Revenge of the Sith. Anakin Skywalker participated in The Phantom Menace, Attack of the Clones and Revenge of the Sith. Shmi Skywalker participated in The Phantom Menace and Attack of the Clones."
}
```

## Description
1. Get all the characters with the name “Skywalker“ using the people endpoint
2. For each character, using the Film endpoint to get the film’s title
3. Prepare a response same as “Expected response“ where for each character, the film where the character appears.
4. Add 1 unit test.

Hints
1. Use Python as the main programming language
2. Create a new virtual env
3. Use any IDE you want
4. Use any Python library that can help you to achieve the goal
5. Call to the API with curl: curl -X GET localhost:8000/skywalker
