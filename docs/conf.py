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
    "sphinx_copybutton",
]

language = "en"
project = "text_formatter"
author = "Diego Ramirez"
copyright = "2021, Diego Ramirez"

# HTML specs
html_theme = "furo"
html_theme_options = {
    "announcement": "Do you like this? Tell us <a href='https://shoutouts.dev/projects/DiddiLeija/text_formatter'>here</a>!",
}
