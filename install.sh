#!/bin/bash

LLDB_INIT_FILE="$HOME/.lldbinit"
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )";
IMPORT_COMMAND="command script import"

declare -a IMPORT_FILES=("juce_colour"
                         "juce_component" 
                         "juce_lldb"
                         "juce_memory"
                         "juce_result"
                         "juce_stringarray"
                         "juce_stringpairarray"
                         "juce_time"
                         "juce_url" 
                         "juce_uuid"
                         "juce_var")

function write {
    for IMPORT_FILE in "${IMPORT_FILES[@]}"
    do
        echo "$IMPORT_COMMAND $SCRIPT_DIR/$IMPORT_FILE.py" >> "$LLDB_INIT_FILE"
    done
}

function replace {
    rm "$LLDB_INIT_FILE"
    write
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
            write
            green "Appended"
            ;;
        *) 
            blue "No changes made to your system"
            exit 0 
            ;;
    esac
else
    green "Created lldb init file"
    write
fi 

