scitools.org.uk
===============

This is the repository containing content found at scitools.org.uk.

Building content for scitools.org.uk
====================================

The content is generated by running the ``build.py`` script at the root of the
repository. ``build.py`` takes special template blocks from ``index.html`` and
injects them into the resulting html.


Adding built docs
-----------------

The html in this repository is a combination of generated and static content.
The built documentation for tools such as Iris and cartopy must be generated
using sphinx outside of this repository and subsequently added here. To do
so, create the appropriate folder (e.g. iris/docs/v2.2) with the built
documentation (typically created via sphinx).
Once the content is in place, consider running
``tools/symlink_common.py .`` from the root of the repository. This will look
through all files and share any common assets into the shared_assets
folder, thus reducing the overall repository size to those that need to clone
the repository.


Example workflow
----------------

To update scitools.org.uk so that it includes the Iris documentation for the
Iris 1.12 release the following steps need to be followed.

1. Build the Iris documentation using sphinx and add it to the scitools.org.uk repo.
```
$ cd <path_to_iris_repo>/docs/iris
$ make html
$ cp -a build/html <path_to_scitools.org.uk_repo>/iris/docs/v1.12
```

2. Update the `latest` symlink.
```
$ cd <path_to_scitools.org.uk_repo>/iris/docs
$ unlink latest
$ ln -s v1.12 latest
```

3. Update available versions in `iris/docs/version_switch.js`.

4. Generate the shared_assets.
```
$ cd <path_to_scitools.org.uk_repo>
$ python tools/symlink_common.py .
```


Adding contributors
-------------------

``contributors.json`` contains a JSON dictionary of all contributors who have
signed the scitools CLA. It is the definitive source of such contributors.
It is where the [CLA bot](https://github.com/SciTools-incubator/scitools-cla-checker)
looks to determine if a CLA is required.
If you've signed the CLA and aren't yet on this list, please consider submitting a PR
to speed the process up. 
A [rendered view](https://scitools.org.uk/signed_cla.html) of the list is also
available.


(C) British Crown Copyright 2010 - 2019, Met Office
