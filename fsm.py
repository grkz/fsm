#!/usr/bin/env python

from ctl import State

# Ticket machine settings:
state_dict = {'get_ready': 0, 'user_input': 1, 'empty': 2, 'broken': -1}
initial_coins_set = [2,2,5,1,0.5,0.1,0.1,5,5,1,1,1,0.50, 0.5, 0.200]
ticket_price = 3.3

fsm = State(state_dict, initial_coins_set, ticket_price)

fsm.get_state()
fsm.set_state('get_ready')
fsm.get_state()
fsm.set_state('user_input')
fsm.get_state()
fsm.set_state('empty')
fsm.get_state()
fsm.set_state('randomstate')
fsm.get_state()
