#!/bin/bash
echo "Start R Server"
rstudio-server start

echo "Adding User to Access R Server"
rstudio-server verify-installation

