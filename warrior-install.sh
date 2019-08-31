#!/bin/sh -e


if ! sudo pip3 freeze | grep -q six
then
  echo "Installing six"
  if ! sudo pip3 install six
  then
    exit 1
  fi
fi
