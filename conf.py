# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme

project = 'Machine learning using quantum'
copyright = '2025, Mohamed Malek Al Fakih & Abdellah Bichlifen'
author = 'Mohamed Malek Al Fakih & Abdellah Bichlifen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


import os
if os.environ.get("READTHEDOCS"):
    html_output = os.path.join(os.environ["READTHEDOCS_OUTPUT"], "html")
import os

# Force correct output directory in Read the Docs environment
if os.environ.get("READTHEDOCS") == "True":
    html_output = os.path.join(os.environ["READTHEDOCS_OUTPUT"], "html")
    if not os.path.exists(html_output):
        os.makedirs(html_output)
    html_static_path = [html_output]
    html_build_dir = html_output  # This ensures Sphinx uses the correct directory
else:
    html_build_dir = "_build/html"

