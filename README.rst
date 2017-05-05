=================================
reshell - Reverse shell in Python
=================================

Deployment debugging with hacker's tools.

Install
-------

.. code:: bash

    pip install reshell

Usage
-----

On the host launch receiver with

.. code:: bash

    $ nc -lvp 12345

On destination host launch reverse shell:

.. code:: bash

    $ reshell 127.0.0.1:12345

(or with env variable instead of argument)

.. code:: bash

    $ export RESHELL_TARGET=127.0.0.1:12345
    $ reshell

Terminology
-----------

Since not all developers are familiar with hacker's technics,
I'll briefly describe what is this all about.

When you open terminal on your machine, it's **local** shell.

When you run SSH to connect to remote machine, it's **remote** shell.

When you listen on port on your machine and make remote machine to connect to you, it's **reverse** shell.

Ethics
------

This tool is **not** usefull **for** actual **hacking**.
Since you already have an ability to execute arbitrary code on remote machine,
it won't buy anything in terms of access.
You just need a shell as an *arbitrary code*.

Reverse benefits
----------------

Reverse shells have some advantages over remote shells:

1. **Bypass firewall** - incoming connections are often blocked on unused ports.
   Whereas outgoing connections are usually allowed.
2. **More secure** - instead of inviting everyone to backdoor, reverse shell communicates with single host:port
3. **Destination can be unknown** - even inaccessible.
   It's the host machine that must be accessible from the destination.
   Not the other way around.

Background (use case)
---------------------

Imagine *crazy* environment.
You can deploy Python application to *cloudy* remote host and have it running.
But you don't have SSH access and can't debug it or see startup logs.
Of course, application it doesn't work.
Also you don't know in advance what will be network address of the remote host.

But you have a dev machine in the same network, where you are free to run anything:
1. So you launch server on dev machine and deploy reverse shell through regular deployment process.
2. Once the application is deployed, it will connect to the server and turn itself into bash.
3. ... You can poke around and figure out what's wrong ...
4. PROFIT! 
