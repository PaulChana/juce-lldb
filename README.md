# juce-lldb

LLDB scripts to make juce objects nicer in the debugger

## Installation

Run `./install.sh` and follow the prompts to install the script globally

## Standards

* Code is formatted using [Black](https://pypi.org/project/black/) - [See here for setup details](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0)
* Editor of choice is [VSCode](https://code.visualstudio.com)
* Terminal is zsh

## Organisation

The code is simply divided up by class that is supported. To extend the support, create a file named `juce_XYZ` where `XYZ` is the name of the juce class that you are adding support for. Then add this filename to `install.sh` (Look for `IMPORT_FILES` and it should be clear).

## Testing

There is a cmake based project located in `tests`. If you run this you can directly see each of the items in lldb itself

## Contributions

Happy to see contributions, just open a PR in the usual way.

## Credits

I have to credit the work of [Jim Credlands lldb scripts](https://github.com/jcredland/juce-toys/blob/master/juce_lldb_xcode.py) and [Sudaras blog](https://melatonin.dev/blog/how-to-create-lldb-type-summaries-and-synthetic-children-for-your-custom-types/) both of which were immensely helpful. Any mistakes here are my own tho ;)
