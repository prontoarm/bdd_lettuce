lettuce test
=======

base lettuce setup

## Installation

You may already have pip and/or nose installed. They are required to install/run the framework.

#### pip:

    [sudo] easy_install pip

#### env package:

    [sudo] pip install -r setup.pip

#### chromedriver:

Download the zip from http://code.google.com/p/chromedriver/downloads/list, unzip and move chromedriver executable into your path, i.e.:

    mv ~/Downloads/chromedriver /usr/local/bin


## Running features manually:

Assuming you have a features directory, this command will run all of the .feature files in your features directory.

    lettuce features
