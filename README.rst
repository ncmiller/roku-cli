roku-cli
========

Interactively control your Roku device from the command-line with vim-style key bindings.

.. image:: https://travis-ci.org/ncmiller/roku-cli.svg?branch=master
    :target: https://travis-ci.org/ncmiller/roku-cli

Who needs this?
--------------------

This was made for lazy people who live on the command line.

(Story time) I was sitting on the couch with my laptop, Netflix on in the
background, when suddenly and without warning, the credits are rolling - it's time
to find something else to watch before "Real Rob" starts playing.
The remote is **all** the way over on the coffee
table. I can't be expected to stop what I'm doing, put my laptop down, use
the remote, sit back down, and resituate myself with my laptop. There has to be
a better way...

Luckily, `python-roku <https://github.com/jcarbaugh/python-roku>`_ exists,
which makes it easy to control my Roku with
Python. Add a simple interactive CLI, and now I'm Roku-ing in style without
ever leaving the terminal.

There are a few practical advantages of roku-cli vs. the remote:

* Responsiveness - Moving around the Roku has never been faster
* Easy text entry - No more hunting around the on-screen keyboard with
  the arrow keys
* Control any Roku in the house - If you have multiple Roku's, you can select
  which one you want to control
* Stay on the command line - No more context switching between your
  computer and the real world

Installation
------------

::

    pip install rokucli

Or to install the latest source::

   git clone https://github.com/ncmiller/roku-cli.git
   cd roku-cli
   python setup.py install

Supported with Python 2 and 3 on Linux and Mac OS. Also works with Cygwin on
Windows. Sorry, no native Windows support.

Usage
-------

To launch the CLI::

    $ roku

With no arguments, Rokus within the LAN will be discovered using `SSDP
<http://en.wikipedia.org/wiki/Simple_Service_Discovery_Protocol>`_.
If only one Roku is found, then it will be selected, otherwise you'll be
asked to select one::

    Found the following Roku devices:
    [1]   192.168.1.116:8060 (Roku 3-4230X SW v7.2.0.4100)
    [2]   192.168.1.147:8060 (Roku 3-4200X SW v7.2.0.4100)

    Multiple Rokus found. Select the index of the Roku to control:
    Select (1 to 2) >

Alternatively, if you already know the IP address of your Roku, then launch the
CLI with the IP as the first argument::

    $ roku 192.168.1.118

This method is much faster than SSDP.

From there, you'll be in interactive mode, and you can input keys to control
your Roku::

    +-------------------------------+-------------------------+
    | Power          p              | Replay          R       |
    | Back           B or <Esc>     | Info/Settings   i       |
    | Home           H              | Rewind          r       |
    | Left           h or <Left>    | Fast-Fwd        f       |
    | Down           j or <Down>    | Play/Pause      <Space> |
    | Up             k or <Up>      | Enter Text      /       |
    | Right          l or <Right>   | Volume Up       V       |
    | Ok/Enter       <Enter>        | Volume Down     v       |
    |                               | Volume Mute     M       |
    +-------------------------------+-------------------------+
    (press q to exit)
