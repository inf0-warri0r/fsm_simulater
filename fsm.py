"""
Author : tharindra galahena (inf0_warri0r)
Project: fsm simulater
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 03/06/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""


class fsm:
    def __init__(self, t_sym, nt_sym, ind):
        self.current_state = ind + str(0)
        self.states = {}
        self.table = {}
        self.current_string = ""
        self.end_states = list()
        self.start_states = [ind + '0']
        self.end_states = [ind + '1']
        self.current_string = ""
        self.copy_list = list()
        self.full_marg_list = list()
        self.add_list = list()

    def copy(self, to, frome):
        if self.table.get(to, 0) == 0:
            self.table[to] = {}
        for key in self.table[frome]:
            if self.table[frome][key] != to:
                self.table[to][key] = self.table[frome][key]

    def chain(self, st, end, ind, lst, a):
        current_state = st
        if len(lst) <= 1:
            next_state = end
        else:
            next_state = st + str(a)
        for l in range(0, len(lst)):
            if lst[l][0] == '|':
                if self.table.get(current_state, 0) == 0:
                    self.table[current_state] = {}
                if type(lst[l][1]) is not list:
                    self.table[current_state][lst[l][1]] = end
                else:
                    self.chain(current_state, end, ind, lst[l][1], a + 1)
                    a = a + 1
            elif lst[l][0] == '(' or lst[l][0] == '':

                if self.table.get(current_state, 0) == 0:
                    self.table[current_state] = {}
                if type(lst[l][1]) is not list:
                    if type(lst[l][1][1]) is not list:
                        if type(lst[l][1]) is tuple:
                            if lst[l][1][1] == '+':
                                if lst[0][1] is list:
                                    for x in lst[0][1]:
                                        self.table[current_state][x[1]] = self.table[st][x[1]]
                                    self.full_marg_list.append((end, current_state))
                                else:
                                    if lst[0][1][1] in self.table[st]:
                                        self.table[current_state][lst[0][1][1]] = self.table[st][lst[0][1][1]]
                                        self.full_marg_list.append((end, current_state))
                            else:
                                if l >= len(lst) - 1:
                                    if lst[l][1][1] not in self.table[current_state]:
                                        self.table[current_state][lst[l][1][1]] = end
                                    else:
                                        stat = self.table[current_state][lst[l][1][1]]
                                        #self.table[current_state][lst[l][1][1]] = end
                                        self.copy_list.append((stat, end))
                                else:
                                    #self.table[current_state][lst[l][1][1]] = next_state
                                    if lst[l][1][1] not in self.table[current_state]:
                                        self.table[current_state][lst[l][1][1]] = next_state
                                        #self.copy_list.append((stat, end))
                                        #current_state = next_state
                                    else:
                                        stat = self.table[current_state][lst[l][1][1]]
                                        #current_state = self.table[current_state][lst[l][1][1]]
                                        self.copy_list.append((stat, next_state))

                                a = a + 1
                                current_state = next_state
                                if l >= len(lst) - 2:
                                    next_state = end
                                else:
                                    next_state = current_state + "." + str(l)
                        else:
                            if lst[l][1] == '+':
                                self.table[current_state][lst[0][1]] = self.table[st][lst[0][1]]
                                self.full_marg_list.append((end, current_state))
                            else:
                                if lst[l][1] not in self.table[current_state]:
                                    self.table[current_state][lst[l][1]] = next_state
                                    current_state = next_state
                                else:
                                    stat = self.table[current_state][lst[l][1]]
                                    #current_state = self.table[current_state][lst[l][1]]
                                    self.copy_list.append((stat, next_state))
                                #current_state = next_state
                                if l >= len(lst) - 2:
                                    next_state = end
                                else:
                                    next_state = current_state + "." + str(l)
                    else:
                        if l >= len(lst) - 1:
                            self.chain(current_state, end, ind, lst[l][1][1], a + 1)
                        else:
                            self.chain(current_state, next_state, ind, lst[l][1][1], a + 1)
                        a = a + 1
                        current_state = next_state
                        if l >= len(lst) - 2:
                            next_state = end
                        else:
                            next_state = current_state + "." + str(l)
                else:
                    self.chain(current_state, next_state, ind, lst[l][1], a + 1)
                    a = a + 1
                    current_state = next_state
                    if l >= len(lst) - 2:
                        next_state = end
                    else:
                        next_state = current_state + "." + str(l)
            elif lst[l][0] == '[':
                if self.table.get(current_state, 0) == 0:
                    self.table[current_state] = {}
                if type(lst[l][1]) is not list:
                    #self.table[current_state][lst[l][1][1]] = next_state + str(a + 1)
                    #self.copy_list.append((next_state + str(a + 1), current_state))
                    #a = a + 1
                    if type(lst[l][1][1]) is not list:
                        if lst[l][1][1] in self.table[current_state]:
                            print current_state, " ", lst[l][1][1]
                            #self.table[current_state][lst[l][1][1]] = next_state + str(a + 1)
                            self.copy_list.append((self.table[current_state][lst[l][1][1]], current_state))
                        else:
                            self.table[current_state][lst[l][1][1]] = next_state + str(a + 1) + "-"
                            self.copy_list.append((next_state + str(a + 1) + "-", current_state))
                            a = a + 1
                    else:
                        self.chain(current_state, next_state + str(a + 1) + "-", ind, lst[l][1][1], a + 1)
                        self.copy_list.append((next_state + str(a + 1) + "-", current_state))
                        a = a + 1
                else:
                    self.chain(current_state, next_state + str(a + 1) + "-", ind, lst[l][1], a + 1)
                    self.copy_list.append((next_state + str(a + 1) + "-", current_state))
                    a = a + 1

    def chain2(self, st, end, ind, lst, a):
        self.start_states.append(st)
        self.end_states.append(end)
        self.chain(st, end, ind, lst, a)
        for l in self.copy_list:
            self.copy(l[0], l[1])
        for p in self.full_marg_list:
            self.full_marg(p)

    def full_marg(self, p):
        end, current_state = p
        if end in self.end_states:
            self.end_states.append(current_state)
        if self.table.get(current_state, 0) == 0:
            self.table[current_state] = {}
        if end in self.table:
            for key in self.table[end]:
                self.table[current_state][key] = self.table[end][key]

    def transfer(self, symbol):
        if self.current_state in self.table:
            if self.table[self.current_state].get(symbol, '') == '':
                return False
            else:
                self.current_state = self.table[self.current_state][symbol]
                self.current_string = self.current_string + symbol
                return True
        else:
            return False

    def duplicate(self, frm, to):
        print "aaa ", frm, " ", to
        if frm in self.table:
            if to not in self.table:
                self.table[to] = {}
            for key1 in self.table[frm]:
                if self.table[frm][key1] != to and self.table[frm][key1] != frm:
                    if key1 in self.table[to]:
                        if self.table[to][key1] != self.table[frm][key1]:
                            self.duplicate(self.table[to][key1], self.table[frm][key1])
                    self.table[to][key1] = self.table[frm][key1]
                elif self.table[frm][key1] == frm:
                    #self.table[to][key1] = to
                    if key1 in self.table[to]:
                        if self.table[to][key1] != to:
                            self.duplicate(self.table[to][key1], to)
                    self.table[to][key1] = to

    def join_fsm(self, fs, stat, action):
        end_states = fs.end_states
        end = self.table[stat][action]
        del self.table[stat][action]
        start_states = fs.start_states
        start = stat
        #print "---->", start, " ", end
        for key_s in fs.table.keys():
            for key_a in fs.table[key_s].keys():
                print key_s, " ", key_a, " ", fs.table[key_s][key_a]
                if key_s in end_states:
                    n_key_s = end
                elif key_s in start_states:
                    n_key_s = start
                else:
                    n_key_s = key_s
                print "== ", n_key_s, " ", key_a, " ", fs.table[key_s][key_a]
                if self.table.get(n_key_s, 0) == 0:
                    self.table[n_key_s] = {}
                    if fs.table[key_s][key_a] in end_states:
                        self.table[n_key_s][key_a] = end
                    else:
                        self.table[n_key_s][key_a] = fs.table[key_s][key_a]
                else:
                    if self.table[n_key_s].get(key_a, 0) != 0:
                        if self.table[n_key_s][key_a] in self.end_states:
                            print n_key_s, " *** ", key_a, " *** ", fs.table[key_s][key_a]
                            if fs.table[key_s][key_a] in end_states:
                                print n_key_s, " --- ", key_a, " ----- ", fs.table[key_s][key_a]
                                self.end_states.append(fs.table[key_s][key_a])
                                self.end_states = list(set(self.end_states))
                                self.table[n_key_s][key_a] = end
                            else:

                                st = self.table[n_key_s][key_a]
                                s2 = fs.table[key_s][key_a]
                                self.duplicate(s2, st)
                                print "xxxxxxxxxx ", n_key_s, " ", key_a, " ", self.table[n_key_s][key_a]
                                #self.end_states.append(fs.table[key_s][key_a])
                                #self.end_states = list(set(self.end_states))

                                if n_key_s[0] == st[0]:
                                    print "_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_> ", s2, " ", st
                                else:
                                    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=> ", s2, " ", st
                                    self.add_list.append((s2, st))
                                    if fs.table[key_s][key_a] in end_states:
                                        self.table[n_key_s][key_a] = end
                                    else:
                                        self.table[n_key_s][key_a] = fs.table[key_s][key_a]
                        else:
                            if self.table[n_key_s].get(key_a, 0) != fs.table[key_s][key_a]:
                                st = self.table[n_key_s][key_a]
                                #print n_key_s, " --- ", key_a
                                if fs.table[key_s][key_a] in end_states:
                                    self.duplicate(st, end)
                                else:
                                    s2 = fs.table[key_s][key_a]
                                    self.duplicate(st, s2)
                            if fs.table[key_s][key_a] in end_states:
                                self.table[n_key_s][key_a] = end
                            else:
                                self.table[n_key_s][key_a] = fs.table[key_s][key_a]
                    else:
                        if fs.table[key_s][key_a] in end_states:
                            self.table[n_key_s][key_a] = end
                        else:
                            self.table[n_key_s][key_a] = fs.table[key_s][key_a]

    def join(self, fs, action):

        st_list = list()
        for key_s in self.table:
            for key_a in self.table[key_s]:
                if key_a == action:
                    st_list.append(key_s)
                    break

        for key_s in st_list:
            self.join_fsm(fs, key_s, action)

    def add(self):
        print self.add_list
        for p in self.add_list:
            frm, to = p
            if to in self.end_states:
                self.end_states.append(frm)

    def map_states(self):
        c = 0
        for s in sorted(self.table.keys()):
            if self.states.get(s, "") == "":
                self.states[s] = "q" + str(c)
                c = c + 1

        for s in self.end_states:
            if self.states.get(s, "") == "":
                self.states[s] = "q" + str(c)
                c = c + 1

    def reset(self):
        self.current_state = self.start_states[0]
