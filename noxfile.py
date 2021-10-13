# Our Nox configuration file, used
# for running tests.

import nox


@nox.session()
def test(session):
    # install flake8 and isort
    session.install("flake8", "isort", "black")
    # stop the build if there are Python syntax errors
    # or undefined names. Consider that the GitHub editor
    # is 127-characters wide.
    session.run(
      "flake8",
      ".",
      "--count",
      "--show-source",
      "--statistic"
    )
    session.run("isort", ".", "--check-only", "-v")
    session.run("black", "--check", ".")
