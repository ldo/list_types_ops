#+
# Run this script from within Blender, for example as follows:
#
#     blender -b -P list_types_ops.py
#
# to get a list of all the undocumented UI object classes which can
# be used for customizing the Blender user interface. These have names
# of the form category_class_name where “category” is an uppercase
# category of Blender functionality, “class” is a two-uppercase-letter
# code indicating the class of UI object, and “name” is the lowercase
# identifying name. The following values for “category” have been observed:
#
#     ACTION
#     ANIM
#     ARMATURE
#     BOID
#     BONE
#     BRUSH
#     BUTTONS
#     CAMERA
#     CLIP
#     CLOTH
#     CONSOLE
#     CONSTRAINT
#     CURVE
#     CYCLES
#     DATA
#     DOPESHEET
#     DPAINT
#     ED
#     FILEBROWSER
#     FILE
#     FLUID
#     FONT
#     GPENCIL
#     GRAPH
#     GROUP
#     IMAGE
#     INFO
#     LAMP
#     LATTICE
#     LOGIC
#     MARKER
#     MASK
#     MATERIAL
#     MBALL
#     MESH
#     NLA
#     NODE
#     OBJECT
#     OUTLINER
#     PAINTCURVE
#     PAINT
#     PALETTE
#     PARTICLE
#     PHYSICS
#     POSELIB
#     POSE
#     PROPERTIES
#     PTCACHE
#     RENDERLAYER
#     RENDER
#     RIGIDBODY
#     SCENE
#     SCREEN
#     SCRIPT
#     SCULPT
#     SEQUENCER
#     SKETCH
#     SOUND
#     SURFACE
#     TEXTURE
#     TEXT
#     TIME
#     TRANSFORM
#     UI
#     USERPREF
#     UV
#     VIEW2D
#     VIEW3D
#     WM
#     WORLD
#
# while the following values for “class” have been observed:
#
#     HT -- window header
#     MT -- menu
#     OT -- operator
#     PT -- panel
#
# Copyright 2011 by Lawrence D'Oliveiro <ldo@geek-central.gen.nz>.
# Licensed under CC-BY <http://creativecommons.org/licenses/by/4.0/>.
#-

import sys
import re
import bpy

name_groups = {}

for name in dir(bpy.types) :
    name_parts = re.search(r"^([A-Z0-9]+_[A-Z]T)_(\w+)$", name)
    if name_parts != None :
        # sys.stdout.write(name + "\n")
        prefix, rest = name_parts.groups()
        if prefix not in name_groups :
            name_groups[prefix] = set()
        #end if
        if rest in name_groups[prefix] :
            sys.stderr.write("duplicate name %s_%s\n" % (prefix, rest))
        #end if
        name_groups[prefix].add(rest)
    #end if
#end for

for prefix in sorted(name_groups) :
    sys.stdout.write(prefix + ": " + ", ".join(sorted(name_groups[prefix])) + "\n")
#end for
