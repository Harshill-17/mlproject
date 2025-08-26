# First import the Following Package.
from setuptools import find_packages, setup 
# find_packages will automatically find packages that are available into the ML application Directory we have created


# now when we create the application we need some parameters like what is the name of the package, version, description of the project, what application of the project so create the setup() like below.

# you can consider setup() as the metadata information.


from typing import List

HYPEN_E_DOT = '-e .'

def get_requirenments(file_path:str)->List[str] :
    # this function accept the file into the form of the string and return into the form of the list which will be string
    
    requirenments = [] # create a empty list to store the libraries that comes form the requirenments.txt
    
    # Now i'll open the file_path in the form of the file_obj 
    with open(file_path) as file_obj :
        # file_obj read all the lines of the file_obj and stored into the requirenment 
        requirenments = file_obj.readlines()
        # after that i'll use the list comresive to replace the \n to "" [req.replace("\n", "") for req in requirenments] because when it readline by line after the new line it automatically add the \n so we had to convert that \n into the "" and replace into the requirenments
        requirenments = [req.replace("\n", "") for req in requirenments]
        
        # Now remember one thing always use the -e . into the requirenments.txt file because it will be automatically triggers the setup.py file but in setup.py file we don't need the -e . 
        # so, we had to remove that for that we create the following condition.
        # HYPEN_E_DOT nothing just a global variable that we had created.
        
        if HYPEN_E_DOT in requirenments :
            requirenments.remove(HYPEN_E_DOT)
        
    # After all of that just Retuning the requirenments
    return requirenments

setup(
    
    name = 'mlproject',
    version='0.0.1', # this was my first version when i update i'll update the version
    author='Harshil Darji',
    author_email='harshilsunildarji@gmail.com',
    packages=find_packages(), # it will be help us to find the packages.
    
    # for the Basic Understand first show that - install_requires=['pandas', 'numpy', 'seaborn'] 
    # the library you want to install into the project it will be write into the form of the list.
    
    install_requires = get_requirenments('requirenments.txt')
)

''' 
After the creating the setup.py how that file will find the packages?
- so that i'll create a folder name src.
- in that folder i'll one file named __init__.py
- so when the find_packages() run it go to the __init__.py file and show howmany folders you have in that particular file so it will be directly consider the src folder as the Package. and it will try to build this and when it wil be build you were import it anywhere like how we import seaborn, pandas and etc. 
- our entire project will be done into this src folder __init__.py file.

'''

'''

Now we create the Realworld Project we don't know how many packages we need for that project. we cannot write the all the libraries into install_requires=['pandas', 'numpy', 'seaborn'] one by one.

so, we create one function.

get_requirenment(requirenments.txt)
this function will help us to get the library that wil be install one by one which was given into the requirenments.txt file.

'''