import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text_formatter",
    version="1.0.0",
    author="Diego Ramirez",
    author_email="dr01191115@gmail.com",
    description="Pretty formatter for Python strings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diddileija/text_formatter/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Unix",
        "Topic :: Software Development"
    ],
    keywords="text format pretty strings formatter",
    python_requires='>=3.6, <3.10',
    project_urls={
        "Documentation": "http://github.com/diddileija/text_formatter/blob/main/README.md", # go to README
        "Tracker": "http://github.com/diddileija/text_formatter/issues" # GitHub issues page
    }
)
