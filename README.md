#Starting the script
Before you can start the script, you need to install the requiered dependecies
```
pip install selenium beautifulsoup4 progress
```

After the depedencies are installed, you can launch the script with the following command:

```
python main.py
```

#Configuring
If you want to use a diffrent URL, or turn headless mode on/off, you need to edit this line in main.py:

```
driver_manager = DriverManager("https://play.typeracer.com", headless=False)
```

To edit the CPM and Accuracy, change this line in main.py:

```
cheat = Cheat(driver_manager, 400, 0.1)
```