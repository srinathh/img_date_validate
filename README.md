img_date_validate
===============================
A Python data science project


Package Structure
-----------------
- **Libraries** provided by the package should be developed inside `src/img_date_validate`
  - A `hello_world()` function is provided inside `src/img_date_validate/__init__.py` as an example
  - The Library packages can be installed for local develoment with `pip install -e .[dev]`
  - The development bui

- **Executables** provided by the package should be developed inside `src/bin`
  - A default executable is provided under `src/bin/main.py` with the entrypoint `main()`
  - To run this executable from console, run `img_date_validate`. It calls the `helllo_world()` function
  - The executable name and entrypoint are configured in `pyproject.toml` under `[project.scripts]`

- **Tests** shoudl be written under `tests` folder
  - Tests are deliberately kept outside the source tree to ensure tests run only after package installation
  - The provided `test_sample.py` tests that the supplied `hello_world()` behaves as expected

- **Data** if needed should be placed in the `data` folder. All contents are ignored

- **Notebooks** should be developed inside `notebooks`. They will work only if package is installed.

```
img_date_validate
├── data
│   └── .gitkeep
├── notebooks
│   └── .gitkeep
├── src
│   ├── bin
│   │   ├── __init__.py
│   │   └── main.py
│   └── img_date_validate
│       └── __init__.py
└── tests
│   └── test_sample.py
├── .gitignore
├── Dockerfile
├── pyproject.toml
└── README.md
```


Development
-----------
Clone the repository to the development machine, create a virtual environment and install
the packages locally for development. Installing with the `.[dev]` option also installs
`ipykernel` and `pytest` to allow for experimentation with notebooks and unit testing.

```
conda create --name img_date_validate python=3.11
conda activate img_date_validate
pip install -e .[dev]
```

Testing
-------
`Pytest` can be used to run the tests in the `tests` folder
````
pytest
```

Executable
----------
`pyproject.toml` by default installs `img_date_validate` as an executable
command from the shell or command line.
```
img_date_validate
```

Docker
------
To containarize your application, simply use standard `docker build` and `docker run` commands.
It assumes the executable named `img_date_validate` is the default entry point.

```
docker build -t img_date_validate:latest .
docker run img_date_validate:latest
```

Authors
-------
`Hariharan Srinath <srinathh@gmail.com>`_.
