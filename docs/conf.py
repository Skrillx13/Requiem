# -- Library Import --
from datetime import datetime

# -- Project Information --
project = 'Requiem'
copyright = f"{datetime.now().year}, A Skrillx Project"
author = 'Skrillx'
release = '1.0'

# -- General Configuration --
extensions = [
    'myst_parser',
    'sphinx_design',
]
myst_enable_extensions = ["colon_fence"]
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = ['_build']
html_show_sphinx = False

# -- Theming --
html_theme = 'alabaster'

html_sidebars = {
    "**": [
        "sidebars.html",
        "customs.html",
    ],
}