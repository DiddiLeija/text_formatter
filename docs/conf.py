# Sphinx config file.
# By now, it is simple and "not-so" fancy, but it will work
# on our case.

# we want some extensions, so we are including them here:
extensions = [
    # first-party
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    # third-party
    "sphinx_copybutton"
]

language = "en"
project = "text_formatter"
author = "Diego Ramirez"
copyright = "2021, Diego Ramirez"

html_sidebars = {"**": ["globaltoc.html", "relations.html", "searchbox.html"]}
