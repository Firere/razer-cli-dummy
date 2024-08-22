#!/usr/bin/bash

if [ -f "/usr/bin/razer-cli" ]; then
	echo "/usr/bin/razer-cli already exists. Renaming to /usr/bin/razer-cli.bak."
	mv /usr/bin/razer-cli /usr/bin/razer-cli.bak
fi

# I have no idea how to work with Bash. Thanks StackOverflow
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR

sudo /usr/bin/bash << EOF
cp main.py /usr/bin/razer-cli
chmod +x /usr/bin/razer-cli
EOF