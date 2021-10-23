#!/usr/bin/env python3

# Standard libraries.
import setuptools  # type: ignore


setuptools.setup(
    name="pelican-markdown-unrendered-metadata",
    version="0.1.0",
    description="Read Pelican metadata from link references",
    author="Boni Lindsley",
    author_email="boni.lindsley@gmail.com",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    + ["pelican.plugins.markdown_unrendered_metadata"],
    license="MIT",
    install_requires=[
        "Markdown >= 3.3.4",
        "pelican >= 4.7.1",
    ],
    extras_require={
        "dev": [
            "Markdown >= 3.3.4",
            "Sphinx >= 4.2.0",
            "black >= 21.9b0",
            "coverage[toml] >= 6.0.2",
            "mypy >= 0.910",
            "pytest >= 6.2.5",
            "recommonmark >= 0.7.1",
            "tox >= 3.24.4",
            "types-Markdown >= 3.3.6",
            "types-appdirs >= 1.4.1",
            "types-pkg_resources >= 0.1.3",
            "types-six >= 1.16.2",
        ],
    },
    python_requires=">= 3.9",
)
