# # Using BagIt
# 
# This notebook is set up with blanks for a teaching demo. If you want to see the 
# entire notebook, with examples of how each cell looks when it has completed,
# see [a completeld Jupyter notebook example here](https://github.com/morskyjezek/bagit-walkthrough-lcwa/blob/main/01a-using-bagit-completed.ipynb).
# 
# ## Learning Objectives
# 
# After completing this lesson, students should be able to:
# 
# * Implement the BagIt specification, and examine the file system to see how a BagIt object is structured.
# * Identify and use shell tools (`ls`, `cat`) to conduct initial checking and validation of a BagIt object.
# * Use the `bagit` Python module to create a BagIt bag, which includes fixity, manifest, and basic descriptive information.

# ## Setup
# 
# Now let's look into how we can create a BagIt object for some sample files. 
# This notebook will demonstrate how 
# to do that using a Python module called `bagit`, from files on your computer. If you want to follow this notebook,
# the instructions explain the process, step by step, for a folder of sample files in this Git repository. 
# 
# If you don't already have the bagit library installed, you may need to get it. You can run the 
# following cell to install it with pip, by uncommenting the last line (remove the `#`) and then running the cell.

# If you don't have bagit installed, install following instructions at https://github.com/LibraryOfCongress/bagit-python
# Alternatively, you can use the magic command on the line below by removing the hashtag and running the cell.
# (When the command below runs, you will see response output appear below this cell as the program downloads and installs.)
#!pip install bagit

# To begin, set up by importing the library:

# import the library

# If you want to explore the "dynamic" creation of dates, as shown below, you will also need the `date` function from the `datetime` library:

# to demonstrate automated creation of metadata, also import the date function

# You will also need the `json` library so that you can import the descriptive metadata template,
# which is saved as a `.json` file. 😺

# ## Bag the Files
# 
# Now, you will work to transform the `PKG-legacy-files` directory into a BagIt information package. In general, these are the steps: 
# 
# 1. Look at what's there before you start?
# 2. Create BagInfo metadata
# 3. Use `bagit` to make the bag

# ### 1. Look at what's there
# 
# We will use the bagit tool to create a valid BagIt object from the directory called `PKG-legacy-files`. First, take a look at what's in this directory.
# 
# - Note: run shell commands from the notebook by putting an exclamation point character at the beginning of the line

# use the list command to see what's there

# The output of the above cell depends what you are asking the list command to list.
# If you are listing `PKG-legacy-files`:
# 
# - You should see nine files of various formats
# 
# But for the lab, when you are working on `PKG-web-files-small`, you should see:
# 
# - You should see five folders and one csv file

# ### 2. Create BagInfo metadata
# 
# The bagit library helps to create basic description information called "BagInfo," which is stored in a file called `bag-info.txt`. In the python environment, this information is stored in a python dictionary, which is later by using a Python dictionary. This example uses a variable called `my_BagInfo` for the bag information. Once this metadata is created, it will be added automatically during bag creation. If you use the code below, replace the placeholders in the bag information wit information appropriate to the project you’re working on.
# 
# This demonstration imports the bag information template from the `bag-info-template.json` file.

# _Use the following cell if you are having trouble importing the template from the JSON file._

# create baginfo data; if you can't import the JSON file, 
# run this cell after you remove the three ticks above and below the baginfo 
'''
my_BagInfo = {
    'Source-Organization': 'Data Curation Training Pros, via Library of Congress (LC)',
    'Contact-Name' : 'Jesse', # <- type your name here
    'Contact-Email': 'hello@some.email', # <- type your email here
    'External-Description': 'These are sample files from the Library of Congress Web Archives that we wanted to structure in BagIt for practice.',
    'External-Identifier': 'myfiles:documents/test/files/1234', # <- this would be something like a call number or collection ID, if the content corresponds to a catalog description or digitized item
    'Source-URL': 'https://www.loc.gov/programs/web-archiving/about-this-program/', #this is a reference URL for the collection, in this case doesn't point to each individual file
    'Collected-Date': '2021-10-12',
}
'''

print('Datatype: ',type(my_BagInfo))

# ### Automate date info
# 
# The `date` functions (imported earlier) will suffice to create date information. If you run the `.today()` function, python should be able to identify the current system date from your system.

# create the dateStamp variable, check the type

# Then, add the date to the bag information in a variable called `Demonstration-Date`.


# And confirm that the information has been added.
print(my_BagInfo)

# ### 3. Bagging the Files
# 
# The bagit module includes a function called `make_bag()` to create BagIt objects from a specific path or directory. We will set up the function by providing as arguments the location of the files that we want to bag (`PKG-legacy-files`), with the `bag_info` option to create unique descriptive information using the `my_BagInfo` dictionary:

# create the bag; note that the tool does not give feedback, so use a try/except 
# to create the effect of giving a response message
#try:
    # <-- insert make_bag() here
#    print('Success!')
#except:
#    print('No bag created :(')

# ## Resources
# 
# See these additional resources for more detailed information:
# * B. Lazorchak, ["From There to Here, from Here to There, Digital Content is Everywhere!"](https://blogs.loc.gov/thesignal/2012/01/from-there-to-here-from-here-to-there-digital-content-is-everywhere/), _The Signal_ (3 January 2012).
# * State Archives of North Carolina, "[Bagger GUI User Guide](https://files.nc.gov/dncr-archives/documents/files/using_bagger.pdf)" (Updated 2012, v. 1.5), available as of March 2018.
# * M. Phillips, ["What do we put in our BagIt bag-info.txt files?"](https://vphill.com/journal/post/4142/) (2015).
# * UNT Libraries, UNT OAIS Information Package Specification (2015), https://www.library.unt.edu/sites/default/files/documents/digital-libraries-uploads/Appendix_M_UNT_Libraries_OAIS_Information_Package_Specification.pdf


