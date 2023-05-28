def complain():
    x = input()
    with open("complains.txt", "a", encoding="utf-8") as f:
        f.write("\n" + x)
    print("Ваша жалоба будет рассмотрена в скором времени.")
def suggestions():
    with open("suggestions.txt", "r", encoding = "utf-8") as f:
      s=f.read()
      print("Предложения SkysmartBank")
    print(s)



