# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os, sys

sys.path.insert(0, os.path.abspath('../src/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'multiwii-proxy-python'

copyright = '2024, BluDay'

author = 'BluDay'

release = '3.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']

source_suffix = '.rst'

root_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

# -- Napoleon options --------------------------------------------------------

napoleon_google_docstring = False

napoleon_numpy_docstring = True

napoleon_include_init_with_doc = False

napoleon_include_private_with_doc = False

napoleon_include_special_with_doc = True

napoleon_use_admonition_for_examples = False

napoleon_use_admonition_for_notes = False

napoleon_use_admonition_for_references = False

napoleon_use_ivar = False

napoleon_use_param = True

napoleon_use_rtype = True

napoleon_preprocess_types = False

napoleon_type_aliases = None

napoleon_attr_annotations = True
