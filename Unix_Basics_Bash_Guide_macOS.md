
# 🧪 Unix Directory Structure & Bash Basics (for macOS Users)

## 📘 1. What is Unix Directory Structure?

```
/
├── bin/       → essential binaries (commands)
├── etc/       → configuration files
├── home/      → user directories (on macOS: /Users/)
├── tmp/       → temporary files
├── usr/       → user programs, libraries, etc.
├── var/       → logs, spool files, etc.
└── dev/       → hardware devices
```

On macOS, your personal files live in `/Users/yourusername`, often referenced as `~`.

---

## 💻 2. Open Terminal on Mac

Open **Spotlight Search** (`Cmd + Space`) → type `Terminal` → press Enter.

---

## 📂 3. Navigating Directories

| Command              | What It Does                      |
|----------------------|-----------------------------------|
| `pwd`                | Show current directory            |
| `ls`                 | List files                        |
| `ls -l`              | Detailed list                     |
| `cd`                 | Change directory                  |
| `cd ~`               | Go to home directory              |
| `cd ..`              | Go up one level                   |
| `cd /`               | Go to root                        |
| `cd /Users`          | Navigate to Users directory       |

### 🧪 Examples
```bash
pwd
cd Documents
cd ..
ls -la
```

---

## 📁 4. File & Directory Operations

| Command                     | Description                          |
|-----------------------------|--------------------------------------|
| `mkdir myfolder`            | Create directory                     |
| `touch myfile.txt`          | Create file                          |
| `rm myfile.txt`             | Delete file                          |
| `rm -r myfolder`            | Delete directory                     |
| `cp file1.txt file2.txt`    | Copy file                            |
| `mv old.txt new.txt`        | Rename or move file                  |

---

## 📄 5. Viewing and Editing Files

| Command           | Description                      |
|-------------------|----------------------------------|
| `cat file.txt`    | Show contents                    |
| `less file.txt`   | Paginated view                   |
| `head file.txt`   | First 10 lines                   |
| `tail file.txt`   | Last 10 lines                    |
| `open file.txt`   | Open in Mac app                  |
| `nano file.txt`   | Edit using nano                  |

---

## 🔍 6. Searching & Finding Files

| Command                        | Description                  |
|--------------------------------|------------------------------|
| `find . -name "*.txt"`         | Find all `.txt` files        |
| `grep "text" file.txt`         | Search in file               |
| `grep -r "text" .`             | Recursive text search        |

---

## ⚙️ 7. Permissions & Ownership (Basics)

| Command                | Description                         |
|------------------------|-------------------------------------|
| `ls -l`                | Show file permissions               |
| `chmod +x file.sh`     | Make script executable              |
| `chmod 644 file.txt`   | Read/write for owner, read for others |

---

## 📦 8. Package Management on macOS (Homebrew)

### Install Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Use it
```bash
brew install wget
brew install tree
```

---

## 🧪 9. Practice Exercises

| Task                                  | Command                                  |
|--------------------------------------|------------------------------------------|
| Make folder & file                   | `mkdir test && touch test/hello.txt`     |
| Move into folder                     | `cd test`                                |
| View file                            | `cat hello.txt`                          |
| Rename file                          | `mv hello.txt goodbye.txt`               |
| Delete file and folder               | `rm goodbye.txt && cd .. && rmdir test`  |

---

## 📚 10. Tips & Tools

- `man <command>` – manual/help
- Use [https://explainshell.com](https://explainshell.com)
- Use Tab for autocompletion
