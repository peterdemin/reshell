=================================
reshell - Reverse shell in Python
=================================

Install
=========

.. code:: bash

    pip install reshell

Usage
=====

On the host launch receiver with

.. code:: bash

    $ nc -lvp 12345

On destination host launch shell:

.. code:: bash

    $ export RESHELL_TARGET=127.0.0.1:12345
    $ reshell

Background
==========

Imagine *crazy* environment.
You can deploy Python package to remote host and have it running.
And for some reason it doesn't work.
But you don't have SSH access and can't debug it or see startup logs.
Also you don't know in advance what will be network address of the remote host.

But you have a dev machine in the same network, where you are free to run anything.
So you deploy reverse shell through regular deployment process
and poke around and figure out what's wrong.
