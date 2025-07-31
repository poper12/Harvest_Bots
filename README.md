<p align="center">
  <img src="https://envs.sh/IZE.jpg" alt="logo" width="500" />
</p>

<h1 align="center">
 <b><a href="https://t.me/Manga_Campus" target="/blank"> File Sharing Bot </a></>
</h1>

<p align="center">🩵 Thanks for Being Here 🩵</p>

---

### CONFIGS VARIABLES

* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `FILE_AUTO_DELETE` File auto delete, value in seconds
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DB_URL` Your mongo db url
* `DB_NAME` Your mongo db session name
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `FORCE_SUB_CHANNEL2` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `REQ_SUB_CHANNEL3` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `REQ_SUB_CHANNEL4` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding

---

### EXTRA VARIABLES

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False
* `BOT_STATS_TEXT` put your custom text for stats command, use HTML
* `USER_REPLY_TEXT` put your text to show when user sends any message, use HTML

---

### FEATURES
- Fully customisable.
- Customisable welcome & Forcesub messages.
- More than one Posts in One Link.
- Can be deployed on heroku directly.
- Deploy to Koyeb + Heroku + Railway.
- Developer Service 24x7.

---

### SETUP

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub

---

### FILLINGS
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

---

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

---

#### CUSTOM_STATS

* `{uptime}` - Bot Uptime

---

### ALL COMMANDS

```
start - start the bot or get posts
batch - create link for more than one posts
genlink - create link for one post
users - view bot statistics
id - to get user id
broadcast - broadcast any messages to bot users
stats - checking your bot uptime
addadmin - <user id> add new admins  [Owner]
removeadmin - <user id> remove useless once [Owner]
listadmins - list all admins [Owner]
req_clear_1 - remove requests from db of request 1 channel [Owner]
req_clear_2 - remove requests from db of request 2 channel [Owner]
```

---

## 💡 Usage Guide

1. **Clone the repo**:

```bash
git clone https://github.com/ArihantSharma/FileStoreBot
cd FileStoreBot
bash start.sh
```

2. **Install requirements**:

```bash
pip install -r requirements.txt
```

3. **Edit your `config.py`** and `setup.json` as explained above.

4. **Run the bot**:

```bash
python3 main.py
```

You’re done!

---

## 🛒 Purchase Full Source

Want to use or resell this bot?

📩 **Contact [𝗔𝗮𝗿𝘂_𝟮𝟬𝟳𝟱](https://t.me/aaru_2075) on Telegram** to purchase the code or for support.

---

## 📜 License

This code is proprietary. You are not allowed to redistribute, resell, or publish it without explicit permission from the owner.

---

### ⭐ CONTACT DEVELOPER ⭐
- [Aaru](https://t.me/Aaru_2075)
