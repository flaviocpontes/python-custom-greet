# Custom Greeter

This is a nano-service used as a teaching device fpr API Gateway classes.

## Usage

The preferred way is to use it dockerized, setting the GREET environment variable as the message to be returned at the `/` endpoint.

## Endpoints
- `/` -> Returns the default greeting
- `/<name>` -> Return greeting to the named entity by the `name` parameter
- `/header` -> Return greeting to the named entity by the `name` header
- `/query` -> Return greeting to the named entity by the `name` query parameter
- `/delay/<delay>` -> Returns greeting to the default named entity after `delay` milliseconds

## Environmet

- `GREET` -> Defines the greeting message. _Default: "Hello"_
- `DEFAULT_NAME` -> Defines the default name for the response. _Default: "Stranger"_ 