# Our Nox configuration file, used
# for running tests.

import nox


@nox.session()
def test(session):
    # install flake8 and isort
    session.install("flake8", "isort")
    # stop the build if there are Python syntax errors
    # or undefined names. Consider that the GitHub editor
    # is 127-characters wide.
    session.run(
      "flake8",
      ".",
      "--exclude=test/lib",
      "--count",
      "--max-complexity=10",
      "--max-line-length=127",
      "--show-source",
      "--statistic"
    )
    session.run("isort", "**/*.py", "--check-only", "-v")
    session.run("isort", "*.py", "--check-only", "-v")
