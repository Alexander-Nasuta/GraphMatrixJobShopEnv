# Graph Matrix Job Shop Env

A Gymnasium Environment for Job Shop Scheduling using the Graph Matrix Representation by [Błażewicz et al.](https://www.sciencedirect.com/science/article/abs/pii/S0377221799004865).

- Github: [GraphMatrixJobShopEnv](https://github.com/Alexander-Nasuta/)
- Pypi: [GraphMatrixJobShopEnv](https://pypi.org/project/manta-manim-theme/)
- Documentation: [GraphMatrixJobShopEnv Docs](https://alexander-nasuta.github.io/)

## Description



## Quickstart

```shell
pip install <<todo>>
```


## State of the Project

This project is complementary material for a research paper. It will not be frequently updated.
Minor updates might occur.
Significant further development will most likely result in a new project. In that case, a note with a link will be added in the `README.md` of this project.  

## Dependencies

This project specifies multiple requirements files. 
`requirements.txt` contains the dependencies for the environment to work. These requirements will be installed automatically when installing the environment via `pip`.
`requirements_dev.txt` contains the dependencies for development purposes. It includes the dependencies for testing, linting, and building the project on top of the dependencies in `requirements.txt`.
`requirements_examples.txt` contains the dependencies for running the examples inside the project. It includes the dependencies in `requirements.txt` and additional dependencies for the examples.

In this Project the dependencies are specified in the `pyproject.toml` file with as little version constraints as possible.
The tool `pip-compile` translates the `pyproject.toml` file into a `requirements.txt` file with pinned versions. 
That way version conflicts can be avoided (as much as possible) and the project can be built in a reproducible way.

## Development Setup

If you want to check out the code and implement new features or fix bugs, you can set up the project as follows:

### Clone the Repository

clone the repository in your favorite code editor (for example PyCharm, VSCode, Neovim, etc.)

```shell
git clone <<todo>>
```

if you are using PyCharm, I recommend doing the following additional steps:

- mark the `src` folder as source root (by right-clicking on the folder and selecting `Mark Directory as` -> `Sources Root`)
- mark the `tests` folder as test root (by right-clicking on the folder and selecting `Mark Directory as` -> `Test Sources Root`)
- mark the `resources` folder as resources root (by right-clicking on the folder and selecting `Mark Directory as` -> `Resources Root`)

at the end your project structure should look like this:

todo

### Create a Virtual Environment (optional)

Most Developers use a virtual environment to manage the dependencies of their projects. 
I personally use `conda` for this purpose.

When using `conda`, you can create a new environment with the name 'my-graph-jsp-env' following command:

```shell
conda create -n my-graph-jsp-env python=3.11
```

Feel free to use any other name for the environment or an more recent version of python.
Activate the environment with the following command:

```shell
conda activate my-graph-jsp-env
```

Replace `my-graph-jsp-env` with the name of your environment, if you used a different name.

You can also use `venv` or `virtualenv` to create a virtual environment. In that case please refer to the respective documentation.

### Install the Dependencies

To install the dependencies for development purposes, run the following command:

```shell
pip install -r requirements_dev.txt
pip install tox
```

The testing package `tox` is not included in the `requirements_dev.txt` file, because it sometimes causes issues when 
using github actions. 
Github Actions uses an own tox environment (namely 'tox-gh-actions'), which can cause conflicts with the tox environment on your local machine.

Reference: [Automated Testing in Python with pytest, tox, and GitHub Actions](https://www.youtube.com/watch?v=DhUpxWjOhME).

### Install the Project in Editable Mode

To install the project in editable mode, run the following command:

```shell
pip install -e .
```

This will install the project in editable mode, so you can make changes to the code and test them immediately.

### Run the Tests

This project uses `pytest` for testing. To run the tests, run the following command:

```shell
pytest
```

For testing with `tox` run the following command:

```shell
tox
```

Tox will run the tests in a separate environment and will also check if the requirements are installed correctly.

### Builing and Publishing the Project to PyPi 

In order to publish the project to PyPi, the project needs to be built and then uploaded to PyPi.

To build the project, run the following command:

```shell
python -m build
```

It is considered good practice use the tool `twine` for checking the build and uploading the project to PyPi.
By default the build command creates a `dist` folder with the built project files.
To check all the files in the `dist` folder, run the following command:

```shell
twine check dist/**
```

If the check is successful, you can upload the project to PyPi with the following command:

```shell
twine upload dist/**
```

### Documentation
This project uses `sphinx` for generating the documentation. 
It also uses a lot of sphinx extensions to make the documentation more readable and interactive.
For example the extension `myst-parser` is used to enable markdown support in the documentation (instead of the usual .rst-files).
It also uses the `sphinx-autobuild` extension to automatically rebuild the documentation when changes are made.
By running the following command, the documentation will be automatically built and served, when changes are made (make sure to run this command in the root directory of the project):

```shell
sphinx-autobuild ./docs/source/ ./docs/build/html/
```

This project features most of the extensions featured in this Tutorial: [Document Your Scientific Project With Markdown, Sphinx, and Read the Docs | PyData Global 2021](https://www.youtube.com/watch?v=qRSb299awB0).



## Contact

If you have any questions or feedback, feel free to contact me via [email](mailto:alexander.nasuta@wzl-iqs.rwth-aachen.de) or open an issue on repository.
