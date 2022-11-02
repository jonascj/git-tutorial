# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Versionsstyring\nmed Git og GitHub'
copyright = '2022, Jonas Camillus Jeppesen'
author = 'Jonas Camillus Jeppesen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', 'venv2']

extensions = ['sphinx_tabs.tabs',
              'sphinxcontrib.bibtex']

bibtex_bibfiles = ['refs.bib']

#extensions = ['sphinxcontrib.images']
#images_config = {'override_image_directive': True}


language = 'da'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_title = project

html_static_path = ['_static']
html_css_files = ['custom.css']
html_theme_options = {
    'home_page_in_toc': False,
    'show_navbar_depth': 1,
    'show_toc_level': 2,
    'toc_title': "MY_TOC_TITLE"
}

numfig = True
numfig_format = {'figure': 'Fig. %s'}

rst_prolog = """
.. role:: figroilbl
    :class: fig-roi-lbl
"""

rst_epilog = """
**********
Litteratur
**********

.. footbibliography::

"""

