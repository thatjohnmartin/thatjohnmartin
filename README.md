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

And to publish as a user page:

    ghp-import output
    git push -f git@github.com:thatjohnmartin/thatjohnmartin.github.io.git gh-pages:master