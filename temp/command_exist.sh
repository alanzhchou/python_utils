help_doc="\
\n
    < command_exist  > 
        test if a command can execute in path,
        accetp only one argument => the command name

        return value allocate its status
        0 for true => command is on this machine
        1 for false => command not exist
"



command_exist(){
    if [ -x "$(command -v $1)" ]
    then
        return 0
    else
        return 1
    fi
}











help(){
    clear
    echo -e "$help_doc"

    # you can run some examples of your fucntion here
    # such as < ls >
    # ls -al
    command_exist python
    if_python=$?
    echo -e "\t\tcommand_exist python\n\t\tif exist it puts 0 else 1 => \n\t\t$if_python"
}


if [ "$1" = "--help" ]
then
    help
fi

