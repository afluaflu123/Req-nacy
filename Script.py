class script(object):
    START_TXT = """<b>{} {},

Mʏ Nᴀᴍᴇ Is {} {}, Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ I Wɪʟʟ Gɪᴠᴇ Mᴏᴠɪᴇs Oʀ Sᴇʀɪᴇs Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Pᴍ.</b>"""   

    SHJ_TXT = """<b>{} {},

Mʏ Nᴀᴍᴇ Is {} {}, Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ I Wɪʟʟ Gɪᴠᴇ Mᴏᴠɪᴇs Oʀ Sᴇʀɪᴇs Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Pᴍ.</b>"""   

    HELP_TXT = """<b>Hᴇʏ {} Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.</b>"""

    HELPER_TXT = """<b>Hᴇʏ {} Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.</b>"""
    
    ABOUT_TXT = """<b>◆ Mʏ Nᴀᴍᴇ : <a href='https://t.me/Oru_adaar_Robot'>♡ Nᴀɴᴄʏ ᵛ³·⁰</a>
◆ Dᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Hacker_Jr'>HᴀᴄKᴇʀ Jʀ 〆⁪⁬⁮⁮⁮</a>
◆ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʀᴏɢʀᴀᴍ</a>
◆ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>Pʏᴛʜᴏɴ 3</a>
◆ Dᴀᴛᴀ Bᴀsᴇ: <a href='https://cloud.mongodb.com/'>Mᴏɴɢᴏ Dʙ</a>
◆ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='tg://need_update_for_some_feature'>Aɴʏᴡʜᴇʀᴇ</a>
◆ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.7.1 [ Sᴛᴀʙʟᴇ ]</b>"""

    SOURCE_TXT = """<b>
◆ <u>Tʜɪꜱ Bᴏᴛ Iꜱ Nᴏᴛ Aɴ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ.</u>

◆ Bᴏᴛ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ ~ <sp>Private 😜</sp> 

◆ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : <a href='https://github.com/Joelkb/DQ-The-File-Donor'>Cʟɪᴄᴋ Hᴇʀᴇ</a></b>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

<b>- 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚆𝙴𝚁𝙴 𝚄𝚂𝙴𝚁𝚂 𝙲𝙰𝙽 𝚂𝙴𝚃 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝙸𝙴𝚂 𝙵𝙾𝚁 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙰𝙽𝙳 𝙴𝙻𝚂𝙰 𝚆𝙸𝙻𝙻 𝚁𝙴𝚂𝙿𝙾𝙽𝙳 𝚆𝙷𝙴𝙽𝙴𝚅𝙴𝚁 𝙰 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙸𝚂 𝙵𝙾𝚄𝙽𝙳 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴</b>

<b>NOTE:</b>
<b>𝟷.𝚂𝙷𝙾𝚄𝙻𝙳 𝙷𝙰𝚅𝙴 𝙰𝙳𝙼𝙸𝙽 𝙿𝚁𝙸𝚅𝙸𝙻𝙻𝙰𝙶𝙴.
𝟸. 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃.
𝟹. 𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙷𝙰𝚅𝙴 𝙰 𝙻𝙸𝙼𝙸𝚃 𝙾𝙵 𝟼𝟺 𝙲𝙷𝙰𝚁𝙰𝙲𝚃𝙴𝚁𝚂.</b>

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

<b>𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝙾𝚃𝙷 𝚄𝚁𝙻 𝙰𝙽𝙳 𝙰𝙻𝙴𝚁𝚃 𝙸𝙽𝙻𝙸𝙽𝙴 𝙱𝚄𝚃𝚃𝙾𝙽𝚂.</b>
<b>NOTE:</b>
<b>𝟷. 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙰𝙻𝙻𝙾𝚆𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙰𝙽𝚈 𝙲𝙾𝙽𝚃𝙴𝙽𝚃, 𝚂𝙾 𝙲𝙾𝙽𝚃𝙴𝙽𝚃 𝙸𝚂 𝙼𝙰𝙽𝙳𝙰𝚃𝙾𝚁𝚈.
𝟸. 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙼𝙴𝙳𝙸𝙰 𝚃𝚈𝙿𝙴.
𝟹. 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚂𝙷𝙾𝚄𝙻𝙳 𝙱𝙴 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈 𝙿𝙰𝚁𝚂𝙴𝙳 𝙰𝚂 𝙼𝙰𝚁𝙺𝙳𝙾𝚆𝙽 𝙵𝙾𝚁𝙼𝙰𝚃</b>
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Example...)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """<b><u>AUTO FILTER NOTE:-</u></b>

• ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
• ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇs.
• ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇs. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<u>ADMIN ONLY THIS COMMANDS</u>

<b>★ /set_template - 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙵𝙾𝚁 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>★ /get_template - 𝙶𝙴𝚃 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙾𝙵 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>★ /autofilter on - 𝙴𝙽𝙰𝙱𝙻𝙴 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>
<b>★ /autofilter off - 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>"""

    CONNECTION_TXT = """<b><u>CONNECTIONS NOTE:-</u></b>

1. ONLY ADMINS CAN ADD A CONNECTION.
2. SEND <code>/connect</code> FOR CONNECTING ME TO UR PM

<b><u>COMMANDS AND USAGE:-</u></b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Elsa

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """<b><u>ADMIN MODS COMMANDS</u></b>

• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /bcspeed - <code>to speed broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a message to all groups</code>
• /gfilter - <code>To add global filter</code>
• /gfilters - <code>To view global filters</code>
• /delallg - <code>To delete all global filters from database</code>
• /delg - <code>To delete a specific global filter</code>
• /setskip - <code>Skip no of files before indexing</code>
• /send - <code>Send any message through bot to users. /send (username/userid) reply with message </code>"""

    STATUS_TXT = """<b>⍟───[ Sᴛᴀᴛᴜs Dᴇᴛᴀɪʟꜱ ]───⍟
    
⎇ Fɪʟᴇs Sᴀᴠᴇᴅ: <code>{}</code>
⎇ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
⎇ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
⎇ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code> Mɪʙ
⎇ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code> Mɪʙ</b>"""   

    LOG_TEXT_G = """#NewUser
 <b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {a}(<code>{b}</code>)</b>
 <b>᚛› 𝐆 𝐈𝐃 ⪼ @{c}
 <b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ {d}</b>
 <b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {e}</b>
 By {f}
 """

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    FILE_MSG = """
<b>Hai 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 Fɪʟᴇ Nᴀᴍᴇ</b> : <code>{}</code>              
                       
<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{}</b>
"""
    CHANNEL_CAP = """
<b>Hai 👋 {}</b> 😍

<code>{}</code>

⚠️ <b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>

<b>കോപ്പിറൈറ്റ് ഉള്ളതുകൊണ്ട് ഫയൽ 10 മിനിറ്റിനുള്ളിൽ ഇവിടെനിന്നും ഡിലീറ്റ് ആകുന്നതാണ് അതുകൊണ്ട് ഇവിടെ നിന്നും മറ്റെവിടെക്കെങ്കിലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക!</b>

<b>© Powered by {}</b>
"""
    SUR_TXT = """<b>{} {},

Mʏ Nᴀᴍᴇ Is <a href=https://t.me/{}>{}</a>, Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ I Wɪʟʟ Gɪᴠᴇ Mᴏᴠɪᴇs Oʀ Sᴇʀɪᴇs Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Pᴍ.</b>"""   

    IMDB_TEMPLATE_TXT = """
<b>⍞ TɪᴛLᴇ : {title}
⌬ YᴇAʀ : {year}
✇ LᴀNɢUᴀGᴇ : {languages}
⛦ RᴀTɪNɢ : {rating} / 10.0
〄 QᴜAʟIᴛY : HDRip</b>"""

    CUSTOM_FILE_CAPTION = """<b>🗂️ Fɪʟᴇ Nᴀᴍᴇ :- {file_name}

🔮 Fɪʟᴇ Sɪᴢᴇ :- {file_size}

⋟ @KLMovieGroup       
⋟ @KL_Group2</b>"""    

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️"""

    ALRT_TXT = """⚠️ 𝖧ᴇʏ !
    
𝖲ᴇᴀʀᴄʜ 𝖸ᴏᴜʀ 𝖮ᴡɴ 𝖥ɪʟᴇ, 
    
𝖣ᴏɴ'ᴛ 𝖢ʟɪᴄᴋ 𝖮ᴛʜᴇʀ𝗌 𝖱ᴇ𝗌ᴜʟᴛ𝗌 😬
"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧"""

    TOP_ALRT_MSG = """<b>Sᴇᴀʀᴄʜɪɴɢ Rᴇꜱᴜʟᴛꜱ. 🥴</b>"""

    MVE_NT_FND = """<b>This Movie Not Available 😢

🤠 <u>For Reasons</u> 👀

◉) OTT Or DVD Not Released..!
◉) Type Name With Year..!
◉) check your correct spelling..!
◉) Movie Is Not Available in My Database..!
◉) Not Available Theater Print 🥴..!</b>"""

    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    I_CUDNT = """ʜᴇʟʟᴏ {}, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ɪɴ ᴛʜᴀᴛ ɴᴀᴍᴇ​"""

    I_CUD_NT = """ʜᴇʟʟᴏ {}, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ​ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ . ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ​"""    
    
    CUDNT_FND = """<b>✯ Nᴏ Mᴏᴠɪᴇ Fᴏᴜɴᴅ Fᴏʀ Yᴏᴜʀ Qᴜᴇʀʏ <u>{}</u>

✯ Cʜᴏᴏsᴇ Tʜᴇ Cᴏʀʀᴇᴄᴛ Mᴏᴠɪᴇ Nᴀᴍᴇ Bᴇʟᴏᴡ 👇</b>​"""

    REPRT_MSG = """ Reported To Admin"""

    SPEL_CHK = """<b>🥺 Sorry No File Found <u>{}</u>

▫️Use The Button Below To Search On <u>Google</u> Or <u>IMDB</u> And Copy The Correct Movie Name And Paste..!!

▪️Don't Ask Movies That Are Not Released In OTT Platform..!!

▪️Try To Ask In [Moviename, Year, Language] This Format..!! 

🚯 Don't Use: ➠ ':(!,./) 🙅‍♂</b>"""

    OWNER_INFO = """
<b>⍟───[ Oᴡɴᴇʀ Dᴇᴛᴀɪʟꜱ ]───⍟
    
• Fᴜʟʟ Nᴀᴍᴇ : • HᴀᴄKᴇʀ Jʀ ~ 🕊 
• Uꜱᴇʀɴᴀᴍᴇ : @Hacker_Jr
• Lᴏɢᴏ Mᴀᴋᴇʀ Cʜᴀɴɴᴇʟ : <a href='t.me/PremiumlogoPro'>Pʀᴇᴍɪᴜᴍ Lᴏɢᴏ Pʀᴏ 🃏</a></b>"""

    GROUP_INFO = """
<b>⍟ Wᴇʟᴄᴏᴍᴇ Tᴏ Tᴇᴀᴍ Kʟ Lɪɴᴋs ⍟</b>"""

    FIlTERS_TXT = """
<b>Tʜᴇsᴇ Aʀᴇ Mʏ Tʜʀᴇᴇ Tʏᴘᴇs Oғ Fɪʟᴛᴇʀs.</b>"""

    GLOBE_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""

    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    AFTER_TXT = """<b>Hᴇʏ Tʜᴇʀᴇ 👋, {} Yᴏᴜʀ Lᴀsᴛ Mᴏᴠɪᴇ Rᴇᴏ̨ᴜᴇsᴛ Hᴀs Bᴇᴇɴ Dᴇʟᴇᴛᴇᴅ 🛑 Bᴇᴄᴀᴜsᴇ Oғ Cᴏᴘʏʀɪɢʜᴛ Issᴜᴇs...©️.
    
    Kɪɴᴅʟʏ Rᴇᴏ̨ᴜᴇsᴛ Aɢᴀɪɴ Fᴏʀ Yᴏᴜʀ Fɪʟᴇs ☺️
    
    Tʜᴀɴᴋ Yᴏᴜ ❤️
    Tᴇᴀᴍ [CT™]</b>"""
    
