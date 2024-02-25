info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
partitions = info.split(":")
result = "+".join(partitions)
print(result)

result2 = info.replace(":", "+")
print(result2)