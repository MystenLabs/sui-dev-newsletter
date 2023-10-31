#!/bin/bash
#gh pr list --repo mystenlabs/sui -L 5000 --state merged --search merged:$1..$2 --json title --json url | jq -r '.[] | "* [" + .title + "]" + "(" + .url + ")" ' | sort
gh search prs --repo=mystenlabs/sui -L 1000 --merged --merged-at $1..$2 --json title --json url | jq -r '.[] | "* [" + .title + "]" + "(" + .url + ")" ' | sort
