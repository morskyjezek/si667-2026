# Beyond the Basics of the Command Line / Terminal Interface

_This tutorial is generally adapted to working in a UNIX environment using the bash shell, but there are various nods to Mac and Windows, which have some differences. Demonstrations during class assume use of Mac OS/Unix style terminal commands. However, commands for both unix and windows environments are offered below. See the linked resources at the bottom for greater detail._

## Description

Now that we have examined the basics of file navigation in the shell,
this lab asks you to connect those skills with your knowledge of
more advanced commands, as well as your understandings of files,
file systems, and file characterization. 

**Lab Questions:**

1. Use the `ls` command with a filter and a pipe to count all of the text files in the directory. What command are you using? How would you modify this to look in the subdirectories? How could you modify this to look for other file types?
1. Use the command line to generate a list of files in a directory, then output that list to a file. List the command that you would use on your system in your answer (and specify what system you’re using).
1. Above and in class we used the `find` command. Look at the find command `find . -type f -name '*.txt'` (described above). What would you expect the output of this command to be? Use your knowledge from our discussion, or test this in the shell to see what happens.
1. Use the commands `wc`, `sort`, and a pipes to devise a command that can list the `txt` files in the directory, and determine the longest and shortest files?   

**A future lab, following coverage of find, grep, and regex:**

1. Devise a way to use `find`, `grep`, `wc`, and a pipe to count how many csv files are in the sample file directory. Share your command, and share your count.   
1. Same commands as above, but devise a command that will search for TIFF files in the directories, keeping in mind that these files may have an extension of `tif` or `tiff`. 
