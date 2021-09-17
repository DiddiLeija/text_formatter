# Our Nox configuration file, used
# for running tests.

import nox


@nox.session(python=["3.6", "3.7", "3.8", "3.9", "3.10"])
def flake8_lint(session):
    # install flake8
    session.install("flake8")
    # stop the build if there are Python syntax errors
    # or undefined names. Consider that the GitHub editor
    # is 127-characters wide.
    session.run(
      "flake8",
      ".",
      "--count",
      "--select=E9,F63,F7,F82",
      "--max-complexity=10",
      "--max-line-length=127",
      "--show-source",
      "--statistic"
    )


@nox.session(python=["3.6", "3.7", "3.8", "3.9", "3.10"])
def isort_lint(session):
    # install isort
    session.install("isort")
    # try to cover every single file on the repository.
    # (Maybe we should modify this run in the future)
    session.run("isort", "**/*.py", "--check-only", "-v")
    session.run("isort", "*.py", "--check-only", "-v")
