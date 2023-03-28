#!/bin/bash

tail -n +2 ./data/Buzzard2015_data.csv |cut -d "," -f 3| sort|uniq -c|sort -r > utn3.txt

