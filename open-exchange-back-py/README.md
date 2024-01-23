# Open Exchange Backend - Python

This service purpose is to upload and store rates of the day automatically.
- More over it has to transmit stored rates from the database to any want to get them.
## Requirement

You should build up your own virtual environment to handle this project.

_N.B: Make sure to be into your virtual environment before launching any dependencies CLI_

## Dependency Management

We use [pip-tools](https://github.com/jazzband/pip-tools) to be able to avoid misunderstood of the requirements.txt.

You should compile the requirements.in 
```shell
$ pip-compile ./requirements.in
```

Then install all dependencies by running:
```shell
$ pip install -r requirements.txt
```

## Launch it !

```shell
$ flask run
```

