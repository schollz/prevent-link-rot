# Prevent Link Rot

**Link rot** is real, it is common, and it is pervasive. What is **link rot**? Link rot is essentially *the process by which hyperlinks cease to function, usually because the web page or server they point to has moved or has become permanently unavailable*. It has existed since the internet began. An example of its influence can be seen as recently as 2000, when [a study](http://dx.doi.org/10.1002/bmb.2003.494031010165) found that within 24 months, 50% of .com domains and 20% of .gov domains were no longer viable. [1] [Another study](http://dx.doi.org/10.1017/S1472669614000255) found that 70% of links in Harvard Law Review and 50% of links within the United States Supreme Court opinions are no longer viable. [2] If we are to take the internet as a primary resource seriously, then we seriously need to think about undertaking a better way of long-term preservation of link contents.

## How stop link rot

Link rot can be combated in several ways.

1. Use a [digital object identifier](http://www.doi.org/) which provides persistent and actionable identification. The a website under a DOI changes, it can be changed in the DOI service so that the unique DOI identifier always links to the most up-to-date material.
2. Use a [permanent web framework](http://ipfs.io/). Our current web protocol has many nodes of failure, while newer hypermedia frameworks seek a more distributed protocol with builtin content identies that would allow data to permanently be available.
3. Only link to archiving sites like the [Internet Archive](https://archive.org/web/) or [perma.cc](https://perma.cc/). **My little program I've written helps to combat link rot by providing a simple and easy way to convert all your links to an archived link.**

# Install and Run

## Snapshot

![Screenshot](http://i.imgur.com/LSM8HUU.jpg)

## Install

```bash
$ virtualenv -p /usr/bin/python venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
```

## And run

```bash
(venv)$ python app.py
```

Goto ```http://127.0.0.1:8012/``` to use the web page to convert links.

## Demo

Try the demo [here](http://permalinker.duckdns.org/).

# References

1. Markwell, John, and David W. Brooks. "“Link rot” limits the usefulness of web‐based educational materials in biochemistry and molecular biology*." Biochemistry and Molecular Biology Education 31.1 (2003): 69-72.
2. Zittrain, Jonathan, Kendra Albert, and Lawrence Lessig. "Perma: Scoping and addressing the problem of link and reference rot in legal citations." Legal Information Management 14.02 (2014): 88-99.
