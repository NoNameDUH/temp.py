import time
import random
import threading

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
LINE_DOWN = '\033[1B'

BLACK = '\033[30m'
RED = '\033[31m'
OKGREEN = '\033[92m'
GREEN = '\033[32m'
PEACH = '\033[91m'
YELLOW = '\033[33m'
OKBLUE = '\033[94m'
BLUE = '\033[34m'
OKMAGENTA = '\033[95m'
MAGENTA = '\033[35m'
OKCYAN = '\033[96m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALIC = '\033[3m'

user_input = None
options = []

BattleNo = 0
wins = 0
ties = 0
Names = [OKGREEN + "The ROCK", PEACH + "PAPER Origmami", RED + "SCIZOR"]
lose = False
Inventory = []

def typing(PreTxt: str | None = "", txt: str | None = "", wait: float | None = 0.02, Input: bool | None = False):
  print(str(PreTxt), end="")
  no = len(PreTxt)
  for i in str(txt):
    no += 1
    print(i, end='', flush=True)
    time.sleep(wait)
  if bool(Input) == True:
    return input()

def Clear():
  print("")
  for i in range(100):
    print(LINE_UP, end=LINE_CLEAR)
  print("---Rock Paper Scissors---\n\n", end="")

def getinput():
  global user_input
  user_input = int(input("\rSHOOT: "))

def Invalid():
  for i in range(3):
    print("\r" + BOLD + RED + "Invalid input!" + RESET, end="" , flush=True)
    time.sleep(0.3)
    print("\r" + "              ", end="" ,flush=True)
    time.sleep(0.3)
  for i in range(100):
    print(LINE_UP, end=LINE_CLEAR)
  print(LINE_CLEAR + ":(")

def Battle():
  
  Clear()
  global BattleNo
  global wins
  global ties
  global lose
  global user_input
  
  BattleNo += 1
  enemy = random.randint(0, 2)
  options = [1, 2, 3]
  shotoptions = ["Rock", "Paper", "Scissors"]
  shotdeco = [OKGREEN, YELLOW, RED]
  enemy_shot = ["Rock", "Paper", "Scissors"]
  win = ["Paper", "Scissors", "Rock"]
  tools = ["Shield", "Trash"]
  del enemy_shot[enemy]
  user_input = None
  check_inventory = None

  print(BOLD + "Battle No. " + str(BattleNo) + RESET)
  print("\nWins: " + str(wins) + " | Ties: " + str(ties) + "\n")
  typing("", "You are challenged by ", 0.02)
  typing("", BOLD + Names[enemy] + RESET, 0.1)
  
  check_inventory = typing("\n\n", "Would you like to check your inventory? (Y/N)", 0.02, True)
  
  if check_inventory == "Y":
    if len[inventory] < 1:
      typing("\n\nInventory:\n\nempty", "...", 0.1, False)
      time.sleep(0.5)
  
  typing("\n\n", "On a count of three, choose either:\n1. Rock\n2. Paper\n3. Scissors\n\nType 1, 2, or 3 to shoot.", 0.02)
  typing("\n", "Ready?", 0.02, True)
  
  print("")
  for i in range(3):
    print("\r" + BOLD + shotdeco[i] + shotoptions[i] + RESET, end="" , flush=True)
    time.sleep(0.95)
    print("\r" + "              ", end="" ,flush=True)
    time.sleep(0.05)

  shot = threading.Thread(target=getinput)
  shot.start()
  
  shot.join(timeout=2)

  if user_input:
      if not user_input in options:
        Invalid()
      user = int(user_input) - 1
      if BattleNo == 1:
        opponent = enemy_shot[(user - 1)%3]
      opponent = random.choice(enemy_shot)
      typing("\n", "Opponent choose: " + opponent, 0.02)
      typing("\n", "You chose: " + shotoptions[user], 0.02)
      print("\n")
      if shotoptions[user] == opponent:
          typing("","It's a tie!", 0.02)
          ties += 1
      elif win[user] == opponent:
          typing("", RED + "You lose!" + RESET, 0.02)
          lose = True
      else:
          typing("",OKGREEN + "You win!" + RESET, 0.02)
          wins += 1
          if wins%2 == 1:
            typing("\n", "You gained a " + CYAN + random.choice[tools] + RESET + "!", 0.02)
  else:
      print("\nToo slow!" + BOLD + RED + "You lose!" + RESET)
      lose = True
  if lose != True:
    typing("\n\n", GREEN + "CONTINUE?" + RESET, 0.02, True)
    

Clear()
typing("", "", wait = 0.02)
typing("", "Welcome to ", wait = 0.1)
typing("", BOLD + RED + "Rock Paper Scissors" + RESET, 0.1)
typing(" : ", OKMAGENTA + ITALIC + "Roguelike" + RESET, 0.05)
typing("\n\n", BOLD + "How to play" + RESET, 0.02)
typing(":\n------------------\n", "· It's basically normal rock paper scissors\n· but non-stop duels...\n· You gain abilites everytime you win!", 0.02)
typing("\n", BOLD + RED + "· but once you lose, you DIE" + RESET, 0.02)
typing("\n\n", YELLOW + BOLD + "Get it?\n" + RESET, 0.02)
typing("", "Press ENTER to start", 0.02, True)

while lose == False:
  Battle()
