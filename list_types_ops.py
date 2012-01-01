#+
# Run this script from within Blender, for example as follows:
#
#     blender -b -P list_types_ops.py
#
# to get a list of all the undocumented UI object classes which can
# be used for customizing the Blender user interface. A (slightly out-of-date)
# list of these can be found at
# <http://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Advanced_Tutorials/Python_Scripting/Object,_Action,_Settings_New>.
#
# Written 2011 December 20 by Lawrence D'Oliveiro <ldo@geek-central.gen.nz>.
#-

import sys
import re
import bpy

name_groups = {}

for name in dir(bpy.types) :
    name_parts = re.search(r"^([A-Z0-9]+_[A-Z]T)_(\w+)$", name)
    if name_parts  != None :
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
