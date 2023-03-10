# screen-commander

A little utility to start multiple terminal sessions from a yaml file using GNU screen

## Installation

The tool uses GNU screen, make sure this is installed by using the packet manager for your platform.

```
pip install git+https://github.com/hdumcke/screen-commander@main#egg=screen-commander
```

Or, to install from source:


Clone this repo:

```
git clone --depth=1 https://github.com/hdumcke/screen-commander
```


Then run:
```
pip install -r requirements.txt
python setup.py install
```

## Usage

```
screen-commander run tests/simple.yaml
```

To list all running screen sessions:

```
screen -ls
```

To connect to a running screen session:

```
screen -r
```

Or if there are more then one screen session active add the session ID when you do screen -r

Once connected to a screen session you can move from one tab to an other using:

```
crtl-a <n>
```

where <n> is the number of the tab as shown on the status line.

To kill all running tabs use:

```
screen-commander kill tests/simple.yaml
```

Consult the documentation of GNU screen for more details how to use screen

## Status

I am using the tool on Ubuntu Linux and Mac OS and it does what I need it to do. Use Github issues or pull requests for feedback.
