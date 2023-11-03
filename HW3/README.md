CSCI HW 3
Robert Fernald & Xavier Floyd

##Quick Start
### Local Test Setup
Install a Python 3 virtual environment with:
sudo apt-get install python3-venv

Create a virtual environment:
python3 -m venv python_venv

Activate the virtual environment:
source python_venv/bin/activate

Download and unzip the code from GitHub

Run requirements.txt:
pip3 install -r CSCI3700/HW3/requirements.txt

Start the server:
python3 CSCI3700/HW3/main.py

open the following pages in your browser to see the server is working:
127.0.0.1:5000
127.0.0.1:5000/api/unique
127.0.0.1:5000/api/update_basket_a