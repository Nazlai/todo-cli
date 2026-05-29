# CLI todo

## What it does

Stores todo items entered by user. User can update, delete retrieve items by id or view all stored items.

## Quick start

```
pip3 install -r requirements.txt
```

## Commands

- add: adds a todo to storage
- update: edits a todo's description in storage
- delete: removes a todo from storage
- mark_todo: changes a todo's status to <span style="color:darkturquoise">todo</span>
- mark_in_progress: changes a todo's status to <span style="color:darkturquoise">in progress</span>
- mark_done: changes a todo's status to <span style="color:darkturquoise">done</span>
- list(<span style="color:darkturquoise">status</span>): retrieves a list of todos, pass todo status to query todos by matching status
- get_by_id: retrieves a todo by id
