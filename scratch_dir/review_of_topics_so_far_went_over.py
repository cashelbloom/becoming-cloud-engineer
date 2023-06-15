'''
1. Built-in Functions
2. Writing Custom Functions
    a. Functions without any parameters
    b. Functions with parameters
        1. positional parameters
        2. keyword parameters
            with default values
            can be optional
            if a value is provided to a keyword param, then the default value is overwritten
        3.
    c. Function ending
        Functions can end RETURNING one or more values
        Functions that don't return any value; however they can be of four types:
            1. pass
            2. exit
            3. without the keyword return
            4. with the keyword return
    .
3. Variable:
    Memory location with a humanly-readable label.
    A variable's value can change during the execution of the program
    A variable's life-time (SCOPE) depends on the exact location of its declaration with in a module
        a variable can be declared at
            the module level
            the function level
            the block level

    If a variable is declared at a higher level (at the module level) and needs to be used at a lower level
    (such as function or block) then at the lower level the variable needs to be preceeded by the keyword "global"

4. CONSTANT:
     Memory location with a humanly-readable label.
    A CONSTANT's value IS NOT EXPECTED to change during the execution of the program
    Normally, CONSTANTS are declared at the very top of the module or even in a separate file

5. Conditional Branching:
    It is when the execution route is chosen during the execution time
        Implementation in Python is thru:
            if
            elif
            else
            match .. case (alse case _: is when none of the previous cases matched with incoming value)
6. Loops:
    1. for loop - the number of times the for loop is going to be executing is KNOWN at the beginning of the loop
        for loop need not execute even once
            because the referenced variable (which should be iterable) for the count might have value 0 too.
    2. while loop- number of times the while loop is going to be executing is NOT KNOWN at the beginning of the loop
        while loop executes at least once

7. File Handling:
    It refers to working with files in the storage location
    The default mode for opening a file is 'r'
    If we use 'w', it means we intend to open an empty file for writing
        creates the named file if it is NOT existing in the specified location
        if the file exists in the specified location, then the contents of the file is overwritten when the file opened
    if we want to open a file for reading and writing, then we need to specify 'r+'
'''