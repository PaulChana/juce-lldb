#!/bin/bash

LLDB_INIT_FILE="$HOME/.lldbinit"
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )";
LLDB_JUCE_FILE="$SCRIPT_DIR/juce_lldb.py"
IMPORT_COMMAND="command script import $LLDB_JUCE_FILE"

function replace {
    echo "$IMPORT_COMMAND" > "$LLDB_INIT_FILE"
}

function append {
    echo "$IMPORT_COMMAND" >> "$LLDB_INIT_FILE"
}

function green {
    echo -e "\033[32m$1\033[0m" 
}

function cyan {
    echo -e "\033[1m\033[96m$1\033[0m"
}

function blue {
    echo -e "\033[1m\033[96m$1\033[0m"
}

if [[ -w "$LLDB_INIT_FILE"  ]] 
then     
    cyan "You already have an lldb init file"                              
    echo "Do you want to append (a) or replace (r) your current file?"
    echo "Press any other key to cancel..."
    read -r -n1 -s ANSWER
    case $ANSWER in
        [rR]) 
            replace
            green "Replaced"
            ;;
        [aA]) 
            append
            green "Appended"
            ;;
        *) 
            blue "No changes made to your system"
            exit 0 
            ;;
    esac
else
    green "Created lldb init file"
    replace
fi 

