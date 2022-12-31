.. title: Main page title

Grids
=======

Introduction
-------------

.. grid:: 1 2 3 4
    :outline:

    .. grid-item::

        A

    .. grid-item::

        B

    .. grid-item::

        C

    .. grid-item::

        D


Placing a card in a grid
-------------------------

.. grid:: 2

    .. grid-item-card::  Title 1

        A

    .. grid-item-card::  Title 2

        B


Controlling spacing between items
------------------------------------

.. grid:: 2
    :gutter: 1

    .. grid-item-card:: Title A

        A

    .. grid-item-card::

        B

.. grid:: 2
    :gutter: 3 3 4 5

    .. grid-item-card::

        A

    .. grid-item-card::

        B


Item level column width
-------------------------

.. grid:: 2

    .. grid-item-card::
        :columns: auto

        A

    .. grid-item-card::
        :columns: 12 6 6 6

        B

    .. grid-item-card::
        :columns: 12

        C


Nesting grids
---------------

.. grid:: 1 1 2 2
    :gutter: 1

    .. grid-item::

        .. grid:: 1 1 1 1
            :gutter: 1

            .. grid-item-card:: Item 1.1

                Multi-line

                content

            .. grid-item-card:: Item 1.2

                Content

    .. grid-item::

        .. grid:: 1 1 1 1
            :gutter: 1

            .. grid-item-card:: Item 2.1

                Content

            .. grid-item-card:: Item 2.2

                Content

            .. grid-item-card:: Item 2.3

                Content


Cards
======

.. card:: Card Title

    Card content


.. card:: Card Title

    Header
    ^^^
    Card content
    +++
    Footer


Card images
------------

.. grid:: 2 3 3 4

    .. grid-item::

        .. card:: Title
            :img-background: images/particle_background.jpg
            :class-card: sd-text-black

            Text

    .. grid-item-card:: Title
        :img-top: images/particle_background.jpg

        Header
        ^^^
        Content
        +++
        Footer

    .. grid-item-card:: Title
        :img-bottom: images/particle_background.jpg

        Header
        ^^^
        Content
        +++
        Footer


Clickable cards
----------------

.. _cards-clickable:


.. card:: Clickable Card (external)
    :link: https://example.com

    The entire card can be clicked to navigate to https://example.com.

.. card:: Clickable Card (internal)
    :link: cards-clickable
    :link-type: ref

    The entire card can be clicked to navigate to the ``cards`` reference target.


Card carousels
------------------

.. card-carousel:: 2

    .. card:: card 1

        content

    .. card:: card 2

        Longer

        content

    .. card:: card 3

    .. card:: card 4

    .. card:: card 5

    .. card:: card 6


Dropdowns
==========

.. dropdown::

    Dropdown content

.. dropdown:: Dropdown title

    Dropdown content

.. dropdown:: Open dropdown
    :open:

    Dropdown content

Tabs
======

.. tab-set::

    .. tab-item:: Label1

        Content 1

    .. tab-item:: Label2

        Content 2


Synchronised Tabs
-----------------

.. tab-set::

    .. tab-item:: Label1
        :sync: key1

        Content 1

    .. tab-item:: Label2
        :sync: key2

        Content 2

.. tab-set::

    .. tab-item:: Label1
        :sync: key1

        Content 1

    .. tab-item:: Label2
        :sync: key2

        Content 2

Tabbed code examples
----------------------

..

  .. tab-set-code::

    .. code-block:: python

        a = 1;

    .. code-block:: javascript

        a = 1;


Badges, Buttons & Icons :octicon:`rocket`
==========================================


Badges
-------

:bdg:`plain badge`

:bdg-primary:`primary`, :bdg-primary-line:`primary-line`

:bdg-secondary:`secondary`, :bdg-secondary-line:`secondary-line`

:bdg-success:`success`, :bdg-success-line:`success-line`

:bdg-info:`info`, :bdg-info-line:`info-line`

:bdg-warning:`warning`, :bdg-warning-line:`warning-line`

:bdg-danger:`danger`, :bdg-danger-line:`danger-line`

:bdg-light:`light`, :bdg-light-line:`light-line`

:bdg-dark:`dark`, :bdg-dark-line:`dark-line`


------


:bdg-link-primary:`https://example.com`

:bdg-link-primary-line:`explicit title <https://example.com>`

Buttons
-------

.. button-link:: https://example.com

.. button-link:: https://example.com

    Button text

.. button-link:: https://example.com
    :color: primary
    :shadow:

.. button-link:: https://example.com
    :color: primary
    :outline:

.. button-link:: https://example.com
    :color: secondary
    :expand:


Inline Icons
------------

Octicon Icons
~~~~~~~~~~~~~~

A coloured icon: :octicon:`report;1em;sd-text-info`, some more text.

Material Design Icons
~~~~~~~~~~~~~~~~~~~~~~~

- A regular icon: :material-regular:`data_exploration;2em`, some more text
- A coloured regular icon: :material-regular:`settings;3em;sd-text-success`, some more text.
- A coloured outline icon: :material-outlined:`settings;3em;sd-text-success`, some more text.
- A coloured sharp icon: :material-sharp:`settings;3em;sd-text-success`, some more text.
- A coloured round icon: :material-round:`settings;3em;sd-text-success`, some more text.
- A coloured two-tone icon: :material-twotone:`settings;3em;sd-text-success`, some more text.
- A fixed size icon: :material-regular:`data_exploration;24px`, some more text.

FontAwesome Icons
~~~~~~~~~~~~~~~~~~

- An icon :fas:`spinner;sd-text-primary`, some more text.
- An icon :fab:`github`, some more text.
- An icon :fab:`gitkraken;sd-text-success fa-xl`, some more text.
- An icon :fas:`skull;sd-text-danger`, some more text.

Additional
==========

article-info
-------------

.. article-info::
    :avatar: images/ebp-logo.png
    :avatar-link: https://executablebooks.org/
    :avatar-outline: muted
    :author: Executable Books
    :date: Jul 24, 2021
    :read-time: 5 min read
    :class-container: sd-p-2 sd-outline-muted sd-rounded-1
