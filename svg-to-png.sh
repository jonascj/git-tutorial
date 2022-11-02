#!/bin/sh
if [ $# -eq 0 ]; then
    echo "Usage: $0 {update|dryrun}"
    exit 1
elif [ $1 != "update" ] && [ $1 != "dryrun" ]; then
    echo "Usage: $0 {update|dryrun}"
    exit 1
fi



if [ $1 = "dryrun" ]; then
    echo "# # DRY RUN # #"
fi

for f in $(find -iname "*\.svg" | grep -v -e "venv" -e "png-embed-template.svg" -e "_build"); do

    file=$(dirname $f)/$(basename $f .svg)

    if [ -f $file.png ]; then
        pngtime=$(stat -c %Y $file.png)
    else
        pngtime=0
    fi
    svgtime=$(stat -c %Y $file.svg)

    if [ $pngtime -gt $svgtime ]; then
        echo Up to date: $file 
    else
	    echo Updated: $file 
        if [ $1 = "update" ]; then
            inkscape --export-png=$file.png $file.svg > /dev/null 2>&1
        fi
    fi
    
done
 

