#!/usr/bin/env python
# encoding: utf-8
import datetime
import glob
import os


class FileHasAliasException(Exception):
    """ Exception to raise if blog post already has alias added. """
    pass


def get_lines_from_file(name):
    """ Return list of lines from input file. """
    with open(name, 'r') as input_file:
        return input_file.readlines()


def write_output_file(name, lines):
    """ Write iterable of strings to output file. """
    with open(name, 'w') as output_file:
        output_file.writelines(lines)


def add_alias_to_contents(post_contents):
    """ Take iterable containing post lines; return lines with alias added. """
    count = post_contents.index('\n')
    header = post_contents[:count]

    for item in header:
        if item.startswith('Date:'):
            pub_datetime_as_string = item.lstrip('Date: ').rstrip()
            pub_datetime = datetime.datetime.strptime(pub_datetime_as_string,
                                                      "%Y-%m-%d %H:%M")
            string_date = pub_datetime.strftime('/%Y/%m/')
        if item.startswith('Slug:'):
            slug = item.replace('Slug: ', '').rstrip()
        if item.startswith('Alias:'):
            raise FileHasAliasException
    
    assert string_date, "No date!"
    assert slug, "No document slug!"
    alias_line = "Alias: " + string_date + slug + ".html\n"
    return header + [alias_line] + post_contents[count:]


def process_blog_post(filename, output_directory):
    """ Take input blog post; add Alias: line if none exists. """
    post_contents = get_lines_from_file(filename)
    
    try:
        lines = add_alias_to_contents(post_contents)
    except FileHasAliasException:
        pass
    else:
        pathname = os.path.join(output_directory, filename)
        write_output_file(pathname, lines)


def main():
    """ Read in .md Pelican posts with date and slug; add Alias: line. """
    # http://stackoverflow.com/questions/273192
    directory_name = 'posts_with_added_alias'
    try:
        os.makedirs(directory_name)
    except OSError:
        if not os.path.isdir(directory_name):
            raise

    for blog_post in glob.glob('*.md'):
        process_blog_post(blog_post, directory_name)

if __name__ == '__main__':
    main()
