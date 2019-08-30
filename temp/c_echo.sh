help_doc="\
\n
choose ascii color code expression from given first color argument
    only support font color change => front color
    color list =>
    r => red => \\\033[31m \033[31mfor test\033[m
    g => green => \\\033[32m \033[32mfor test\033[m
    y => yellow => \\\033[33m \033[33mfor test\033[m
    b => blue => \\\033[34m \033[34mfor test\033[m

    there are three support method to use
    1. only one argument => same as < echo -e >

    2. two arguments are given => output whole statement with given color code
    first => color code
    second => output statement

    3. more than two argument are given => output all grgument after statement with given color code others leave unchanged
    first argument => color code
    second argument => statement ready for output
    other arguments => ready to change into color font in statement

    example as\n
    => r \"'try catch python in this statement\" python this"

c_echo(){
    if test $# -gt 1
    then
        color_code=$1
        end_color_code="\\\033[m"

        ## start choose ascii color code
        if [ "$color_code" = "r" ]
        then
            color_code="\\\033[31m"
        elif [ "$color_code" = "g" ]
        then
            color_code="\\\033[32m"
        elif [ "$color_code" = "y" ]
        then
            color_code="\\\033[33m"
        elif [ "$color_code" = "b" ]
        then
            color_code="\\\033[34m"
        else
            echo -e "\033[31merror color code => \n     expected r/g/y/b => /red/green/yellow/blue => exit\033[m"
            exit
        fi
        ## replace origin pattern string around with color_code and end_color_code
        statement=$2

        if test $# -gt 2
        then
            for i in "${@:3}"
            do
                if [[ "$i" != "$color_code" && "$i" != "$statement" ]]
                then
                    statement=$(echo $statement | sed "s/$i/$color_code$i$end_color_code/g")
                fi
            done
            echo -e $statement
        else
            echo -e $(echo -e "$color_code$statement$end_color_code")
        fi
    elif test $# -eq 1
    then
        echo -e $1
    fi
}

help(){
    clear
    echo -e "$help_doc"

    c_echo r "\ndo not use some string contains < / > which will cause some error" "<" ">"
    c_echo "\tsuch as => ( y/n )\n"
}


if [ "$1" = "--help" ]
then
    help
fi
