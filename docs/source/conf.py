# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath("./DQMaRC"))
sys.path.insert(0, os.path.abspath("../../DQMaRC"))

# -- Project information -----------------------------------------------------
# -- Project information -----------------------------------------------------
version_info = {}
with open(os.path.join("../../DQMaRC", "__version__.py")) as f:
    exec(f.read(), version_info)
__version__ = version_info["__version__"]

project = 'DQMaRC'
copyright = '2024, Anthony Lighterness and Michael Adcock'
author = 'Anthony Lighterness and Michael Adcock'

# Assign version and release as strings
release = str(__version__)
version = str(__version__)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',  # Core Sphinx library for auto html doc generation from docstrings
    "sphinx.ext.autosectionlabel",
    'sphinx.ext.autosummary',  # Create neat summary tables for modules/classes/methods etc
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    'sphinx.ext.intersphinx',  # Link to other project's documentation (see mapping below)
    'sphinx.ext.viewcode',  # Add a link to the Python source code for classes, functions etc.
    'sphinx_autodoc_typehints', # Automatically document param types (less noise in class signature)
    'nbsphinx',  # Integrate Jupyter Notebooks and Sphinx
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinx.ext.napoleon',
    "sphinx_click",
    "sphinx_copybutton",
    'jupyter_sphinx',
    'sphinx_tabs.tabs'
]

autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
html_show_sourcelink = False  # Remove 'view source code' from top of page (for html, not python)
autodoc_inherit_docstrings = True  # If no docstring, inherit from base class
set_type_checking_flag = True  # Enable 'expensive' imports for sphinx_autodoc_typehints
nbsphinx_allow_errors = True  # Continue through Jupyter errors
#autodoc_typehints = "description" # Sphinx-native method. Not as good as sphinx_autodoc_typehints
add_module_names = False # Remove namespaces from class/method signatures

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_preserve_defaults = True


# -- HTML output ------------------------------------------------------------

# Readthedocs theme
# on_rtd is whether on readthedocs.org, this line of code grabbed from docs.readthedocs.org...
# on_rtd = os.environ.get("READTHEDOCS", None) == "True"
# if not on_rtd:  # only import and set the theme if we're building docs locally
#     import sphinx_rtd_theme
#     html_theme = "sphinx_rtd_theme"
#     html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# html_css_files = ["readthedocs-custom.css"] # Override some CSS settings
html_theme = 'sphinx_book_theme'

html_theme_options = {
    # "logo_only": True,
    "repository_url": "https://github.com/christie-nhs-data-science/DQMaRC",
    # "use_repository_button": True,
    # "use_issues_button": True,
    # "use_edit_page_button": True,
    "path_to_docs": "docs",
}

# html_theme = 'sphinx_rtd_theme'

# Pydata theme
#html_theme = "pydata_sphinx_theme"
#html_logo = "_static/logo-company.png"
#html_theme_options = { "show_prev_next": False}
#html_css_files = ['pydata-custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_js_files = ['js/custom.js']

html_css_files = ['css/custom.css']
