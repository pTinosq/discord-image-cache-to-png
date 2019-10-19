# Discord cache to png extractor

## Welcome
This project came about when I had to trawl through my Discord cache to find a piece of evidence regarding a deleted screenshot. It took an unnecessarily long time so I decided it'd be best to just make a script that will trawl through that folder and convert everything to a png into a folder of my choice.


## How to use
1. Run cmd as an administrator
2. If the Discord directory isn't automatically found, you'll have to manually input it in the form: `C:\Users\example\hello\world\Discord`

3. The script will loop through all your cache and display all of the file names and at the end it will show how many files it found

4. Then you will be given the option a or b with `a` downloading all your images and `b` allowing you to decide how many images you'd like to download

5. If you selected `a` the final warning will appear now and if you selected `b` you can input the number of images to download in integer format

6. The script will then ask you for a save-to directory. This is where all the images will be dumped. **DO NOT USE YOUR DESKTOP, IT'LL FLOOD IT AND MAKE IT VERY HARD TO UNDO**

7. Once you have done that it'll do one last final check and initiate the download process.

8. Once done it'll automatically exit

## Common errors to avoid
* Setting save-to directory to a folder that isn't empty
* Setting save-to directory to Desktop or C:
* Using / instead of \ in file mentioning (Example: C:\hello\world)
* Not capitalizing where necessary
* Not running as administrator

## Contributing
The project is open source and can be contributed to by anyone as long as the contributions are useful.
