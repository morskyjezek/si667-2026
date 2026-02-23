# # Using BagIt
# 
# This python script is set up to provide a "fill in the blank" structure
# for you to complete. If you want to see a complete, worked example,
# which shows how each cell would or should look when it has run,
# see [a complete example in a Jupyter notebook](https://github.com/morskyjezek/bagit-walkthrough-lcwa/blob/main/01a-using-bagit-completed.ipynb).
# 
# ## Setup
# 
# If you don't already have the bagit library installed, you may need to get it. 
# To install the library, you will need to run "pip install bagit" in your shell or package manager.
# If you don't have bagit installed, install following instructions at https://github.com/LibraryOfCongress/bagit-python

# Once the bagit library is installed and ready, you can begin this activity.

## Step 1: import the library

### Step 1a: if you choose to input the date dynamically 
# (that is, by using the information from your computer's operating system),
# also import the date function

## Step 2: Create the Bag tags (i.e., the descriptive metadata)
# Using the Python bagit library, you can create “BagInfo” information,
# which will be stored in a Python dictionary.
# Assign this dictionary to a variable called `my_BagInfo`, 
# which will be inserted as an argument later when you bag the files. 
# Add your name, an organization, and a description of the files in the bag.


my_BagInfo = {
    'Source-Organization': 'Data Curation Training Pros, via Library of Congress (LC)',
    'Contact-Name' : 'Jesse', # <- type your name here
    'Contact-Email': 'hello@some.email', # <- type your email here
    'External-Description': 'These are sample files from the Library of Congress Web Archives that we wanted to structure in BagIt for practice.',
    'External-Identifier': 'myfiles:documents/test/files/1234', # <- this would be something like a call number or collection ID, if the content corresponds to a catalog description or digitized item
    'Source-URL': 'https://www.loc.gov/programs/web-archiving/about-this-program/', #this is a reference URL for the collection, in this case doesn't point to each individual file
    'Collected-Date': '2021-10-12',
}


### Step 2a: add date info
my_BagInfo['Demonstration-Date'] = str(dateStamp) #string of date formatted following ISO date standard format YYYY-MM-DD


## to confirm that the metadata is complete, you can print out the bag tag dictionary.

print('Bag Info:\n\n',
      my_BagInfo,
     '\n\nDatatype: ',type(my_BagInfo))


## Step 3. Bag the FilesUse BagIt to make the bag: make_bag()
# The bagit module includes a function called `make_bag()`
# to create BagIt objects from a specific path or directory.
# Set up the function by providing as arguments:
# - the location of the files that you want to bag (`sample-files`),
# - with the `bag_info` option to create unique descriptive information using the `my_BagInfo` dictionary:

# create the bag; note that the tool does not give feedback, so use a try/except 
# to create the effect of giving a response message
try:
     # <-- insert make_bag() here
    print('Success!')
except:
    print('No bag created :(')

# If the cell runs and you don't see the error message, this created a bag,
# which is accessible as a python object in the `my_bag` variable. 


# display the contents of sample-files directory

# Finally, use the validate bag function to validate the bag of files you just created.