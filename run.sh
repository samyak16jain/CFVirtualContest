#!/bin/bash

function launch(){
    cd
    cd Desktop/TestProjects/CFcontest
    python test.py $1
    python web.py 
    cd
    subl D.cpp
    subl C.cpp
    subl B.cpp
    subl A.cpp
}