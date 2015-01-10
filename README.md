# Pelican blog post aliaser for Blogger posts

## What is it?

Take Pelican blog posts in Markdown format and use the date and slug
metadata to automatically generate an alias for use with
[pelican-alias](https://github.com/Nitron/pelican-alias).

By default, I'm intending to use simpler URLs for my posts than the ones
Blogger used which contain year and month, so used this to add the old
URLs to my posts. That way, any links to the old posts should still be
valid.

## How to use it?

Put `alias_posts.py` in the same directory as your unaliased .md files
and run it. The script creates an output directory:
`posts_with_added_alias` containing modified files and leaves the
original files unmodified.

Posts need to have "Date:" and "Slug:" entries, formatted as below.
(Not bothered to make this more flexible as it was primarily for my own
use, but feel free to modify.)

### Date

Needs to be:

```
Date: YYYY-MM-DD HH:MM
```

### Slug

The slug you've used in your post should be the slug without `.html`
from a Blogger post URL like:

```
{your_blog_domain}/YYYY/MM/{slug}.html
```

If {slug} was `post-about-something-really-interesting`, then
the slug line in your Pelican post metadata needs to be:

```
Slug: post-about-something-really-interesting
```

`alias_posts.py` makes a new directory containing posts with added
aliases.

The alias format will then be `/YYYY/MM/slug.html` (which Blogger uses).
