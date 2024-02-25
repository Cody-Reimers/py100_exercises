string = "Launch School"
start = string.find("c")
end = start + 6 if len(string) >= start + 6 else len(string)
print(string[start:end])