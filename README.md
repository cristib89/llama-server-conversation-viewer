# llama-server-conversation-viewer
A simple conversation viewer for llama-server exports

<img width="526" height="275" alt="image" src="https://github.com/user-attachments/assets/b7dc86bc-c0dd-44bc-903d-f1f5435da538" />
<img width="526" height="275" alt="image" src="https://github.com/user-attachments/assets/43eea032-0db7-44b5-86a2-f6d8aac87039" />

## Contents

- [split.py](split.py) - splits the json array containing conversations from llama-server into individual conversations and the filename is generated based on the metadata from the conversation item as if it you would export a single conversation from llama-server

		usage:

		python split.py 2026-04-13_conversations.json 
		Generated: 2026-04-13_14-29-12_conv_2ea30759_run_a_query_on_the_a.json
		Generated: 2026-04-13_14-28-08_conv_7e3591a8_hello_test_123.json

- [viewer.html](viewer.html) - a static html file which relies on https://cdn.jsdelivr.net/npm/marked/marked.min.js to render markdown nicely

## Usage

- clone repo
- export conversation(s) from llama-server
- if needed, split the json array using the python script
- open the html file with a browser
- load exported conversation
- enjoy

## Features

- captures user/assistant turns and timestamps
- can show MCP tool calls
- can show reasoning blocks
- at the end of the session it will show statistics regarding that conversation
- copy button for code snippets

## Why

- maybe I don't want to start a llama-server to take a look at past conversations
- maybe I want to have a copy of conversations somewhere else outside of browser localstorage
- the json format might be hard to read with a text editor

## Online version

- https://cristib89.github.io/llama-server-conversation-viewer/viewer.html

## Disclaimers

- intended for local usage
- generated with AI
