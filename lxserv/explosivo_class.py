#!/usr/bin/env python
################################################################################
#
# explosivo_class.py
# Description: The class used for toggling a mesh morph from 100% to -100%
# Usage:
# Explosivo.toggle - toggles the explode map on the selected meshes
# Explosivo.toggle other_explode_morph_name - toggles the explode on the selected meshes
# but uses a custom named morph map
# Explosivo.delete removes the morphs on all meshes instead of toggling them
# Explosivo.delete other_explode_morph_name - removes morph on all meshes with special morph name
# Author: Chris Sprance Entrada Interactive
#
################################################################################

import lx
import lxifc
import lxu.command
import modo


class ExplosivoToggle(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.dyna_Add('explode_name', lx.symbol.sTYPE_STRING)
        self.basic_SetFlags(0, lx.symbol.fCMDARG_OPTIONAL)
        self.morph_name = str()
        self.selection = list()
        self.scene = modo.Scene()
        self.mesh = None
        self.explode_tag = 'EXPL'
        self.user_selection = list()

    def cmd_Flags(self):
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    def basic_Enable(self, msg):
        return True

    def cmd_Interact(self):
        pass

    def store_selection(self):
        '''
        Takes the user selection and stores all the selected
        meshes into a list for later use in self.selection
        '''
        self.user_selection = self.scene.selected
        self.selection = self.scene.selectedByType('mesh')

    def apply_morph(self):
        '''Applys a morph to a mesh at 100% named self.morph_name'''
        self.scene.select(self.mesh)
        lx.eval('vertMap.applyMorph %s 1.0' % self.morph_name)

    def remove_morph(self):
        '''applys a negative morph to the mesh which resets the mesh but keeps the morph'''
        self.scene.select(self.mesh)
        lx.eval('vertMap.applyMorph %s -1.0' % self.morph_name)

    def set_tag(self):
        '''sets the tag on a mesh to say that it is currently exploded'''
        self.mesh.setTag(self.explode_tag, 'True')

    def remove_tag(self):
        '''Removes any tags set on the mesh saying it is exploded'''
        # select the current mesh
        self.mesh.setTag(self.explode_tag, None)

    def is_exploded(self):
        '''Gets the tag on a mesh to see if it is currently exploded'''
        if self.mesh.hasTag(self.explode_tag):
            return True
        return False

    def basic_Execute(self, msg, flags):
        # If the morph name is set store it else just use the default
        self.morph_name = self.dyna_String(0, 'Explode')
        # store our selection filtering out only the mesh items
        self.store_selection()
        # loop through all the selected meshes
        for mesh in self.selection:
            # set current mesh in the loop
            self.mesh = mesh
            # if the mesh has no explode tag on it
            if not self.is_exploded():
                # apply the morph
                self.apply_morph()
                # set the tag exploded
                self.set_tag()
            # if the mesh does have an explode tag on it
            else:
                # remove the morph
                self.remove_morph()
                # remove the tag
                self.remove_tag()
        self.scene.deselect(None)
        for mesh in self.user_selection:
            self.scene.select(mesh, add=True)

    def cmd_Query(self, index, vaQuery):
        lx.notimpl()


class ExplosivoDelete(ExplosivoToggle):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        ExplosivoToggle.__init__(self)

    def basic_Execute(self, msg, flags):
        # If the morph name is set store it else just use the default
        self.morph_name = self.dyna_String(0, 'Explode')
        # store our selection filtering out only the mesh items
        self.store_selection()
        # loop through all the selected meshes
        for mesh in self.selection:
            self.mesh = mesh

            if self.is_exploded():
                self.remove_tag()
                self.remove_morph()
        self.scene.deselect(None)
        for mesh in self.user_selection:
            self.scene.select(mesh, add=True)


lx.bless(ExplosivoToggle, "Explosivo.toggle")
lx.bless(ExplosivoDelete, "Explosivo.delete")
