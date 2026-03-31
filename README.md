# PhotoManagement



# Install photo frame

1. Set up a new raspberry pi
3. clone the git repo,
   * `git clone https://github.com/EchoDel/PhotoManagement.git`
4. Change to that folder
   * `cd PhotoManagement`
5. Copy the service 
   * `sudo cp ./install/PhotoManagement.service /etc/systemd/system/PhotoManagement.service`
6. Launch the service for the first time
   * `sudo systemctl start PhotoManagement.service`
   * Validate that it has started correctly
7. Setup the automated updates
   * `crontab -e`
   * `Add the following;  */5 * * * * /home/pi/PhotoManagement/install/ota_update.sh`
