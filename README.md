# Tess

Manage your algorithms' implementations to be run against prepared and 
auto-generated test cases. Apply Stress Testing to detect issues when 
implementing new algorithms. Compare algorithms written in different languages 
with ease.

## Installation
Tess hasn't been tested on Windows, so if you are on a Windows machine, we 
recommend you to use a Linux distribution. You can access this 
[link](https://docs.microsoft.com/en-us/windows/wsl/install-win10) 
to learn how to install it.

### Dependencies
Before installing Tess, please make sure you have installed these dependencies:

* [Python](https://www.python.org/downloads/) >= 3.7 
* [Pip](https://pip.pypa.io/en/stable/installing/)
* [GCC](https://gcc.gnu.org/install/) (with support for C++14)
* [OpenJDK](https://openjdk.java.net/install/)

### Download
Run the next command from your terminal to download and install Tess:

    pip install -i https://test.pypi.org/simple/ tess-andresscode
    
## Setup
After installing Tess and all its dependencies, it is recommended to enable
the auto-completion feature for your terminal. Tess supports auto-completion
for **bash**, **zsh**, and **fish** shells. Run the next command to create
a shell script that will be used by your terminal to recognize Tess commands.

    tess auto-complete /location/where/you/want/to/store/the/script.sh

A file named **tess-completion.sh** will be created at your specified location.
Now, you need to add the next line to your **.bashrc** or **.zshrc** file.

    . /location/tess-completion.sh
    
>Remember to replace the path with the one where the file was created in the
>previous step.

If you are using _MacOSX_ you might have issues with the **zsh** terminal. If,
after sourcing from your **.zshrc** the auto-completion script you see an error,
or the Tess commands are not being auto-completed, you can add two extra lines
on top of the previous one to enable the auto-completion for the shell. Your
**.zshrc** file should look like this:

    autoload -Uz compinit
    compinit
    . /location/tess-completion.sh

Now, you should be able to start using Tess with its auto-completion feature on.

## Getting Started
You can watch how to use Tess [here](https://www.youtube.com/).

## Contribute
Tess is the result of the testing practices learned from the 
[Algorithmic Toolbox](https://www.coursera.org/learn/algorithmic-toolbox?specialization=data-structures-algorithms)
course offered by [Coursera](https://www.coursera.org/). It is a work in 
progress, aiming to help other students like me enrolled in the [Data Structures 
and Algorithms Specialization](https://www.coursera.org/specializations/data-structures-algorithms) 
to test their algorithms using the stress testing 
approach suggested in the course easing the process and allowing the students to 
use different programming languages to create their models and solutions.

### How can I contribute?
Tess is a new tool looking to grow and help more students and anyone who is 
interested and needs to test algorithms in an efficient and simple way, without 
restricting you to use a particular programming language or IDE. Currently, Tess 
is supporting three programming languages, **Python**, **C++**, and **Java**; 
one of the main goals of Tess is to give support to more programming languages 
but,  as the code base grows and more features are added, the need for a more 
reliable and flexible code is critical to achieving this. Here you can find a 
list of tasks that would help the project to grow and improve the user's 
experience:

* **Unit testing:** This is the top priority at this point.
* **Testing and reporting issues:** You can contribute using the tool and 
reporting any bugs to my [email](andressbox90@gmail.com).
* **Code documentation:** Code is not documented, this is critical to make it
easier for more developers to join in.
* **OOP migration:** Any contributions refactoring code to make it more 
object-oriented would be very appreciated. 

Please feel free to [contact me](andressbox90@gmail.com) to report something 
else that is not part of this documentation or if you want more information 
about the project and how to contribute.