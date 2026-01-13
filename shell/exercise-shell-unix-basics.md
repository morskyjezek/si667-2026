# Basics of the Command Line / Terminal Interface

_This tutorial is generally adapted to working in a UNIX environment using the bash shell, but there are various nods to Mac and Windows, which have some differences. Demonstrations during class assume use of Mac OS/Unix style terminal commands. However, commands for both unix and windows environments are offered below. See the linked resources at the bottom for greater detail._

## Description

This activity aims to present basic skills for using the "[command line](https://en.wikipedia.org/wiki/Command-line_interface)," a text-based system for working with the operating system and files on most laptop and dekstop computers (including MacOS, Windows, and Linux operating systems). A digital curator should have a basic level of comfort and competence with this interface for a few reasons: most importantly, the command line is an efficient and powerful environment that allows for basic creation of batch operations and simple scripts; in addition, some tools require operation from the command line. While not immediately intuitive, the command line and shell programs offer many quick and efficient ways to perform some actions, such as generating basic information about files and systems.

Keep in mind there are differences between the command line and the visual interfaces that may seem more comfortable. We generally interact with computers via a GUI (sounds like “gooey”); that is, a Graphical User Interface that allows you to interact with the system visually, through clicking, dragging and dropping, pointing and tapping, etc. In some cases, such as word processors, we call this WYSIWYG (“what you see is what you get”), when what you see on the screen is comparable to what you would expect to see when the file is printed out on a page or displayed on a website. In the command line interface (CLI), as when we are looking at markup files in a text editor, you can see what you do to get what you want. In some ways, it is a more transparent way to get a desired result because you have greater knowledge of what you have asked the computer to do, as well as what the computer is doing.

_Note: where you see “Mac” below, this generally designates a UNIX-wide command, “Windows” is generally DOS-like._

## General Structure for a Command

Most shell commands follow a typical syntax structure, which can be summarized like this:

`command` + `options` + `arguments`

The **command** is the short bit of text that you use to invoke a program, such as `ls`,
`mkdir`, or `find`. This is the most basic part of the command. 
Some commands can be run without any additional options or arguments.
The **options** are additional flags that give the program more
information about what you want it to do (e.g. `ls -a` or `mkdir -v`),
or allow you provide additional information (e.g., `find -type f`). 
Options are generally noted with a single hyphen followed by a letter 
(e.g., `-h`),
or a double hyphen followed by a word (e.g., `--help`); in many cases,
options are followed by additional information such as a number (e.g., `head -n 2`). 
Finally, **arguments** provide the program with information and input, 
often a file or file path. For example, `ls` can be supplied with a filepath of the 
location where you want list the files.

There are many commands, a few of which are covered below. It can be confusing at first
to remember all of the different commands, but don't worry - you're not alone, and
there are a lot of options to find out more information. One easy way to get more
details within the shell is to use `man` (short for manual), which will bring up
documentation for the command, which you have provided as an argument. For example,
`man find` tells you all about the ways you can use `find`. There are also many helpful 
resources, some of which are listed at the end of this document. If you're running on 
Git Bash (or other Windows flavors of the command line), you can use the option `-h` or 
`--help` on many commands to display similar instructions or explanation.

The rest of this reference document will cover two main actions:

1. Navigation - how to find where you are, move your location, and to look at other locations
1. Combining & Refining - how to combine commands and to refine your requests with filters or matching patterns
1. Inspection - how to learn more about files, look for specific kinds of files, or look at the contents of files

## Navigation 

This section covers commands that help you to find your way, move around, and to look at the contents of a location in the file system.

### Wayfinding and Moving Around

* determining where you are (Unix: `pwd` / DOS: `cd`)
* moving within the directory structure (`cd`)
* moving files (`mv`)

### Managing Files

* creating directories (`mkdir`)
* viewing/opening files (Unix: open / DOS: <type the file>; OR viewers like less(Unix)/more(Win); OR editors: vi, nano, ted and notepad)
* copying/moving files (Mac: `cp` / `mv` / Windows: copy con/move)

## Combining and Refining 

This section includes information on how to combine commands, to refine your requests, and create 
filters that matching patterns to look for specific types of information, like certain types of files

### Create File Lists

* listing contents of a current directory (Mac: `ls` / Windows: `dir` )
* using operators (hyphen and slash, depending on your system):
  * show all files (a)
  * recursion (-R or /s)
  * details (-l) (Mac only; you won’t need this on windows)
  * NB: these are just a few useful operators, there are many others!
* So, a basic UNIX command that lists file details and the hidden files is `ls -la`.
* You can further define a specific path if you want the command to list files in another directory: `ls -la /{MY Directory}/{MY subdirectory}`
* outputting lists (print to file: `>`)

### Filters

The UNIX command line offers ways for us to filter data. For example, 
what if you want to look for all of the files that are in JPEG format? 
For this task, you can use file expansion wildcards. These are special 
characters that the command line can use to filter results based on specific patterns.

Here are two useful ones that we can use in file filtering:

* `*` the asterisk character can be used to indicate a series of many characters. For example, the string `*.jpg` would look for any string with `.jpg` in it, but it may be preceded by any number of characters. This could be useful for looking for all of the JPEG files.
* `?` the question mark can be used to stand in for one or zero single characters. For example, if you want to look for `.jpeg` or `.jpg`, you could use the question mark to filter like `.jp?g`, which would match both the 3-letter and 4-letter patterns.

Note: this is generally a type of pattern matching, which is a larger topic. 
If you're interested in more advanced pattern matching, then regular expressions (discussed below)
are of more interest to you.  

### Combining Commands, or Piping Data

You can use the `|` and the `<` and `>` to move data between the commands. This stringing together, or "piping" 
data in between operations is useful since each command does about one thing. The pipe moves the data out to the next command, while the brackets access from or write to a file.

For example, you could use the `wc` command to count the lines in a file, pipe it to the `sort` command
to order by number, then use the `head -n 1` command to display the first line, ultimately displaying the longest or shortest file in the results.

## Inspecting Files

This section explores ways to look around the file system in more detailed ways, search for files 
based on specific criteria, and to filter information from outputs and files

### Finding files

The `find` command is a useful way to find files. The syntax is somewhat more complicated than
other commands, but it can be a powerful way to get an overview of items in a particular drive or directory.
One of the things tha makes `find` useful is that you can give it very detailed instructions about where to
look and what to look for. The syntax for `find` is as follows:

* `find` + `{location you want to search}` + `{options that you want to search for, designated by hyphen flags, like -type or -name of object, followed by the arguments for each`

For example:

* `find . -type f -name '*.txt'`

In the above:
* `find` initiates the find program,
* `.` indicates to search the current directory (you could specify
a different path here); note that in this case, the command is _recursive_, which means that
it will search any directories contained in the current path (`.`), but that is another thing you can
control if you investigate the options for this program further,
* `-type f` defines what type of object to look for, in this case `f` designates files
(you can also use `d` for directories or find other options here using the `man` page)
* `-name '*.txt'` limits the results to anything that has a string ending with the text `.txt`
in the name of the object.

In the lab activity, you are asked to describe what the output of this command would be.

Find can also be adapted to search for patterns using regular expressions. For example: 

* `find -E . -type f -regex ".*\.tiff?"`

In the above, the option `-E` indicates that the regular expression will use advanced operators 
(in this case, the question mark).
Then it is similar to the above, it looks for objects that are files. 
Finally, `-regex` indicates regular expression, followed by the expression in double quotes.
In this example, the expression looks for matches that are strings with any number of any characters (`.*`),
have a dot (`\.`), have a string of tif (`tif`), and then have zero or one instances of the 
character f (`f?`). In plain language, this expression will look in the current directory, 
search all of the files, and return matches for files ending with `.tif` or `.tiff`, which
are both likely possible extensions for a tif file. 

_[TODO - GREP, FILE, MD5]_

### Other useful commands for working with text data

* `sed` - the "stream editor" command allows you to efficiently remove text by line, filter particular characters using regular expressions, etc. 
* `tr` - the "translate" allows for use of regular expressions and the conversion, or easy removal, of particular character strings; can be useful for removing punctuation, converting upper to lower case, etc. 
* `awk` - useful for pulling information from files with data in standard formats on each line, among other things (for example, fixed-width data, or csvs); more complicated and expansive than `cut`.

### Other commands useful for inspecting files and the operating system

* `ps` lists the programs and processes that are currently running; if you run this without operators, it will show you what's running in the current container; if you run with the options aux, you will see all the processes on the operating system: `ps aux`
* `df` gives information about the file system usage
* `md5` creates an md5 checksum value
* `hexdump` gives a hex view of the file, useful for searching for magic numbers
* `dig` can provide information about the DNS entries of a website

### General Rules of Thumb

* Know the basic architecture of the file structure environment (some places you’ll expect many directories/folders, others you will expect mostly files)
* Have a general idea of the ways you might use this for basic digital preservation tasks (navigating, listing, describing).
* In performing preservation actions, you typically want everything to be reversible and tested in advance. Reversibility is not a hallmark of the command line (nor should it be assumed in a GUI environment).
* Don't be afraid of the command line, do be cautious: there are not always built-in safeguards as in the GUI environment. If you delete something from the command line, for example, it will not be moved to the trash before deletion - it will be removed immediately. This is not a cause for alarm, but it is a reminder to make sure you are doing exactly what you want, know how to do it (or ask someone who does), and don't proceed too quickly.

## Lab 2 Activities

**Answer these questions for January 23:**

1. Imagine that you have opened a window that gives access to the command line. What command would you use to determine your current location (current path address)?
1. What command would you use to move to another directory or folder?
1. What command would you use to list the contents of the directory or folder?
1. You can request a basic list (names of files and directories) and an advanced list (that shows permissions, file size, path, etc)? What command and options would you use to generate the basic list? What commands and options generate the advanced list?
1. What are the `.` and `..` directories?
1. Use the `ls` command with a filter (`*`) to determine how many `.jpg` files are in the top directory of this repository. What is the command? How many `.jpg` files are there? 
1. In what sorts of situations do you think that the command line interface would be useful or advantageous over the GUI? Give at least one example.
1. Do you feel more comfortable using the command line? Why or why not?

1. BONUS: Are there any `.jpeg` files? How many? Are these "the same" kind of files as `.jpg`? How can you look for both kinds? 

### Credits and Additional Resources

Another useful, and user-friendly, resource for searching for commands is [Explain Shell](https://explainshell.com/). A resource geared specifically toward archivists and librarians is the [_Script Ahoy_](https://dd388.github.io/crals/) resource. In addition, the "[Wizard Zines](https://wizardzines.com/)" by Julia Evans
offer a friendly and visually engaging pathway into many of these skills.

See these additional resources for more detailed information:

* B. Lyons, [Introduction to Using the Command Line Interface](https://www.weareavp.com/an-introduction-to-using-the-command-line-interface-to-work-with-files-and-directories/) (2014); versions for both MAC and Windows OS.
* C. Severance, _Python for Everybody_: tips for [Mac](https://www.py4e.com/software-mac.php), tips for [Windows](https://www.py4e.com/software-win.php).
* [Copy, Create, Rename and Remove Unix Directories](http://documentation.its.umich.edu/node/295)
* Wikipedia, [Find (Unix)](https://en.wikipedia.org/wiki/Find_(Unix))
* Art of the Command Line https://github.com/jlevy/the-art-of-command-line
* [Bash cookbook for archivists](https://avpres.net/Bash/)
* [Script Ahoy](https://dd388.github.io/crals/) resource for archivists