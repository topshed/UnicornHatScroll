Unicorn Hat Scrolling text
==========================

This Python provides a simple way to generate a scrolling text message on a [Pimoroni Unicorn Hat] (http://shop.pimoroni.com/products/unicorn-hat).

Requirements
------------

[unicornhat] (https://github.com/pimoroni/UnicornHat)

bitarray

Installation
------------

pip install unicornhat
pip install bitarray
git clone https://github.com/topshed/UnicornHatScroll

Files
-----

**UHScroll.py**

The main file which defines all the functions 

**UHScroll_defs.py**

Contains all the character designs and mappings

**test.py**

A simple test program 

Usage
-----

```python
from UHScroll import *

unicorn_scroll(text,colour,brightness,speed)
```

*example:*
 
```python
unicorn_scroll('hello world','red',255,0.1)
```