from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line

import btccore

sats = 100000000

kv = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: e1
                min: -360.
                max: 360.
'''

class Wallet_GUI(App):
	def build(self):
		#parent = Widget()
		#painter = MyPaintWidget()
		"""
		toplayout = BoxLayout(padding=10,orientation='vertical')
		parent = BoxLayout(padding=10, orientation='horizontal')
		parent2 = BoxLayout(padding=10, orientation='horizontal')
		toplayout.add_widget(parent)
		toplayout.add_widget(parent2)
		"""

		griddy = GridLayout(cols=1,row_force_default=True,row_default_height=40,spacing=5,padding=10)
		updates = Label(text='updates go here...')	
		address_label = Label(size_hint_x=None,width=150, text='address: ')	
		amount_label = Label(size_hint_x=None,width=150, text='amount: ')	
		fee_label = Label(size_hint_x=None,width=150, text='fee :')	
		import_label = Label(size_hint_x=None,width=150, text='import :')	

		address_input = TextInput(text="", multiline=False, size_hint_x=None, width=300)
		amount_input = TextInput(text="", multiline=False, size_hint_x=None, width=300)
		fee_input = TextInput(text="", multiline=False, size_hint_x=None, width=300)
		import_input = TextInput(text="", multiline=False, size_hint_x=None, width=300)
		
		clearbtn = Button(text='Clear', size_hint_x=None, width=150)
		exitbtn = Button(text='Exit', size_hint_x=None, width=150)
		sendbtn = Button(text='Send', size_hint_x=None, width=150)
		importbtn = Button(text='Import', size_hint_x=None, width=150)

		parent = BoxLayout(orientation='horizontal')
		parent.add_widget(address_label)
		parent.add_widget(address_input)
		griddy.add_widget(parent)
		parent = BoxLayout(orientation='horizontal')
		parent.add_widget(amount_label)
		parent.add_widget(amount_input)
		griddy.add_widget(parent)
		parent = BoxLayout(orientation='horizontal')
		parent.add_widget(fee_label)
		parent.add_widget(fee_input)
		griddy.add_widget(parent)
		parent = BoxLayout(orientation='horizontal')
		parent.add_widget(sendbtn)
		parent.add_widget(importbtn)
		griddy.add_widget(parent)
		parent = BoxLayout(orientation='horizontal')
		parent.add_widget(clearbtn)
		parent.add_widget(exitbtn)
		griddy.add_widget(parent)
		parent = BoxLayout(orientation='horizontal')
		parent.add_widget(import_label)
		parent.add_widget(import_input)
		griddy.add_widget(parent)
		parent = BoxLayout(orientation='horizontal')
		parent.add_widget(updates)
		griddy.add_widget(parent)
	
		"""
		#parent.add_widget(painter)
		parent.add_widget(clearbtn)
		parent.add_widget(exitbtn)
		parent2.add_widget(updates)
		parent2.add_widget(input0)
		"""

		def empty_textboxes(self):
			address_input.text = ""
			fee_input.text = ""
			amount_input.text = ""
			import_input.text = ""
			updates.text = "Text boxes have been cleared."

		def import_key(self):
			if importbtn.text == "":
				updates.text = "Please enter a new bitcoin key to import."
			else:
				btccore.changewallet(importbtn.text)
				importbtn.text = ""
				updates.text = "Wallet has been updated."
		
		def send(self):
			am = int(float(amount_input.text)*sats)
			fee = int(float(amount_fee.text)*sats)
			outp = btccore.perform_transaction(address_input.text,am,fee)
			print(outp)
			updates.text = "New transaction Performed! -- IS \n" + str(outp)

		clearbtn.bind(on_release=empty_textboxes)
		exitbtn.bind(on_release=quit)
		sendbtn.bind(on_release=send)
		importbtn.bind(on_release=import_key)
		global kv
		Builder.load_string(kv)
		return griddy


if __name__ == '__main__':
	Wallet_GUI().run()
