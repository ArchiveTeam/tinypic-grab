#!/bin/bash

echo "Installing warcio"

if type pip3 > /dev/null 2>&1
then
  if ! sudo pip3 install warcio --upgrade
  then
    exit 1
  fi
fi

if ! sudo pip install warcio --upgrade
then
  exit 1
fi

exit 0

