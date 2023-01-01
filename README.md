Nikola with sphinx-design
==========================

* Sample Nikola site using [sphinx-design](https://github.com/executablebooks/sphinx-design) directives for bootstrap-like cards without writing raw HTML.
* Not everything is working (panels do, icons do, drop-downs don't).
* Checkout recusrively, `sphinx-design` is included as submodule.
* Needs a recent sass compiler (otherwise you get errors about `math.div`).
* Run `nikola build` or `nikola auto` as usual.
* [plugins/sphinxdesign/sphinxdesign.py](plugins/sphinxdesign/sphinxdesign.py) contains Sphinx stubs so that sphinx-design can be loaded and used unmodified as if inside sphinx.
* The [sample page](pages/index.rst) is composed from examples showing [various components of sphinx-design](https://sphinx-design.readthedocs.io/en/furo-theme/grids.html).

![screenshot](images/nikola-sphinx-design.png)
