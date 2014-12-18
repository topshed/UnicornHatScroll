''' This python script provides the functions to display simple scrolling text on
a Pimoroni Unicorn hat, and add-on board for the Raspberry Pi model B+'''

import unicornhat as UH 
from bitarray import bitarray
import time
#import letter definitions and mappings
from uhscroll_letters import *

'''It assumes the Pi/hat will orientated with the long side of the Pi without any connectors on
the bottom, i.e. the Hat will be rotated 90 degrees clockwise (assuming the "UNICORN HAT" label and 
Pimoroni logo are normally at the bottom of the hat. If you want to use a different orientation  
then you can alter the UH.rotation value in the show_letter function below. You may also need to adjust or omit
the flip call which is used to ensure that the bitarray definitions in uhscroll_letters are the correct 
way round for easy reading'''

flip = [7,6,5,4,3,2,1,0]

def show_letter(letter,colour): #displays a single letter on th UH
	UH.rotation(270)		
	for i in range(8):
		for j in range(8):
			if letter[j][i]:
				UH.set_pixel(j,flip[i],colour,colour,colour)
			else:
				UH.set_pixel(j,flip[i],0,0,0)

	UH.show()

def scroll_letter(letter,colour,speed): # scrolls a single letter across the UH
	for i in range(8):
		for p in range(6):
			letter[i].insert(0,False)
	for s in range(14):
		show_letter(letter,colour)
		time.sleep(speed)
		for i in range(8):
			letter[i].pop(0)
			letter[i].append(0)

'''scrolling is achieved by redrawing the letter with a column of the bitarray shifted to the left and a new blank column
added to the right'''
def scroll_word(word,colour,speed): # scrolls a word across the UH
	for s in range(len(word[0])):
		show_letter(word,colour)
		time.sleep(speed)
		for i in range(8):
			word[i].pop(0)
			word[i].append(0)

def make_word(words): # takes a list of chars and concats into a word by making one big bitarray
	bigword = [bitarray(''),bitarray(''), bitarray(''),bitarray(''), bitarray(''),bitarray(''), bitarray(''),bitarray('')]
	for w in range(len(words)):
		for i in range(len(words[w])):
			bigword[i] = bigword[i] + words[w][i]
	return bigword
	
def trim_letter(letter): #trims a char's bitarray so that it can be joined without too big a gap
	trim = []
	for c in range(len(letter)):
		trim.append(letter[c].copy())
	for i in range(8):
		if letter not in wides:
			trim[i].pop(0)
		trim[i].pop(0)
		trim[i].pop(5)
		if letter in narrows:
			trim[i].pop(0)
	return trim

def map_character(chr):
	if chr in mapping:
		return mapping[chr]
	else:
		return mapping['_']

def load_message(message):
	unicorn_message = []
	for ch in (range(len(message))):
		unicorn_message.append(trim_letter(map_character(message[ch].upper())))
		
	return(unicorn_message)
#for r in range(1000):
#	show_letter(letter_L,255)
#	time.sleep(0.001)
#	show_letter(letter_K,255)
#	time.sleep(0.001)
#b = map_character('H')
#print b
#scroll_letter(letter_A,255,0.5)
#scroll_letter(letter_B,255,0.5)
#scroll_letter(letter_C,255,0.5)
#hell = []
#hell.append(trim_letter(letter_H))
#hell.append(trim_letter(letter_E))
#hell.append(trim_letter(letter_L))
#hell.append(trim_letter(letter_L))
#hell.append(trim_letter(letter_M))
#hell.append(trim_letter(letter_B))
#print hell
#hello = load_message('HELLO')
#print hello
#test = make_word(hello)
#print test
#scroll_word(test,255,0.5)
#scroll_word(make_word(load_message('titsjack')),255,0.2)

def unicorn_scroll(text,colour,speed):
	scroll_word(make_word(load_message(text)),colour,speed)

	


