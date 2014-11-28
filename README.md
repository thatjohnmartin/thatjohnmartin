thatjohnmartin
==============

Not the other one.

Building and testing
--------------------

After creating a virtual env and installing requirements.txt, set the build-and-watch running:

    make regenerate

And to clean, build, and publish:

    make github
    
To serve the site locally on port 8000:

    cd output
    python -m SimpleHTTPServer