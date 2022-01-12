
##Install Python3.7##
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
##Install dependencies##
python3.7 -m pip install --upgrade pip
python3.7 -m pip install -r requirements.txt
##Mess around because pillow is a pain##
python3.7 -m pip uninstall Pillow
python3.7 -m pip install Pillow
##Get latest version of gecko driver##
cd /home/greenminds-screengrab
Download from https://github.com/mozilla/geckodriver/releases
tar -xzf <downloaded file>
##Run script##
python3.7 screengrab.py 
