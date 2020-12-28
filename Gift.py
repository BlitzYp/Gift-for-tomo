import requests
import termcolor

def get_data(topic):
    data = requests.get(f"https://icanhazdadjoke.com/search", headers={"Accept": "application/json"}, params={"term": topic, "limit": 5}, )
    if data.status_code != 200:
        return { "status": "bad" }
    return data.json()

def get_jokes():
    topic = input("Enter topic: ")
    data = get_data(topic)
    if data.get("status") == "bad" or not len(data.get("results")):
        print("No jokes about this sorry")
        return
    for joke in data.get("results"):
        print(joke.get("joke"))

def main():
    termcolor.cprint("Merry Christmas, Tomo!", color="yellow")
    get_jokes()

if __name__ == "__main__":
  main()