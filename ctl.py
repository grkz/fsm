#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cpu import Cpu

class State:
	"""Controls machine state."""
	def __init__(self, state_dict, initial_coins_set, ticket_price):
		"""Sets initial state."""
		self.state = 'broken'
		self.state_dict = state_dict
		self.initial_coins_set = initial_coins_set
		self.ticket_price = ticket_price
		self.set_state(self.state)
	def get_state(self):
		"""Prints last machine's state."""
		if self.state_dict.has_key(self.state):
			print "\nMachine's last state: ", self.state_dict[self.state], "description: ", self.state
		else:
			print "This machine has ony following states:"
			for x, y in self.state_dict.iteritems():
				print x + ":\t" + str(y)
	def set_state(self, state_name):
		"""Sets machine to specified state."""
		self.state = state_name
		if self.state_dict.has_key(state_name):	
			if self.state_dict[state_name] == 0:
				self.demo = Cpu(*self.initial_coins_set)
				self.demo.set_price(self.ticket_price)
			elif self.state_dict[state_name] == 1:
				self.demo.buy()
			elif self.state_dict[state_name] == 2:
				self.demo.pull_out_money()
			elif self.state_dict[state_name] == -1:
				pass
		else:
			print "\nThis machine has no state '" + state_name + "'!"
			

