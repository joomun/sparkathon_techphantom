# Sparkathon Tech Phantom Project

## Setting up the server

Install Python3 and pip (Python package installer):

```bash
sudo apt-get install python3 python3-pip
```

## Transfer your application to the server

You can do this using `SCP` (Secure Copy Protocol), `FTP` (File Transfer Protocol), or by cloning from a Git repository if your project is in Git.

```bash
git clone git@github.com:joomun/sparkathon_techphantom.git
```

```bash
scp -r /path/to/your/sparkathon_techphantom user@server_ip:/path/to/your/project
```

## Setup a Virtual Environment

Use a virtual environment for Python applications to manage dependencies

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python run.py
```

## Set Up a Web Server Gateway Interface (WSGI):

1. For production, Flask’s built-in server is not suitable. You should use a production WSGI server. One common option is Gunicorn, which can be installed through pip:

   ```bash
   pip install gunicorn
   ```

2. Run your application through Gunicorn:

   ```bash
   gunicorn -w 3 run:app
   ```

## Configure a Reverse Proxy:

1. Install Nginx:

   ```bash
   sudo apt-get install nginx
   ```

2. Create a new server block configuration file in `/etc/nginx/sites-available/`:

   ```bash
   sudo nano /etc/nginx/sites-available/sparkathon_techphantom
   ```

3. Add the following configuration (replace `server_domain_or_IP` with your domain or IP, and also ensure the `proxy_pass` is correct):

   ```
   server {
    listen 80;
    server_name server_domain_or_IP;

    location / {
        proxy_pass http://localhost:8000;  # port where Gunicorn will be running
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
   }
   ```

   If you do not know your server’s IP address, you can find it by using the `icanhazip.com tool`, which will give you your public IP address as received from another location on the internet:

   ```bash
   curl icanhazip.com
   ```

4. Enable the server block by linking it to the sites-enabled directory:

   ```bash
   sudo ln -s /etc/nginx/sites-available/sparkathon_techphantom /etc/nginx/sites-enabled
   ```

5. Test your Nginx configuration for syntax errors:

   ```bash
   sudo nginx -t
   ```

6. If no errors are reported, restart Nginx:

   ```bash
   sudo systemctl restart nginx
   ```

## Start Gunicorn on Boot:

1. Create a systemd service file:

   ```bash
   sudo nano /etc/systemd/system/sparkathon_techphantom.service
   ```

2. Add the following configuration (replace `sammy` with your username, and also ensure the `WorkingDirectory` and `ExecStart` paths are correct):

   ```
   [Unit]
   Description=Gunicorn instance to serve Sparkathon Tech Phantom Project
   After=network.target

   [Service]
   User=sammy
   Group=www-data
   WorkingDirectory=/path/to/sparkathon_techphantom
   Environment="PATH=/path/to/sparkathon_techphantom/venv/bin"
   ExecStart=/path/to/sparkathon_techphantom/venv/bin/gunicorn -w 3 run:app

   [Install]
   WantedBy=multi-user.target
   ```

3. Start the Gunicorn service you created and enable it so that it starts at boot:

   ```bash
   sudo systemctl start sparkathon_techphantom
   sudo systemctl enable sparkathon_techphantom
   ```
