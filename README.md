# IDEA Formatter

A simple POC to use GPT to format your idea to desired context text formats

Current support format
```
DESIRED_FORMATS=[
"[To Dos]",
"[Text Message]",
"[Ideas]",
"[Line Message]",
"[FB Post]",
"[中文 WeChat Post]",
"[Explain Like I'm Five]",
"[Outline]",
"[Elevator Pitch]",
"[Blog Post]",
"[LinkedIn Post]",
"[Movie Script]",
"[Song]",
"[College Essay]",
"[Professional Email]",
"[Twitter Thread]",
"[Summary]",
"[VC Pass Email]",
"[NY Times Article]",
"[中文 Professional Email (Mandarin)]",
"[Reddit Post]",
"[TikTok Script]",
"[中文 Explain Like I'm Five (Mandarin)]",
]
```



## Resources
可協助使用者生成相關形式文章 Format
https://www.theoasis.com/?fbclid=IwAR1dVmdatITlAGVG_Nc5qJdd1EV0_I6BPrJYhS7-v90WtBL1uDA9Jmaz2ro


- Original prompts
```
"請把我的靈感，直接轉化成社群貼文、部落格、電子郵件內文等，包辦「想法到成品」的過程。 我的想法是：{{天氣很好 }}， 請以繁體中文回復，把每個輸出內容依各個形式標題分段顯示，我需要的內容形式是： {{ 形式 || [To Dos]、[Text Message]、[Ideas]、[中文 WeChat Post]、[Explain Like I'm Five]、[Outline]、[Elevator Pitch]、[Blog Post]、[LinkedIn Post]、[Movie Script]、[Song]、[College Essay]、[Professional Email]、[Twitter Thread]、[Summary]、[VC Pass Email]、[NY Times Article]、[中文 Professional Email (Mandarin)]、[Reddit Post]、[TikTok Script]、[中文 Explain Like I'm Five (Mandarin)] }} 。"
```