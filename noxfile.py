# Our Nox configuration file, used
# for running tests.

import nox


@nox.session
def test(session):
    # install flake8 and isort
    session.install("flake8", "isort", "black")
    # stop the build if there are Python syntax errors
    # or undefined names. Consider that the GitHub editor
    # is 127-characters wide.
    session.run("flake8", ".", "--count", "--show-source", "--statistic")
    session.run("isort", ".", "--check-only", "-v")
    session.run("black", "--check", ".")


@nox.session
def format(session):
    # Run black to reformat the whole code.
    session.install("black")
    session.run("black", ".")


@nox.session
def docs(session):
    # build the Sphinx documentation, to see
    # if no warnings are raised
    session.install("-e", ".")
    session.install("-r", "docs/requirements.txt")

    command = [
        "sphinx-build",
        "-W",
        "-c",
        "docs/conf.py",
        "-d",
        "docs/build/doctrees",
        "-b",
        "html",
        "docs/",
    ]

    session.run(*command)
