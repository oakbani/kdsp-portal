# Remotebase Hackfest Submission for KDSP - Challenge

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to create virtual environment and install requirements.

```bash
python -m venv venv
python ./venv/Script/activate
pip install requirements.txt
```

## Usage

```run applications
python -m gunicorn -w 1 wsgi.py:app

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

