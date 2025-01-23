EASY-GREP
=========

A natural language to command line converter tool. Simply describe what you want to do, and easy-grep will generate and execute the appropriate command.

INSTALLATION
-----------

To install using Homebrew:
brew tap mohammadkazem-sadoughi/easy-grep
brew install easy-grep

USAGE
-----

First time setup:
The first time you run the tool, it will prompt you for your Anthropic API key.

Basic usage:
e-g ask [your natural language query]

Example:
e-g ask show me list of txt files containing 'hello'

The tool will:
1. Generate the appropriate command
2. Show you the command it plans to execute
3. Ask for your confirmation
4. Execute the command if you confirm

FEATURES
--------
- Convert natural language to command line commands
- Secure API key storage
- Command execution confirmation
- Easy installation via Homebrew

REQUIREMENTS
-----------
- Python 3.6 or higher
- Anthropic API key
- macOS (for Homebrew installation)

TROUBLESHOOTING
--------------
If you encounter permission issues:
1. Check if the API key is correctly stored in ~/.config/easy-grep/config.json
2. Ensure you have execution permissions for the installed command

For any issues or feature requests, please visit:
https://github.com/yourusername/easy-grep/issues

LICENSE
-------
MIT License
Copyright (c) 2024 Your Name
