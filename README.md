# Description

plr is a command-line utility that can help prevent link rot by
automatically archiving links to the [Internet
Archive](https://archive.org). It works on markdown or plain text.

# Installation

TODO: AUR package, double check the following commands:

```bash
$ python3 -m venv .
$ source venv/bin/activate
$ pip install -r requirements.txt
```

# Usage

```bash
$plr -if inputfile.md -of outputfile.md
```

plr's file arguments are optional; it defaults to standard input and
output.

TODO: to return just a list of links, add the command-line flag `-list`

# About

**Link rot** is real, it is common, and it is pervasive. What is
**link rot**? Link rot is essentially *the process by which hyperlinks
cease to function, usually because the web page or server they point
to has moved or has become permanently unavailable*. It has existed
since the internet began. An example of its influence can be seen as
recently as 2000, when [a
study](http://dx.doi.org/10.1002/bmb.2003.494031010165) found that
within 24 months, 50% of .com domains and 20% of .gov domains were no
longer viable. [1] [Another
study](http://dx.doi.org/10.1017/S1472669614000255) found that 70% of
links in Harvard Law Review and 50% of links within the United States
Supreme Court opinions are no longer viable. [2] If we are to take the
internet as a primary resource seriously, then we seriously need to
think about undertaking a better way of long-term preservation of link
contents.

This is a fork of
[schollz/prevent-link-rot](https://github.com/schollz/prevent-link-rot).
Full credit for the original library and logic should go to
[schollz](https://github.com/schollz). This fork cannibalizes the
project with a [KISS](https://en.wikipedia.org/wiki/KISS_principle)
attitude. The goal is to create a small but useful command-line
utility and an accompanying library that can be integrated into other
projects.

## Todo

- ~~return a list of links instead of the full markdown contents with the `-list` command-line flag~~

- add the archive links *commented out* to the markdown content so the admin can un-comment as needed

- automatically ignore links that don't work (like nytimes) or provide alternative methods for them

- allow domain whitelists (so you aren't archiving links to your own website automatically)

- Detect relative links and fill in the original address to be able to convert (need a command-line option for the baseurl)
    - Find Relative Links
    - Figure out if link is relative to root, or directory ("./" or "/", or "")
    - Join Links
