# BronzerClient
Bronzer helps find vulnerabilities of Android apps. 
<br />
BronzerClient is written by Python and runs on a PC.

```
Usage: ACTION [OPTIONS] [COMPONENT]
ACTION:
    list:             list all packages
    set:              set packagename

    THE FOLLOWING ACTION NEED SET UP packagename FIRST
    attacksurface:    get an app's attack surface
    start:            start an activity
    startservice:     start a service
    stopservice:      stop a service
    broadcast:        send a broadcast
    exit:             exit Bronzer


OPTIONS:
    -D --debug:                  enable debug switch
    -a --action ACTION:          add an action
    -d --data-uri URI:           set a data-uri
    -c --category CATEGORY:      add a category
    -e --extra TYPE VALUE:       add an extra value
    --eb --extra-bool VALUE:      add an extra boolean value
    --ei --extra-int VALUE:       add an extra int value
    --el --extra-long VALUE:      add an extra long value
    --ef --extra-float VALUE:     add an extra float value
    --eu --extra-uri VALUE:       add an extra uri value
    --es --extra-string VALUE:    add an extra string value

COMPONENT:
    an android component name
```
