thatjohnmartin
==============

Not the other one.

Building and testing
--------------------

After creating a virtual env and installing requirements.txt, build the site with the following command:

    pelican -r content

And to serve the site:

    cd output
    python -m SimpleHTTPServer