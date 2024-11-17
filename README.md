# leosync
Leosync is a script to sync all your projects between your devices using a Git repo

# How to configure
```js
.
├── leosync.py
└── projects // where your projects are going to be stored
```
```py
# leosync.py
class config:
    REPO = '' # your Git repository url
    PATH = '' # your projects path (AKA where your github repo will be located), example: /home/leo/projects/
```
### On VScode
Open the command palette type: `Tasks: Open Use Tasks` and hit Enter.
```json
// tasks.json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Sync Project",
            "type": "shell",
            "command": "python3 <PATH-TO-LEOSYNC> sync"
        }
    ]
}
```

# How to use
## On VScode
Open the command palette and type `Tasks: Run Task` and select `Sync Project`