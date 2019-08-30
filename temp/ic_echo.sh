help_doc="\
\n
< ic_echo > module for inserted color code to echo => help with printing color font in console
    only support for four types color code inserted
    {{r }} => red => \\\033[31m => \033[31m for test \033[m
    {{g }} => green => \\\033[32m => \033[32m for test \033[m
    {{y }} => yellow => \\\033[33m => \033[33m for test \033[m
    {{b }} => blue => \\\033[34m => \033[34m for test \033[m

    use for ic_echo module just like < echo -e >
    in where you want display colorful font use < {{x my word here}} > expression to hint

    such as < {{r i want to be red}} > =>  \033[31mi want to be red\033[m

    in fact, this module just represent the < {{x }} > expression into ascii color code
"

ic_echo(){
    red_code="\\\033[31m"
    green_code="\\\033[32m"
    yellow_code="\\\033[33m"
    blue_code="\\\033[34m"
    end_color_code="\\\033[m"

    red_prefix="{{r"
    green_prefix="{{g"
    yellow_prefix="{{y"
    blue_prefix="{{b"

    suffix="}}"

    replace_suffix=$( echo $1 | sed "s/}}/$end_color_code/g" )
    replace_red=$( echo $replace_suffix | sed "s/{{r /$red_code/g"  )
    replace_green=$( echo $replace_red | sed "s/{{g /$green_code/g"  )
    replace_yellow=$( echo $replace_green | sed "s/{{y /$yellow_code/g"  )
    replace_blue=$( echo $replace_yellow | sed "s/{{b /$blue_code/g"  )
    echo -e $replace_blue
}






help(){
    clear
    echo -e "$help_doc"
    ic_echo "\t => try this with {{r red}} {{g green}} {{y yellow}} {{b blue}}\n"
}


if [ "$1" = "--help" ]
then
    help
fi

