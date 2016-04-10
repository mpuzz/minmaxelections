#!/bin/bash

tr "," ";" < $1 | sed "s/$/;/" > newfile
mv "newfile" $1
