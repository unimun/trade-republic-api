========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/trade-republic-api/badge/?style=flat
    :target: https://trade-republic-api.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/unimun/trade-republic-api/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/unimun/trade-republic-api/actions

.. |codecov| image:: https://codecov.io/gh/unimun/trade-republic-api/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/unimun/trade-republic-api

.. |version| image:: https://img.shields.io/pypi/v/trade-republic-api.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/trade-republic-api

.. |wheel| image:: https://img.shields.io/pypi/wheel/trade-republic-api.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/trade-republic-api

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/trade-republic-api.svg
    :alt: Supported versions
    :target: https://pypi.org/project/trade-republic-api

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/trade-republic-api.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/trade-republic-api

.. |commits-since| image:: https://img.shields.io/github/commits-since/unimun/trade-republic-api/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/unimun/trade-republic-api/compare/v0.0.1...main



.. end-badges

Trade Republic API (Unofficial)

* Free software: BSD 2-Clause License

Installation
============

::

    pip install trade-republic-api

You can also install the in-development version with::

    pip install https://github.com/unimun/trade-republic-api/archive/main.zip


Documentation
=============


https://trade-republic-api.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
