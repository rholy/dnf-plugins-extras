# coffee.py
# DNF plugin adding some fun.
#
# Copyright (C) 2015 Igor Gnatenko
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#

from __future__ import absolute_import
from __future__ import unicode_literals

import dnf


COFFEE = r"""
        (((((
        )))))
    _____________
   |             | _
   |             |/ |
   |             |  |
   |             |_/
   |_           _|
     \___DNF___/
"""

HOTDOG = r"""
               .---. __
    ,         /     \   \    ||||
   \\\\      |O___O |    | \\||||
   \   //    | \_/  |    |  \   /
    '--/----/|     /     |   |-'
           // //  /     -----'
          //  \\ /      /
         //  // /      /
        //  \\ /      /
       //  // /      /
      /|   ' /      /
      //\___/      /
     //   ||\     /
     \\_  || '---'
     /' /  \\_.-
    /  /    --| |
    '-'      |  |
              '-'
"""


class Coffee(dnf.Plugin):

    name = "coffee"

    def __init__(self, base, cli):
        super(Coffee, self).__init__(base, cli)
        self.base = base

    def config(self):
        print(COFFEE)

    def transaction(self):
        print(HOTDOG)
