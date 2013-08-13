# -*- coding: utf-8 -*-
#
# AWL simulator - instructions
#
# Copyright 2012-2013 Michael Buesch <m@bues.ch>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from awlsim.instructions.main import *


class AwlInsn_ZV(AwlInsn):
	def __init__(self, cpu, rawInsn):
		AwlInsn.__init__(self, cpu, AwlInsn.TYPE_ZV, rawInsn)
		self.assertOpCount(1)

	def staticSanityChecks(self):
		self.ops[0].assertType(AwlOperator.MEM_Z)

	def run(self):
		s = self.cpu.callStackTop.status
		self.cpu.getCounter(self.ops[0].resolve(True).value.byteOffset).run_ZV(s.VKE)
		s.OR, s.NER = 0, 0