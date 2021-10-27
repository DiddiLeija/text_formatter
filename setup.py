import setuptools

# look for the README.md file for the long description
# on the metadata
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# package setup
setuptools.setup(
    name="text_formatter",
    version="1.0.0dev6",
    author="Diego Ramirez",
    author_email="dr01191115@gmail.com",
    description="Pretty formatter for Python strings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diddileija/text_formatter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Unix",
        "Topic :: Software Development",
        "Topic :: Text Processing",
    ],
    keywords="text format pretty strings formatter",
    python_requires=">=3.6",
    project_urls={
        "Documentation": "http://text-formatter.readthedocs.io",  # ReadTheDocs site
        "Tracker": "http://github.com/diddileija/text_formatter/issues",  # GitHub issues page
        "Source": "http://github.com/diddileija/text_formatter",  # source code on GitHub
    },
    zip_safe=False,
)
