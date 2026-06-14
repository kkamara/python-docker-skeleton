# Python Docker Skeleton

(2020) Get started with Python and Docker.

* [Installation](#installation)

* [Usage](#usage)

* [Not Using Docker?](#not-using-docker)

* [Misc.](#misc)

* [Contributing](#contributing)

* [License](#license)

## Installation

Make sure you have [Docker Compose](https://docs.docker.com/compose/install/) installed if you are using Docker.

```bash
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

## Usage

```bash
# to run on first time
docker-compose up --build
# to run in background
docker-compose up --build -d
# to run when file-changes have been made
docker-compose up
```

<a name="not-using-docker"></a>
#### Not Using Docker?

```bash
python src/main.py -f=foo --bar=baz
```

## Misc.

[Python Docker Skeleton](https://github.com/kkamara/python-docker-skeleton).

[PHP Docker Skeleton](https://github.com/kkamara/php-docker-skeleton).

[NodeJS Docker Skeleton](https://github.com/kkamara/nodejs-docker-skeleton).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
