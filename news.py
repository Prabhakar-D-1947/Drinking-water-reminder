import requests
import webbrowser

url = "https://gnews.io/api/v4/top-headlines"
print("================== News Outlet =================")
print("1. Technology")
print("2. Sports")
print("3. Business")
print("4. Health")

while True:
    choice = input("Choose category: ")
    if choice == "1":
        category = "technology"
        break

    elif choice == "2":
        category = "sports"
        break
    elif choice == "3":
        category = "business"
        break       
    elif choice == "4":
        category = "health"
        break
    else:
        print("Invalid choice")
        continue

parameter = {
    "apikey":"8425e297f70e97aa3c980c375634ad58",
    "country": "in",
    "lang":"en",
    "category": category
}

response = requests.get(url,params = parameter)

data = response.json()
if len(data["articles"]) == 0:
    print("No articles found.")
    exit()
for i, article in enumerate(data["articles"], start=1):
    print(i, article["title"])
    print(" ")
while True:
    choice = int(input("Choose article: "))

    article = data["articles"][choice - 1]

    print("\nTitle:", article["title"])
    print("Source:", article["source"]["name"])
    print("Description:", article["description"])
    webbrowser.open(article["url"])

    again = input("\nDo you want to read another article? (y/n): ")

    if again.lower() == "n":
        break

print("Thank you for using News Outlet!")



