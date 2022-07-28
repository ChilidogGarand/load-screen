# load-screen
Dynamic generator for weird loading screen messages, inspired by [Zack Freedman](https://www.youtube.com/channel/UCUW49KGPezggFi0PGyDvcvg). Mostly using this as a function for future projects to have goofy fun loading messages.

# How It Works Right Now
Right now there are just 3 lists that it pulls from to construct a loading screen message:

* action_list
* object_property_list
* object_list

The main function ("loader") constructs load screen statements by pulling from the lists in the following way:

`$action_list $object_property_list $object_list`

So you get output like this at regular intervals (which are defined by the 'time.sleep' variable [default: 5 seconds] in the "loader" function):

```
Cracking tiny foray...
Exacerbating unrelated foray...
Upcycling resounding toughnut.dll...
Establishing emotional bond with un-fragged property...
Non-euclidifying pseudo-unknowable toughnut.dll...
Denying any knowledge of scrambled property...
Pseudo-decoding redacted toughnut.dll...
Re-detecting epsilon flowerchild...
Vibe-checking pseudo-smelly toughnut.dll...
Unlearning fuckwithable property...
Unvigorating un-fragged property...
Un-fragging reduced foray...
Denying proximity to duplicitous flowerchild...
Undetecting load API for toughnut.dll...
Certifying supercollated foray...
Bloating un-redacted load arguments...
Making amends with foolish foray...
Creating psuedo-strange property...
```

# Things I Want to Do
* Revamp lists to generate more dynamic load statements.
    * Will likely do this to include action prefixes, then trimming the action list down so the actions on it are prefixable.
* Adding loading ellipses or a spinner after each statement to better create the illusion that something silly is loading.
* May redefine some of the lists as dictionaries so that more complex statements can be constructed.
