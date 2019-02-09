
Jacob
-----
made compare.html to represent the output page where the comparison between codes will be displayed
i assume forms.html will be where the input from the user is gathered

tried my best to add columns for all the stats we will be tracking for each car, but i'm not very great at sql

began the framework we can use to compare cars. the specifications for this are as follows:

there is a ComparePackage class which has three members:
'owned' - the car the user owns of type Car
'theoretical' - the car the user chose to compare to of type Car
'diff' - a structure containing all of the differences between owned a theoretical of type Diff.

type diff is just a collection of data representing the differences between owned and theoretical

the idea is that compare.html can take this single object (a ComparePackage instance) and grab all of the data it needs to
display from that, instead of having to pass in 24 separate variables.
