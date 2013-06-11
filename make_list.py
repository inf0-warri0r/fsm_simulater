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


class read_lt:
    def __init__(self):
        pass

    def list_bar_positions(self, st):
        s = list()
        br_c = 0
        for i in range(0, len(st)):
            if st[i] == '(' or st[i] == '[':
                br_c = br_c + 1
            if st[i] == '|':
                if br_c == 0:
                    s.append(i)

            if st[i] == ')' or st[i] == ']':
                br_c = br_c - 1

        return s

    def split_from_bar(self, st):
        p = self.list_bar_positions(st)
        s_ls = list()
        l = 0
        for i in range(0, len(p)):
            s = st[:p[i] - l]
            s_ls.append(('|', s))
            st = st[p[i] - l + 1:]
            l = p[i] + 1

        s_ls.append(('|', st))
        return s_ls

    def split_from_brac(self, st):
        br_c = 0
        st_list = list()
        s = ""
        bt = ''
        for i in range(0, len(st)):
            if st[i] == '(' or st[i] == '[':
                br_c = br_c + 1
                if br_c == 1 and s != "":
                    st_list.append((bt, s))
                    bt = st[i]
                    s = ""
                elif br_c == 1:
                    bt = st[i]
                elif br_c != 1:
                    s = s + st[i]

            elif st[i] == ')' or st[i] == ']':
                br_c = br_c - 1
                if br_c == 0:
                    st_list.append((bt, s))
                    s = ""
                    bt = ''
                else:
                    s = s + st[i]
            else:
                s = s + st[i]

        if s != "":
            st_list.append((bt, s))
        return st_list

    def check_bar(self, st):
        for i in st:
            if i == '(' or i == '[':
                return True
        return False

    def check_brac(self, st):
        for i in st:
            if i == '|':
                return True
        return False

    def sep(self, st_list, n, ls):
        if n >= len(st_list):
            return ls

        lt = self.tree_list(st_list[n])

        if type(lt) == list and len(lt) == 1:
            ls.append((st_list[n][0], lt[0]))
        else:
            ls.append((st_list[n][0], lt))
        return self.sep(st_list, n + 1, ls)

    def tree_list(self, st):
        if not self.check_bar(st[1]) and not self.check_brac(st[1]):
            return st
        p = self.split_from_bar(st[1])
        lst = list()
        for i in range(0, len(p)):
            if not self.check_bar(p[i][1]) and not self.check_brac(p[i][1]):
                lst.append(p[i])
            else:
                st_list = self.split_from_brac(p[i][1])
                lst.append(("|", self.sep(st_list, 0, [])))
        return lst
