# profiles REST API

REST API basic functionality for managing user profiles

the virtualenvwrapper was a huge problem for me so I find these solution in stackoverflow
you should add this to your .bashrc file which can be found when you up your vagrant with ssh
for editing you can use vim and then press I for inserting :

export WORKON_HOME=~/virtualenvs
source /usr/local/bin/virtualenvwrapper.sh


after adding this two line above you should also copy paste this in your vagrant terminal:

source ~/.bashrc

mkdir -p $WORKON_HOME

then you are now okay with making virtual environment like
mkvirtualenv yourprojectname
