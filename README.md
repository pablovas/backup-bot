# backup-bot
Personal script to backup files using a Telegram Bot.

# Instructions
To this script works you need to create a `config.js` file, like the following example:

``` JavaScript
module.exports = {
  botToken: 'YOUR_BOT_TOKEN',
  myID: 'YOUR_CHAT_ID',
  homeDir: '/home/YOUR_USER/',
};
```
With the config file, now you can run this project typing `sh start.sh` in the terminal.
