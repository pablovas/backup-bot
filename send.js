const TelegramBot = require('node-telegram-bot-api');
const fs = require('fs');
const config = require('./config');

const bot = new TelegramBot(config.botToken);

const zipFilesDir = config.homeDir;

fs.readdir(zipFilesDir, (err, files) => {
  if (err) {
    console.error(err);
    return;
  }

  const zipFiles = files.filter(file => file.endsWith('.zip'));

  zipFiles.forEach(zipFile => {
    const filePath = `${zipFilesDir}/${zipFile}`;
    bot.sendDocument(config.myID, filePath);
  });
});

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, `O ID do seu chat é: ${chatId}`);
});