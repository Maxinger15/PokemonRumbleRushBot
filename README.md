---
This project won't get any new Updates

Currently only for german, english and france
Optimized for a 16:9 screens with a resolution of 1080x1920 and nox app player even on 1080x1920. If you have a different screen look in the "Issues" section for help. 
---

<h2 id="only-for-android">ONLY FOR ANDROID</h1>
<h2 id="index">Index</h2>
<ul>
<li><a href="#what-it-does">What it does</a></li>
<li><a href="#requirements">Requirements</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#config">Config</a></li>
<li><a href="#future">About the Future</a></li>
<li><a href="#help">Help me and others</a></li>
<li><a href="#screenTutorial">How to create a screen config</a></li>
<li><a href="https://www.reddit.com/r/PokemonRumbleRushBots/" target="_blank">Our Subreddit</a></li>
</ul>
<h2 id="what-it-does">What it does</h2>
<p>This Bot is able to play one of the three selected adventures and destroys every ore once your factory is full. This is good to get high level creatures.</p>
<h2 id="requirements">Requirements</h2>
<ul>
<li><a href="#python">Python 3.7</a></li>
<li><a href="#tesseract">Tesseract 4.0</a></li>
<li><a href="#minimal-adb-and-fastboot">Minimal adb and fastboot</a></li>
<li>Python-Packages:<br>
– <a href="#pure-python-adb">pure-python-adb</a><br>
– <a href="#pytesseract">pytesseract</a></li>
</ul>
<h3 id="python">Python:</h3>
<p>The main logic is written in python.<br>
<a href="https://www.python.org/downloads/" target="_blank">Download</a></p>
<h3 id="tesseract">Tesseract:</h3>
<p>Tesseract is a optical character recognition engine which is used to detect the different states of the game by reading the text on your display.<br>
<a href="https://github.com/UB-Mannheim/tesseract/wiki" target="_blank">Download</a><br>
<a href="https://github.com/tesseract-ocr/tesseract" target="_blank">Wiki</a></p>
<h3 id="pure-python-adb">pure-python-adb</h3>
<p>This package is used to interact with the adb server.</p>
<h3 id="pytesseract">pytesseract</h3>
<p>This package is used to communicate with Tesseract</p>
<h3 id="minimal-adb-and-fastboot">Minimal adb and fastboot</h3>
<p>This is the host for the adb-server which is used to communicate with the mobile phone.<br>
<a href="https://forum.xda-developers.com/showthread.php?t=2317790" target="_blank">Download</a></p>
<h2 id="installation">Installation</h2>
<h3 id="windows">Windows</h3>
<ol>
<li>
<p>Enable USB-Debugging on your device</p>
</li>
<li>
<p>Download and install <a href="#python">python</a></p>
</li>
<li>
<p>Download and install <a href="#minimal-adb-and-fastboot">Minimal adb and fastboot</a></p>
</li>
<li>
<p>Download the files from the repository and copy them to any folder.</p>
</li>
<li>
<p>Open CMD and type:<br>
– <code>pip install pure-python-adb</code><br>
– <code>pip install pytesseract</code></p>
</li>
<li>
<p>Download and install <a href="#tesseract">Tesseract</a>. Select in the installer your language pack for Tesseract</p>
</li>
<li>
<p>Copy the path of the installation directory from Tesseract and replace the given Path in the Config.cfg</p>
</li>
<li>
<p>Edit the selected_raid variable in the config with a number between 1 and 3 depending on what raid should be played</p>
</li>
<li>
<p>Start Minimal adb and fastboot and type into the new window: <code>adb start-server</code></p>
</li>
<li>
<p>Open the Pokemon Rumble Rush app and go to the main menu</p>
</li>
<li>
<p>Go to the directory with the <a href="http://start.py">start.py</a> file, click in the address bar, type <code>cmd</code> and press enter.</p>
</li>
<li>
<p>Now write: <code>python start.py</code></p>
</li>
<li>
<p>Enjoy :)</p>
</li>
</ol>
<h3 id="linux">Linux</h3>
<p>Coming soon</p>
<h3 id="config">Config:</h3>
<p>The config is located in the conf folder and can be opend with the editor.</p>
<p>There you can change the language to your language. Possible values are explained in the config file. Currently are Englisch and German 
   available (Default Value: DE)</p>
<p> You can also change the speed to make the bot grinds faster (CAUTION!!! if you are to fast it wont work anymore) or slow down if your handy isn´t the newest.</p>
<p> To select which Raid you want to play you have to edit the selected_raid row in the config. Choose 1, 2 or 3</p>
<p> <img src="https://raw.githubusercontent.com/Maxinger15/pgrinder/images/raid%20numeration%20explenation.png" width="400" height="300"/></p>
<p> If you want to help me or you have a problem you can also enable debuging</p>
<p> To change the rounds the bot should play change the value of rounds </p>
<h2 id="future">About the Future</h2>
<p> If you would help me feel free contact me and we can work together. In the near future I want to add a config file for the button coordinates of
 different devices. It´s also planned to add more Tutorials with Pictures about writing the different configs.</p>
 <p>In the middle future I plan to make a Windows Installer (If you know how this works contact me because I don´t know yet) and make tests with the bot on an raspberry pi 3b+.</p>
 <p>Far away are things like a GUI.</p> 
 <h3 id="help">Help me and others</h3>
 <p> This is my first Project I share with others. I try to give my best to make the bot more comfortable and stable. But to do this I will need help (or it take
a long time). If you want to help me go to the project site on github and have a look what topics are open. Or write some new topics to me if you have good ideas.
The best thing you can do is to help me programming the bot. If you want to then write a message to me on discord (Maxinger#1608) or create a pull-request. If you have any 
other idea how you can help me contact me. I am happy about every type of help. If you know how to fix common errors or something else about the bot feel free to write an article in the wiki</p>
 

<h3 id="screenTutorial">How to create a screen config</h3>
<ol>
<li>Start the script with <code>python start.py --init</code>. This will create a json with the name of your phone in the template folder inside the screens folder.</li>
<li>Go to the <a href="https://www.greenbot.com/article/2457986/how-to-enable-developer-options-on-your-android-phone-or-tablet.html" target="_blank">developer options</a> in your settings 
 and eneable the option "Pointer location". This will show you on the top of the screen a bar with the x and y coordinates of a touch on the display. If you have a notch you have to make a screenshot to see the y coordinate.</li>
<li>The following images show you the name in the config and the point on the screen where you have to take the coordinates:
   <p><img src="https://raw.githubusercontent.com/Maxinger15/PokemonRumbleRushBot/images/adventure.png" width="400" height="400"/></p>
   <p><img src="https://raw.githubusercontent.com/Maxinger15/PokemonRumbleRushBot/images/select_raid.png" width="400" height="500"/></p>
   <p><img src="https://raw.githubusercontent.com/Maxinger15/PokemonRumbleRushBot/images/battle.png" width="400" height="400"/></p>
   <p><img src="https://raw.githubusercontent.com/Maxinger15/PokemonRumbleRushBot/images/next_done.PNG" width="400" height="600"/></p>
   <p><img src="https://raw.githubusercontent.com/Maxinger15/PokemonRumbleRushBot/images/trashcan.png" width="400" height="600"/></p>
   <p><img src="https://raw.githubusercontent.com/Maxinger15/PokemonRumbleRushBot/images/refineryClose.png" width="400" height="500"/>    </p>
   <p><img src="https://raw.githubusercontent.com/Maxinger15/PokemonRumbleRushBot/images/yesToRecycle.png" width="400" height="600"/>  </p>
   <p><img src="https://raw.githubusercontent.com/Maxinger15/PokemonRumbleRushBot/images/dontRefine.png" width="400" height="500"/></p>
   <p>The ore_acceptNoOre don't need to be set at the begining. If you always have a ore working in your factory the message where this button is needed won't apear.</p>
</li> 
<li>Write your coordinates in the config. The first number is x the second is y</li>
<li>If you have used the --init argument to create the config the program recognize it automaticly.</li>
<li>If your config works commit it to the repo or post a link to the file to our <a href="https://www.reddit.com/r/PokemonRumbleRushBots/" target="_blank">subreddit</a></li>


</ol>
