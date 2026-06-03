# update system
apt-get update
apt-get upgrade -y
# install Linux tools and Python 3
apt-get install software-properties-common wget curl
# install Python packages
pip install --user -r .devcontainer/requirements.txt
# install recommended packages
apt-get install zlib1g g++ freeglut3-dev \
    libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev libfreeimage-dev -y
# clean up
pip cache purge
apt-get autoremove -y
apt-get clean