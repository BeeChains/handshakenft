# handshakenft
handshakenft/ 
 
# My Handshake NFT Project Developing 

all for http://block1.handshakenft.hns.to/

This is a basic example project that demonstrates how to create an NFT on the Handshake blockchain using the `nft-maker-cli` tool.

## Installation

1. Install Node.js and npm if you haven't already: https://nodejs.org/
2. Clone this repository: `git clone https://github.com/username/my-nft-project.git`
3. Navigate to the project directory: `cd my-nft-project`
4. Install dependencies: `npm install`

## Usage

1. Edit the `create-nft.sh` script to customize your NFT's properties.
2. Run the script to create your NFT: `./create-nft.sh`
3. Use the `inspect-nft.sh` script to view your NFT's details: `./inspect-nft.sh`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## install Handshake

To interact with the Handshake blockchain and create NFTs, you need to have a Handshake node running on your machine or use the Handshake JSON-RPC API. The nft-maker-cli tool used in the script interacts with the Handshake node to create and manage NFTs.

To install and run a Handshake node, you can follow the instructions in the official Handshake documentation: <a href="https://hsd-dev.org/hsd">HSD</a> or go to <a href="https://handshake.org/">Handshake.org</a> or do this;

# Linux

## Download the latest Handshake binary for Linux
wget https://github.com/handshake-org/hsd/releases/latest/download/hsd-linux-x64.tar.gz

## Extract the binary and move it to /usr/local/bin
tar -xzf hsd-linux-x64.tar.gz
sudo mv hsd-linux-x64/bin/hsd /usr/local/bin

## Clean up the downloaded files
rm -rf hsd-linux-x64*

# Windows

To install Handshake on Windows, you can use PowerShell to download and extract the latest Handshake binary:

## Download the latest Handshake binary for Windows
Invoke-WebRequest https://github.com/handshake-org/hsd/releases/latest/download/hsd-win-x64.zip -OutFile hsd-win-x64.zip

## Extract the binary and move it to C:\Program Files\Handshake
Expand-Archive hsd-win-x64.zip -DestinationPath "C:\Program Files\Handshake"

## Add the Handshake binary directory to the system PATH
$env:Path += ";C:\Program Files\Handshake"

## Clean up the downloaded files
Remove-Item hsd-win-x64.zip

# Windows Command Prompt instead of PowerShell

- Download the latest Handshake binary for Windows from the Handshake GitHub repository: [https://github.com/handshake-org/hsd/releases/latest](https://github.com/handshake-org/hsd/releases/latest)

- Extract the downloaded archive to a folder on your system, for example, C:\handshake

- Add the C:\handshake folder to your system PATH environment variable:
- Open the Start menu and search for "Environment Variables".
- Click on "Edit the system environment variables".
- Click on the "Environment Variables" button.
- Under "System Variables", scroll down and find the "Path" variable, then click on "Edit".
- Click on "New" and add the path to the C:\handshake folder.
- Click "OK" to close all the windows.
</ul>
Open a new Command Prompt window and run the hsd command to start the Handshake daemon.
That's it! You should now be able to use the Handshake command-line interface (CLI) in the Command Prompt by typing hsd-cli or use the hsd command to start the Handshake daemon.

Note that running Handshake on Windows may require administrative privileges or elevated command prompt access depending on your system configuration.

# Example of how you can create a simple web page using Flask and Python to register Handshake NFT subdomains:

## Installation

1. Install Python 3.9 or above: https://www.python.org/downloads/
2. Install Flask using the command ```pip install Flask```
3. Clone the repository: ```git clone https://github.com/BeeChains/handshakenft```

## Deployment

1. Create a HandshakeNFT subdomain on Namebase: https://www.namebase.io/domains
2. Create a TXT record for the subdomain with the metadata URL. If you're using Namebase, go to the DNS section for your subdomain and add a TXT record with the    following value: "txt=handshakenft/"
3. Replace the TODO placeholders in the app.py file with your own code.
4 Start the server by running the command python app.py
5.Access the application by opening a web browser and navigating to http://localhost:5000.

## Frontend Code
Using Flask for a frontend that allows users to buy and sell NFTs:
```
## Backend
python




