# CSCI 3700 Database Management Systems
## HW 3
### Robert Fernald & Xavier Floyd

#### Virtual Environment Setup
Install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

Activate the virtual environment:
```
source python_venv/bin/activate
```

Download and unzip the code from GitHub
Move the folder to the home directory,
Alternatively you need to use the folder's location when running commands
[parent folder]/CSCI3700/HW3/main.py

Run requirements.txt:
```
pip3 install -r CSCI3700/HW3/requirements.txt
```

##### Server Testing
Start the server:
```
python3 CSCI3700/HW3/main.py
```

open the following pages in your browser to see the server is working:

for the welcome page:
```
127.0.0.1:5000
```

to see the unique items in basket_a and basket_b:
```
127.0.0.1:5000/api/unique
```

add 5, Cherry to basket_a
```
127.0.0.1:5000/api/update_basket_a
```

reload the unique items page to see that an item was added:
```
127.0.0.1:5000/api/unique
```