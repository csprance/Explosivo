#!/usr/bin/env python
################################################################################
#
# explosivo_class.py
# Description: The class used for toggling a mesh morph from 100% to -100%
# Usage:
# Explosivo.toggle - toggles the explode map on the selected meshes
# Explosivo.toggle other_explode_morph_name - toggles the explode on the selected meshes
# but uses a custom named morph map
# (if nothing selected everything is selected)
# Author: Chris Sprance Entrada Interactive
#
################################################################################

import lx
import lxifc
import lxu.command


class ExplosivoToggle(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.dyna_Add('explode_name', lx.symbol.sTYPE_STRING)
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)
        self.morph_name = str()

    def cmd_Flags(self):
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    def basic_Enable(self, msg):
        return True

    def cmd_Interact(self):
        pass

    def basic_Execute(self, msg, flags):
        self.morph_name = self.dyna_String(0, 'Explode')
        lx.out(self.morph_name)

    def cmd_Query(self, index, vaQuery):
        lx.notimpl()


lx.bless(ExplosivoToggle, "Explosivo.toggle")
