import subprocess
import platform
import socket
import time
import os

import git
import psutil
import colorama
from colorama import Fore
import difflib
import pathlib
import calendar
import random
import datetime
from win32api import GetSystemMetrics
from git import *

def play_hangman():
  iot = open('words.txt', 'r')
  word_list = iot.readlines() 
  
  # Select a random word from the list
  word = random.choice(word_list)
  # Use a set to store the letters the user has guessed
  letters_guessed = set()
  # Set the number of guesses the user has
  num_guesses = 6

  # Create a list of underscores the same length as the word
  # to represent the letters the user has not yet guessed
  word_letters = list(word)
  for i in range(len(word_letters)):
    word_letters[i] = "_"

  # Main game loop
  while num_guesses > 0:
    # Print the current state of the word
    print("Current word: ", " ".join(word_letters))
    # Prompt the user to guess a letter
    letter = input("Guess a letter: ").lower().strip()
    # Check if the letter has already been guessed
    if letter in letters_guessed:
      print("You already guessed that letter.")
      continue
    # Add the letter to the set of letters guessed
    letters_guessed.add(letter)
    # Check if the letter is in the word
    if letter in word:
      print("Correct!")
      # Update the state of the word to reveal the letter
      for i in range(len(word)):
        if word[i] == letter:
          word_letters[i] = letter
      # Check if the user has won
      if "".join(word_letters) == word:
        print("Congratulations, you won!")
        return
    else:
      print("Incorrect!")
      num_guesses -= 1
    print("You have", num_guesses, "guesses left.")
  # The user has run out of guesses
  print("You lost! The word was", word)
os.system('cls')
today = datetime.datetime.now()
yy =  today.year
mm = today.month
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "
PIPE = "│"
ELBOW = "└──"
TEE = "├──"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
colorama.init(autoreset=True)
print(Fore.LIGHTGREEN_EX + "SINO TERMINAL [VERSION 0.05]")
print(Fore.LIGHTGREEN_EX + "(c) ACL COMPUTERS. ALL RIGHTS RESERVED.")
print("                                       ")
while True:
    print()
    cmd = input(Fore.CYAN + host_name + " " + Fore.LIGHTYELLOW_EX + " " + "~").lower().strip()
    if cmd == "ping":
        host = input(Fore.BLUE + "Enter Website To Ping: ")
        number = input(Fore.BLUE + "Enter How Many Times To Ping")


        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            print(Fore.WHITE + str(subprocess.call(command)))


        print(ping(host))
    elif cmd == 'local':
        pid = str(os.getpid())
        print(Fore.WHITE + "LOCAL IPS:" + host_ip)
        print(Fore.WHITE + "DESKTOP NAME:" + host_name)
        print(Fore.WHITE + "OS NAME:" + platform.platform())
        print(Fore.WHITE + "OS VERSION:" + platform.version())
        print(Fore.WHITE + "COMPUTER PROCESSOR:" + platform.processor())
        print(Fore.WHITE + "MACHINE:" + platform.machine())
        print(Fore.WHITE + "OS RELEASE:" + platform.release())
        print(Fore.WHITE + "REGISTERED OWNER:" + os.getlogin())
        print(Fore.WHITE + "PRODUCT ID:" + pid)
        print(Fore.WHITE + "TIME ZONE:" + time.strftime("%z", time.gmtime()))
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        newwidth = str(width)
        newheight = str(height)
        print(Fore.WHITE + "Screen resolution" + newwidth, "x", newheight)

    elif cmd == 'date':
        print(Fore.WHITE + "DATE:" + time.strftime("%m/%d/%Y"))

    elif cmd == "list":
        dir_list = input("Enter a path")
        print(Fore.WHITE + "YOUR FILES AND DIRECTORIES:")
        print(Fore.WHITE, dir_list)
    elif cmd == "read":
        text = input(Fore.BLUE + "ENTER THE TEXT FILE YOU WANT TO READ")
        file = open(text)
        read = file.readlines()
        print(Fore.WHITE, read)
        file.close()
    elif cmd == "read -c":
        print(Fore.BLUE + "ENTER THE FILE YOU WANT TO CHANGE:")
        text1 = input(Fore.BLUE + ":")
        opeeen = open(text1, 'w')
        print(Fore.BLUE + "RE-WRITE YOUR FILE:")
        ab = input(Fore.BLUE + ":")
        change = opeeen.write(ab)
        opeeen.close()
        print(Fore.WHITE + "file successfully updated")
    elif cmd == "file_opener":
        print(Fore.BLUE + "Enter the path to the app:")
        dir = input(Fore.BLUE + ":")
        os.startfile(dir)
        print(Fore.WHITE + dir +" IS SUCCESSFULLY OPENED")
    elif cmd == "usage":
        cpu = str(psutil.cpu_percent())
        ram = str(psutil.virtual_memory())
        print(Fore.WHITE + "CPU USAGE: " + cpu + " percent")
        print(Fore.WHITE + "RAM USAGE: " + ram)

    elif cmd == "help":
        print(Fore.WHITE + "local: Shows information about the computer")
        print(Fore.WHITE + "ping: sends one datagram per second and prints one line of output for every response received")
        print(Fore.WHITE + "read: Reads a text file")
        print(Fore.WHITE + "read -c: Re-writes or writes a text file")
        print(Fore.WHITE + "list: lists files and directories")
        print(Fore.WHITE + "file_opener: Allows user to open a file")
        print(Fore.WHITE + "exit: exits the SINO terminal")
        print(Fore.WHITE + "usage: shows RAM and CPU usage")
        print(Fore.WHITE + "new-file: Creates a new file")
        print(Fore.WHITE + "del: deletes a file")
        print(Fore.WHITE + "boottime: show the computers boottime")
        print(Fore.WHITE + "tasklist: Shows a list of taks the computer is doing")
        print(Fore.WHITE + "file_compare: compares 2 files")
        print(Fore.WHITE + "file_tree: generates a file tree")
        print(Fore.WHITE + "serial_number: shows serial number of the motherboard ")
        print(Fore.WHITE + "ren:renames a file")
        print(Fore.WHITE + "cal: shows calendar")
        print(Fore.WHITE + "search: searchs files")
        print(Fore.WHITE + "clr:cleares the screen")
        print(Fore.WHITE + "hangman: A game to play when your taking a break")
        print(Fore.WHITE + "file_info: finda information about a file")
    elif cmd == "exit":
        exit()

    elif cmd == "new-file":
        newfile = input(Fore.BLUE + "NAME OF THE FILE THAT YOU WILL CREATE:")
        newpath = input("Enter your path to the file")
        filepath = os.path.join(newpath, newfile)
        ab = open(filepath, "x")
        print(Fore.WHITE + "new file created")

    elif cmd == "del":
        removefile = input(Fore.BLUE + "Enter the file you want to delete:")
        if os.path.exists(removefile):
            os.remove(removefile)
            print(Fore.WHITE + "File deleted")

    elif cmd == "boottime":
        last_reboot = int(psutil.boot_time())
        print(Fore.WHITE + str(datetime.datetime.fromtimestamp(last_reboot)))
        print(Fore.WHITE + "This is your current boot time")
        
    elif cmd =="tasklist":
        output = os.popen('wmic process get description, processid').read()
        print(Fore.WHITE + output)

    elif cmd == "file_compare":
        x = input(Fore.BLUE + "First File:")
        y = input(Fore.BLUE + "Second File:")
        with open(x) as file1:
            file1_text = file1.readlines()
        with open(y) as file2:
            file2_text = file2.readlines()
        for line in difflib.unified_diff(
            file1_text, file2_text, fromfile=x,
            tofile=y, lineterm=''):
            print(Fore.WHITE+ line)

    elif cmd == "file_tree":
        def generate_directory(
                tree, item, index, len_diritems, prefix, connector):
            tree.append(f"{prefix}{connector} {item.name}{os.sep}")
            if index != len_diritems - 1:
                prefix += PIPE_PREFIX
            else:
                prefix += SPACE_PREFIX
            add_body(tree, item, prefix)
            tree.append(prefix.rstrip())


        def add_root(tree, root_directory):
            tree.append(f"{root_directory.name}{os.sep}")
            tree.append(PIPE)


        def add_body(tree, root_directory, prefix=""):
            dir_iter = root_directory.iterdir()
            diretory_items = sorted(dir_iter, key=lambda item: item.is_file())
            len_diritems = len(diretory_items)
            for index, item in enumerate(diretory_items):
                connector = ELBOW if index == len_diritems - 1 else TEE
                if item.is_dir():
                    generate_directory(
                        tree, item, index, len_diritems, prefix, connector)
                else:
                    tree.append(f"{prefix}{connector} {item.name}")


        def make_tree(root_directory):
            tree = []
            add_root(tree, root_directory)
            add_body(tree, root_directory)
            return tree


        directory = input("enter a path")
        try:
            root_directory = pathlib.Path(directory)
            tree = make_tree(root_directory)
            for item in tree:
                print(item)
        except Exception as e:
            raise e

    elif cmd == "serial_number":
        print(Fore.WHITE +"Serial number:"+ current_machine_id)

    elif cmd == "ren":
        new_address = input(Fore.BLUE + "Source address of the file:")
        new_dest = input(Fore.BLUE + "Destination of the file with the new name")
        os.rename(new_address, new_dest)# renames and puts it in a new destination
        print(Fore.WHITE + "FILE SUCCESSFULLY RENAMED")

    elif cmd == "cal":
        print(Fore.WHITE + calendar.month(yy,mm))

    elif cmd == "search":
        rootDir = input("Path of the file you want to search")
        fileToSearch = input("Name of the file")
        for relpath,dirs,files in os.walk(rootDir):  #loop for finding file
            if(fileToSearch in files):
                fullPath = os.path.join(rootDir,relpath,fileToSearch)
                print(Fore.WHITE + fullPath)
            else:
                print(Fore.WHITE + "Could not find file")

    elif cmd == "clr":
        os.system('cls')
        
    elif cmd == "hangman":
         play_hangman()
         
    elif cmd == "file_info":
          file_input = input(Fore.BLUE + "path of the file")
          file_size = os.path.getsize(file_input)
          file_extension = pathlib.Path(file_input).suffix
          print(Fore.WHITE + "File size:", file_size, "bytes")
          print(Fore.WHITE + "File type:", file_extension)

    elif cmd == "git":
        print( Fore.WHITE + """
        usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

        """)
        job = input(Fore.BLUE + "git :")
        if job == "init":
            init = input(Fore.BLUE + "name with path of of the file")
            new_repo = git.Repo.init(init)  #creates git directory with path
        if job == "clone":
            cloned = input("Enter URL to gist/git")
            pathy = input("Enter path to create file")
            new_repo2 = Repo.clone_from(cloned, pathy)

    else:
          print(f"command {cmd} not found")
