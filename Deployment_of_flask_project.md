
### Deployment of Machine Learning or Flask Projects on AWS (Amazon Web Services)

#### Step-by-Step Guide

---

### Step 1: Launch EC2 Instance
- **Action**: Launch a new EC2 instance.
- **Process**: 
  - Choose an instance name.
  - Select the OS system (Ubuntu recommended).
  - Create a key pair if you don't have one already.
  - Finally, launch the instance.

---

### Step 2: Create a Security Group
- **Action**: Create a security group to control the instance's traffic.
- **Process**: 
  - Provide a name for the security group.
  - Add inbound rules (allow **All Traffic** for the purpose of testing, but for production, restrict to required ports like 22 for SSH, 80/443 for HTTP/HTTPS).
  - Allow the IPv4 address (0.0.0.0/0 for open access, or restrict to specific IPs).

---

### Step 3: Link Security Group to Network Interface (NI)
- **Action**: Link the created security group to the network interface.
- **Process**: This can be done in the EC2 instance settings to ensure the security group is applied.

---

### Step 4: SSH into the EC2 Instance
- **Command**:
  ```bash
  ssh -r -i "your-key.pem" LOCALPATH remote-server 
  ```
  - Once connected, you can use `pwd`, `ls`, etc. to verify the connection.
  - **Logout** once you are done with initial setup.

---

### Step 5: Copy Project Files to the EC2 Instance
- **Command**:
  ```bash
  scp -i "your-key.pem" your-project-folder remote-server:~/
  ```
  - This command copies your project folder from the local machine to the remote server (EC2 instance).

- **Login Again** to EC2:
  ```bash
  ssh -r -i "your-key.pem" LOCALPATH remote-server
  ```
  - Navigate to the folder and verify that the files are copied by running:
    ```bash
    ls
    ```

---

### Step 6: Update EC2 Packages
- **Command**:
  ```bash
  sudo apt update
  ```

### Step 7: Upgrade EC2 Packages
- **Command**:
  ```bash
  sudo apt upgrade
  ```

---

### Step 8: Install Python and Pip
- **Command**:
  ```bash
  sudo apt install python3-pip
  ```
  - Verify the Python version:
    ```bash
    python3 -V
    ```

---

### Step 9: Install Project Dependencies
- **Action**: Navigate to your project folder and install dependencies.
- **Commands**:
  ```bash
  cd web_app
  pip install -r 'requirements.txt'
  ```
  If `pip install` fails, you can set up a virtual environment:
  ```bash
  sudo apt install python3-venv
  python3 -m venv myenv
  source myenv/bin/activate
  pip install -r 'requirements.txt'
  ```

---

### Step 10: Verify Installed Libraries
- **Command**:
  ```bash
  pip list
  ```
  - Ensure Flask and other required libraries are installed.

---

### Step 11: Navigate to Project Directory
- **Command**:
  ```bash
  cd web_app
  ls
  ```
  - Verify that all files and folders are present.

---

### Step 12: Run the Flask Application
- **Command**:
  ```bash
  python3 app.py
  ```

---

### Step 13: Access the Application via Browser
- **Action**: 
  - Go to the **AWS EC2 instance running page**.
  - Copy the **Public IPv4 address**.
  - Paste it in your browser (use `http://your-public-ip:5000` if your app runs on port 5000).

---

### Step 14: Run Flask Application in the Background
- **Action**: To keep the application running even after disconnecting from SSH, use `nohup`.
- **Command**:
  1. Stop the running application by pressing `Ctrl + C`.
  2. Run the app in the background:
     ```bash
     nohup python3 app.py &
     ```
  3. Logout from the EC2 instance.

---

### Step 15: Verify Application is Running
- **Commands**:
  - To check if the application is running:
    ```bash
    top -u $USER
    ```
  - To clear the terminal:
    ```bash
    clear
    ```
  - To kill the running application (if needed):
    ```bash
    kill 13777  # (replace with the actual process ID)
    ```
  - To forcefully kill the application:
    ```bash
    kill -9 13777  # (replace with the actual process ID)
    ```
  - Logout once done:
    ```bash
    logout
    ```

---

### Restarting EC2 Instance After Stopping

When you stop and restart the EC2 instance, the **Public IPv4 address** changes, so you will need to repeat some steps to get the app running again.

1. **SSH into the Instance Again**:
   ```bash
   ssh -r -i "your-key.pem" LOCALPATH remote-server
   ```

2. **Update and Upgrade Packages** (if necessary):
   ```bash
   sudo apt update
   sudo apt upgrade
   ```

3. **Navigate to Your Project Directory**:
   ```bash
   cd /path/to/your/project
   ```

4. **Run the Flask App Again in the Background**:
   ```bash
   nohup python3 app.py &
   ```

Your app will now be running again, and you can access it via the new public IP.

---

Following these steps will allow you to deploy, manage, and restart your machine learning project on AWS using EC2! Let me know if you need further clarification or assistance.
