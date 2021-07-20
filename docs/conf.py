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
    #"myst_parser", # ignore this one (by now)
    "sphinx_copybutton"
]

project = "text_formatter"
copyright = "Diego Ramirez"

# by now, set ".rst" as the source suffix
source_suffix = ".rst"

# myst_parser options
#myst_enable_extensions = ["deflist"]
