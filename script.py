import emoji

snake = emoji.emojize("🐍")
eyes = emoji.emojize("👀👀")
book = emoji.emojize("📖")
thumbs_up = emoji.emojize(":thumbs_up:")

htmlContent = f""" <meta charset="UTF-8"> <html>
<head></head>
<body>

<p style="font-size:100px">

{ snake }
<br/>
{ eyes }
<br/>
{ book }
<br/>

{ thumbs_up }

</p>

</body>
</html>"""


with open("index.html", "w", encoding="utf-8-sig") as myFile:
    myFile.write(htmlContent)