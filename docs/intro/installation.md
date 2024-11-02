# Project Installation

The first part of using this package is to ensure it is installed properly. Requiem can be installed as a Python Package, and requires Python version 3.13 or newer, and `pip` version 24.3.1 or newer.

## Dependencies

Requiem comes with several depedencies, which are as follows:

- [Requests](https://github.com/psf/requests), for local development and hosting.
- [Werkzeug](https://github.com/pallets/werkzeug), for web utilities.
- [Jinja2](https://github.com/pallets/jinja), for web templating.
- [Python Chess](https://github.com/niklasf/python-chess), for more chess utilities.

## Virtual Enviroments

Using avirtual enviroment for all your project dependencies is **highly recommended**, both for development and production.

This is because the more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even Python itself. Virtual Enviroments seperate packages, and ensure they do not affect or "break" each other.

Python comes bundled with the venv module to create virtual environments, so we will be using that to install our packages.

### Creating an enviroment:

::::{tab-set}
:::{tab-item} Windows
``` console
python -m venv venv
.venv\Scripts\activate
```
:::
:::{tab-item} MacOS
``` console
python -m venv venv
source venv/bin/activate
```
:::
::::

## Installing Requiem

Now that you have set up a Virtual Enviroment, you can finally install Requiem:

``` console
pip install requiem
```