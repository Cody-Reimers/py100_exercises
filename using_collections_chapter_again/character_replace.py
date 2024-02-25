info = "xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh"
info = "+".join(info.split(":"))
print(info)

info = "xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh"
print(info.replace(":", "+"))