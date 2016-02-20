# AoikReplace
A Sublime Text plugin to do regular expression replacement and toggling.

You can for example:
- Toggle between single quote (') and double quote (").
- Toggle between forward slash (/) and backslash (\\).

Tested working with:
- Sublime Text 2
- Sublime Text 3

## Table of Contents
- [Setup](#setup)
  - [Setup via git](#setup-via-git)
- [Usage](#usage)
  - [Run via Console Panel](#run-via-console-panel)
  - [Run via Shortcut](#run-via-shortcut)

## Setup

### Setup via git
Clone this repository to Sublime Text's **Packages** directory (Preferences - Browse Packages...):
```
git clone https://github.com/AoiKuiyuyou/AoikReplace-SublimeText AoikReplace
```

Make sure the repository directory is renamed to **AoikReplace**
(without the "-SublimeText" postfix), otherwise it may not work well.

## Usage

### Run via Console Panel
Open "View - Show Console (Ctrl+Shift+C)", run:
```
# Toggle between single quote (') and double quote (")
window.run_command("aoik_replace", { "mode": "toggle", "src": { "regex": "\"", "value": "\"" }, "dst": { "regex": "'", "value": "'" } })

# Toggle between forward slash (/) and backslash (\)
window.run_command("aoik_replace", { "mode": "toggle", "src": { "regex": "\\\\", "value": "\\\\" }, "dst": { "regex": "\\/", "value": "/" } })
```

### Run via Shortcut
Open "Preferences - Package Settings - AoikReplace - Default.sublime-keymap (Example)",
copy the content to your "Preferences - Key Bindings - User" file. Then:
- **Ctrl+Shift+'**: toggle between single quote (') and double quote (").
- **Ctrl+Shift+/**: toggle between forward slash (/) and backslash (\\).
