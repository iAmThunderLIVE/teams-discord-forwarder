# Teams to Discord Forwarder Bot

A small Python service that listens for new messages in a Microsoft Teams channel (via Microsoft Graph) and forwards them into a Discord channel.

---

## Features

- Event-based forwarding using Microsoft Graph change notifications (no polling).
- Forwards message text, author name, and timestamp.
- Simple configuration via environment variables.
- Can use either a Discord bot or a Discord channel webhook as the destination.

---

## Prerequisites

- **Python** 3.10+ installed
- A **Discord server** where you can create a bot or channel webhook

---

## Getting Started

# Make sure you have python installed on your editor (If Visual Studio Code) then

```Link to get python 3.10.11 https://www.python.org/downloads/release/python-31011/ ```

 This is the version I'm using for the project, it doesn't have to be the exact same so long as it is greater than 3.10 and not less. 3.9 and under have some pretty major differences that may get in the way. 

# Make sure you also have git installed

```https://git-scm.com/install/windows```


# If you would like to use the coding editor I use

```https://code.visualstudio.com/```

### 1. Clone this repository

# Navigate to a newly created folder for the project then

``` Clone the project up in the top right via the green code button```
``` Then Https tab, copy the link```
``` git clone https://github.com/USERNAME/REPOSITORY.git```



### 2. Create a virtual environment in your preffered editor


 ```python -m venv .venv  ```

 # then if your terminal doesn't show (.venv)

 ```.\.venv\Scripts\Activate.ps1```



 ### 3. Install Dependencies 

 ```python -m pip install --upgrade pip```
```pip install discord.py```
```pip install python-dotenv```


### 4. Create a .env file for environment variables

 You will use your own generated keys for this file, though I will give you access to my sandbox discord for testing purposes. You will never have to use 'Production keys' during development. 

 Type in this file


```DC_API_KEY = ```

 then you will put in quotes here the API key for discord which I will give out or if someone wants to make their own testing environment here is a link to Discord on how to do that

```https://discord.com/developers/docs/quick-start/getting-started```

```https://discord.com/developers```