# Explosivo!!
A modo kit by @csprance to toggle morphs on and off for baking things wth Explode morph maps.

## Installation
This is a modo kit so install it like normal. I've only tested this on Modo 10, but I don't think it's doing anything
fancy. Let me know if you run into any issues and if it works on other versions of modo!
* Extract/Clone into `%appdata%/Luxology/Kits`
* Restart modo

## How to use
* `Click` the Explosivo button to toggle the morph
* `Alt + Click` the Explosivo button to reset all selected meshes to unexploded

## Video Guide

[![Click For Video](http://www.csprance.com/shots/2016-05-09_23-14-51a6ce51b8-e066-4c36-a16d-ab4189e182d5.png)](https://youtu.be/rXcz94eqZy4 "Video Guide")
## Whats going on
The actual command being fired is either `Explosivo.toggle` or `Explosivo.toggle other_morph_to_toggle` firing this
command with meshes selected will apply a previously defined morph to the mesh and set a tag on the mesh
indicating that the mesh is currently exploded. This way you can toggle explodes per mesh or all at once.

The other command that gets run is `Explosivo.delete` or `Explosivo.delete other_morph_to_toggle` which will remove any
applied morph maps from any selected meshes instead of toggling them. This is handy if you have some toggled on and some
off you can quickly get them all to off and then on again.

## Uninstallation process
* Delete `csprance_explosivo` from `%appdata%/Luxology/Kits`

## Credits
* Chris Sprance - All the Things
* Thanks to the guys in the modo Developers Channel. Super friendly bunch of dudes helped me a lot.

