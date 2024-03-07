from Repo import Repo
from Service import Service
from ui import Ui



def main():
    repo = Repo("listfile.txt")
    service=Service(repo)
    ui=Ui(service)
    ui.run()

if __name__ == "__main__":
    main()
