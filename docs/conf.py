# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../desdeo_mcdm"))


# -- Project information -----------------------------------------------------

project = "desdeo_mcdm"
copyright = "2020, Giovanni Misitano"
author = "Giovanni Misitano"

# The full version, including alpha/beta/rc tags
release = "1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx_automodapi.automodapi",
    "sphinx.ext.graphviz",
    "sphinx.ext.viewcode",
    "recommonmark",
    "nbsphinx",
    "sphinx.ext.mathjax",
]
numpydoc_show_class_members = False

# autodoc_default_flags = ["members"]
# autosummary_generate = True
# autosectionlabel_prefix_document = True
# autodoc_default_options = {
#     "members": None,
#     "undoc-members": None,
#     "private-members": None,
#     "special-members": None,
#     # "inherited-members",
#     "show-inheritance": None,
#     "exclude-members": ("_abc_cache,_abc_negative_cache," + "_abc_negative_cache_version,_abc_registry"),
# }

source_suffix = [".rst", ".md"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_sourcelink_suffix = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_logo = "_static/desdeo_logo.png"

master_doc = "index"
