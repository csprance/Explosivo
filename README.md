# Explosivo!!
A modo kit by @csprance to toggle morphs on and off for baking things wth Explode morph maps.

## Installation
This is a modo kit so install it like normal. I've only tested this on Modo 10, but I don't think it's doing anything
fancy. Let me know if you run into any issues and if it works on other versions of modo!
* Extract into `%appdata%/Luxology/Kits`
* Restart modo

## How to use
* `Click` the little Explodey icon on and off to toggle the morph
* `Ctrl Click` the Explodey icon to reset all selected meshes to unexploded
* `Alt + Click` the Explodey icon to set the explode map name (Defaults to Explode)

## Whats going on
The actual command being fired is either `Explosivo.toggle` or `Explosivo.toggle other_morph_to_toggle` firing this
command with any meshes or none (which means all) selected will apply a morph to the mesh and set a tag on the mesh
 indicated that the mesh is currently exploded. This way you can toggle explodes per mesh or all at once.

## Uninstallation process
* Delete `csprance_explosivo` from `%appdata%/Luxology/Kits`

## Credits
* Chris Sprance - All the Things
* Thanks to the guys in the modo Developers Channel. Super friendly bunch of dudes helped me a lot.

