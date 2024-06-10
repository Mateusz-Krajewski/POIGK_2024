description: |
    API documentation for modules: POIGK_2024, POIGK_2024.Game, POIGK_2024.Generator, POIGK_2024.Move, POIGK_2024.Pomel, POIGK_2024.docs, POIGK_2024.docs.conf, POIGK_2024.main, POIGK_2024.resources, POIGK_2024.resources.gcodeparser, POIGK_2024.tests, POIGK_2024.tests.test_try.

lang: en

classoption: oneside
geometry: margin=1in
papersize: a4

linkcolor: blue
links-as-notes: true
...



# Namespace `POIGK_2024` {#id}





## Sub-modules

* [POIGK_2024.Game](#POIGK_2024.Game)
* [POIGK_2024.Generator](#POIGK_2024.Generator)
* [POIGK_2024.Move](#POIGK_2024.Move)
* [POIGK_2024.Pomel](#POIGK_2024.Pomel)
* [POIGK_2024.docs](#POIGK_2024.docs)
* [POIGK_2024.main](#POIGK_2024.main)
* [POIGK_2024.resources](#POIGK_2024.resources)
* [POIGK_2024.tests](#POIGK_2024.tests)







# Module `POIGK_2024.Game` {#id}








## Classes



### Class `Game` {#id}




>     class Game(
>         slower,
>         YOFFSET,
>         XZOFFSET
>     )


Main class Of the game, they initialize all of Entities


Args
-----=
**```do```** :&ensp;<code>list\[Move]</code>
:   list of moves to get by Pomel class


**```slower```** :&ensp;<code>int</code>
:   multiply quantity of elements in printing part










#### Methods



##### Method `Cursor` {#id}




>     def Cursor(
>         self
>     )


Enable / Disable Cursor


##### Method `menu` {#id}




>     def menu(
>         self
>     )


function Wchich is responsible for generate menu view


##### Method `start_gen_cube` {#id}




>     def start_gen_cube(
>         self
>     )


Function responsible for disable menu, and start generating cube


##### Method `start_gen_sphere` {#id}




>     def start_gen_sphere(
>         self
>     )


Funcrion responsible for disable menu, and start generating Sphere




# Module `POIGK_2024.Generator` {#id}








## Classes



### Class `Generator` {#id}




>     class Generator(
>         slower,
>         YOFFSET,
>         XZOFFSET
>     )


Generator Objects Ready to print by 3D Priner








#### Methods



##### Method `GenerateCube` {#id}




>     def GenerateCube(
>         self,
>         a
>     ) ‑> list[Move.Move]


Function generates Moves to create Cube


Args
-----=
**```a```** :&ensp;<code>int</code>
:   size of Cube



Returns
-----=
<code>list\[Move]</code>
:   moves list




##### Method `GenerateSphere` {#id}




>     def GenerateSphere(
>         self,
>         radius: float,
>         num_layers: int,
>         num_points_per_layer: int
>     ) ‑> list[Move.Move]


Function to generate Moves list to create a Sphare


Args
-----=
**```radius```** :&ensp;<code>float</code>
:   radius of sphere


**```num_layers```** :&ensp;<code>int</code>
:   nomber of layers in Y


**```num_points_per_layer```** :&ensp;<code>int</code>
:   num of points in layer XZ



Returns
-----=
<code>list\[Move]</code>
:   moves list






# Module `POIGK_2024.Move` {#id}








## Classes



### Class `Move` {#id}




>     class Move(
>         position=(0, 0, 0),
>         only_move=False
>     )


Represents a move in GCode.

Initialize Move with position and only_move flag.








#### Methods



##### Method `change_x` {#id}




>     def change_x(
>         self,
>         delta_x
>     )


Change the X coordinate by delta_x.


##### Method `change_y` {#id}




>     def change_y(
>         self,
>         delta_y
>     )


Change the Y coordinate by delta_y.


##### Method `change_z` {#id}




>     def change_z(
>         self,
>         delta_z
>     )


Change the Z coordinate by delta_z.


##### Method `get_position` {#id}




>     def get_position(
>         self
>     )


Get the current position as a tuple.




# Module `POIGK_2024.Pomel` {#id}








## Classes



### Class `Pomel` {#id}




>     class Pomel(
>         do: list[Move.Move],
>         slower,
>         **kwargs
>     )


Pomel class is responsible for Move Pomel Model and Generate printing efect


Args
-----=
**```do```**
:   (list[Move]): moves lists


**```slower```**
:   (int): change print resolution





#### Ancestors (in MRO)

* [ursina.entity.Entity](#ursina.entity.Entity)
* [panda3d.core.NodePath](#panda3d.core.NodePath)
* [dtoolconfig.DTOOL_SUPER_BASE](#dtoolconfig.DTOOL_SUPER_BASE)







#### Methods



##### Method `ChangePause` {#id}




>     def ChangePause(
>         self
>     )


change pause state


##### Method `dropEntity` {#id}




>     def dropEntity(
>         self
>     )


Delete printed items func


##### Method `enableEntity` {#id}




>     def enableEntity(
>         self
>     )


Enable printed items


##### Method `update` {#id}




>     def update(
>         self
>     )


Function called by ursina engine. They change position of Pomel and print Cube




# Namespace `POIGK_2024.docs` {#id}





## Sub-modules

* [POIGK_2024.docs.conf](#POIGK_2024.docs.conf)







# Module `POIGK_2024.docs.conf` {#id}










# Module `POIGK_2024.main` {#id}








## Classes



### Class `Main` {#id}




>     class Main













# Namespace `POIGK_2024.resources` {#id}





## Sub-modules

* [POIGK_2024.resources.gcodeparser](#POIGK_2024.resources.gcodeparser)







# Module `POIGK_2024.resources.gcodeparser` {#id}

GCode parser module.






## Classes



### Class `GCodeParser` {#id}




>     class GCodeParser


Parser for GCode files.

Initialize the GCodeParser.








#### Methods



##### Method `convert_gcode_to_list` {#id}




>     def convert_gcode_to_list(
>         self,
>         gcode_list
>     )


Convert GCode to a list of Move objects.


##### Method `filter_lines` {#id}




>     def filter_lines(
>         self,
>         lines: list[str]
>     ) ‑> list[str]


Return filtered lines that start with G.


Args
-----=
**```lines```** :&ensp;<code>list\[str]</code>
:   Lines read from a file.



Returns
-----=
<code>list\[str]</code>
:   Filtered lines.




##### Method `filter_v2` {#id}




>     def filter_v2(
>         self,
>         lines: list[str]
>     )


Further filter lines by removing lines ending with F.


##### Method `get_filtered_lines` {#id}




>     def get_filtered_lines(
>         self
>     )


Get filtered lines from a GCode file.


##### Method `read_file_lines` {#id}




>     def read_file_lines(
>         self
>     ) ‑> list[str]


Read lines from a GCode file.


##### Method `save_lines` {#id}




>     def save_lines(
>         self,
>         lines: list[str]
>     )


Save lines to a GCode file.




# Namespace `POIGK_2024.tests` {#id}





## Sub-modules

* [POIGK_2024.tests.test_try](#POIGK_2024.tests.test_try)







# Module `POIGK_2024.tests.test_try` {#id}








## Classes



### Class `TestClass` {#id}




>     class TestClass(
>         methodName='runTest'
>     )


A class whose instances are single test cases.

By default, the test code itself should be placed in a method named
'runTest'.

If the fixture may be used for many test cases, create as
many test methods as are needed. When instantiating such a TestCase
subclass, specify in the constructor arguments the name of the test method
that the instance is to execute.

Test authors should subclass TestCase for their own tests. Construction
and deconstruction of the test's environment ('fixture') can be
implemented by overriding the 'setUp' and 'tearDown' methods respectively.

If it is necessary to override the __init__ method, the base class
__init__ method must always be called. It is important that subclasses
should not change the signature of their __init__ method, since instances
of the classes are instantiated automatically by parts of the framework
in order to be run.

When subclassing TestCase, you can set these attributes:
* failureException: determines which exception will be raised when
    the instance's assertion methods fail; test methods raising this
    exception will be deemed to have 'failed' rather than 'errored'.
* longMessage: determines whether long messages (including repr of
    objects used in assert methods) will be printed on failure in *addition*
    to any explicit message passed.
* maxDiff: sets the maximum length of a diff in failure messages
    by assert methods using difflib. It is looked up as an instance
    attribute so can be configured by individual tests if required.

Create an instance of the class that will use the named test
method when executed. Raises a ValueError if the instance does
not have a method with the specified name.



#### Ancestors (in MRO)

* [unittest.case.TestCase](#unittest.case.TestCase)







#### Methods



##### Method `test_is_none` {#id}




>     def test_is_none(
>         self
>     )