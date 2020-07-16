#!/bin/bash
smbclient -N -c "put $1; ls" //192.168.70.130/share
