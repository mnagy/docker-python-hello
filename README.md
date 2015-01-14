Dockerfile example with python twisted
=======================================

This repository contains a simple twisted application with a Dockerfile.

Using
---------------
```
$ docker build -t mnagy/twisted_hello .
$ docker run -p 1337:1337 -t mnagy/twisted_hello
```

The application will run on port 1337.
