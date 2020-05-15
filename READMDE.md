## Infobot
A simple bot that provides an information menu and prompts users to select from the available menu option in order to provide more detailed information about the selected option.

> This bot has been generated using Floc Crisis Center.

## Setup
Make sure you have the latest version of Rasa and Docker.

Begin by training the bot:
```
rasa train
```

Run the duckling server that is used by Rasa to extract the "number" entity:
```
docker run -d --name ducking rasa/duckling -p 8000:8000
```

> Make sure to update config.yml if you want to use a different port for duckling

Next, start the action server:
```
rasa run actions
```

To test the bot, execute rasa's shell command:
```
rasa shell
```

### Read Rasa Docs
Check out [Rasa docs](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/) for more information regarding training and the various configuration options that are available to tweak and deploy the bot.