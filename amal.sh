echo "Activity tracker is starting"
cd Tracker
./main.py
git pull
git add .
git commit -m "added new activity"
git push -u origin master 

