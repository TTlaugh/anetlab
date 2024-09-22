# ⁉️ What is this
- A Terminal User Interface (TUI) tool that automatically install and configure services on Linux server using Docker
- e.g. DNS, Email, Web,...
- That's it!

# 💫 Now
- 🤔 This is just the idea stage
- 📖 I'm still in the process of learning.

# 🔎 Looking for collaborate
Are you interested in diving deeper into Linux and networking? Or maybe you're looking to become a system administrator? Let's work together on this project and learn from each other. We'll create something useful and have a lot of fun in the process. Or, if you're a Linux enthusiast and command-line interface, this is where you can start your first project! It's also a great way to add to your skills and boost your resume. Join me and let's build something awesome!

# 📌 Current progress
- Demo DNS server using BIND on docker
    > Take a look at the configuration files in dns/config before running the demo.
    - How to run:
    ```
    cd dns
    docker compose up -d # -d for detach and run in background
    ```
    - Test (local host):
    ```
    nslookup anetlab.home 127.0.0.1 # localhost server's ip
    ```

### 📦 Requirement
- Linux server
- Docker (compose)
- Python 3
- [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)
- Knowledge about Linux and Networking
