#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Cpu:
	"""Model of a ticket machine."""
	__allowed = [0.05, 0.10, 0.20, 0.5, 1.0, 2.0, 5.0] # allowed coin values
	
	def __init__(self, *init):
		self.__money = dict.fromkeys(self.__allowed, 0)
		print "Initial state:"
		self.__accept_coins(*init)
		self.__input = []	# buffer for user input
		self.list_coins("", self.__money)
	def set_price(self, price):
		"""Sets the ticket price."""	
		self.__price = price

	def buy(self, *input):
		"""Return the reminder for the given user input."""

		print "\nBuying a ticket. Ticket price is %.2f PLN." % self.__price
		self.insert_coins()
		inserted_coins_value = sum(self.__input)
		print "Total value of inserted coins: %.2f" % inserted_coins_value
		reminder = inserted_coins_value - self.__price
		returned_coins = dict.fromkeys(self.__allowed, 0)
		if reminder < 0:
			print "Not enough coins inserted... Returning reminder:"
			for c in sorted(self.__allowed, reverse=True):
				returned_coins[c] = self.__input.count(c)
		else:
			for c in sorted(self.__allowed, reverse=True):
				returned_coins[c] = int(100*reminder) / int(100*c)
				reminder = (int(100*reminder) % int(100*c)) / 100.0
			if reminder < 1e-4:
				print "\nThe ticket has been bought. Calculating reminder:"
			else:
				print "\nMachine couldn't return the reminder:"
		self.list_coins("Returning...", returned_coins)
		self.__remove_coins(returned_coins)
		del self.__input[:]

	def insert_coins(self):
		"""Interactively collects input from the user."""
		print "Insert a coin " + str(self.__allowed).strip("[]") + " (k - ends):"
		ch = raw_input('>>> ')
		while ch != 'k':
			if not float(ch) in self.__allowed:
				print "Put correct value."
				ch = raw_input('>>> ')
				continue
			self.__input.append(float(ch))	
			if sum(self.__input) >= self.__price:
				break	
			ch = raw_input('>>> ')
				
		self.__accept_coins(*self.__input)


	def __accept_coin(self, coin):
		"""Get single coin from the user."""
		if float(coin) in self.__allowed:
			self.__money[float(coin)] += 1
		else:
			print ">>> [ERROR] Use only following values: 0.05, 0.10, 0.20, 0.5, 1, 2, 5"


	def __accept_coins(self, *coins):
		"""Accepts multiple coins.
		Posible values: 0.05, 0.10, 0.20, 0.5, 1, 2, 5."""
		sum = 0.0
		for c in coins:
			self.__accept_coin(c)
			sum += c
		print "Inserted values ->",
		print str(coins).strip("()")


	def __remove_coins(self, dict_coins):
		"""Remove coins specified in dict_coins (holding coin values and quantities)""" 
		for c, n in dict_coins.iteritems():
			if n > 0:
				self.__money[c] -= n

	def pull_out_money(self):
		"""Pull out all the money from the machine."""
		print "\nTicket machine is holding:"
		self.list_coins("", self.__money)

		
	def list_coins(self, string, coin_dict, print_total=True):
		"""Prints coin values and quantities from coin_dict."""
		sum = 0.0
		for c in sorted(coin_dict, reverse=True):
			if coin_dict[c] > 0:
				print "%s %d x %.2f PLN" % (string, coin_dict[c], c)
				sum += coin_dict[c]*c
		print "Total: %.2f" % sum
