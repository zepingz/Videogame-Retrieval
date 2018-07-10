# Videogame-Retrieval

This is the tutorial notebook collection for videogame retrieval project.

# About BizHawk

BizHawk is an emulator designed originally for the Tool-Assisted Speedruns (TAS) community. We use BizHawk because it supports a number of platforms such as SNES, GB and N64, it has full recording support and more importantly it allows Lua scripting. 

The version of BizHawk we were using for the videogame retrieval project is 2.2.2. If you plan to run some of our lua or python scripts, make sure you are using 2.2.2 or later.

You can download the precompile BizHawk in http://tasvideos.org/BizHawk/ReleaseHistory.html

You should run a couple of roms to make sure that BizHawk works.

# BK2 Movie

According to http://tasvideos.org/Bizhawk/BK2Format.html, “.bk2 is an archive file that contains movie data broken into various files. It is a zip format and can be opened with any unzip tool, such as 7z.” Essentially, bk2 files allow us to record and play previous input back. Most bk2 files on the internet are stored in the TASVideos website and these movies are usually tool-assisted speedrun. For example, http://tasvideos.org/2948M.html is the speedrun movie for ActRaiser 2 in SNES. To get a better description of what a bk2 file is, check out http://tasvideos.org/Bizhawk/BK2Format.html

Unfortunately, there are several issues preventing us from using almost all of the movie files in TASVideo. First of all, not all movies in TASVideo are in the bk2 format. Some of them are bkm files, the obsolete movie format, while some others are lsmv files or smv files, movie formats for other emulators. Although bizhawk provides a way to convert them to bk2 format, it is not guaranteed that the converted bk2 files would still be in sync. Even with a bk2 files there is still a chance where it is not compatible with the latest version of BizHawk because it is recorded in a much older version of BizHawk.

# How to record an input sequence (movie)

1. Run BizHawk
2. File -> Open Rom
3. File -> Movie -> Record Movie... (record from power on)
4. Play game
5. File -> Movie -> Stop Movie

Note that the movie file should be stored in BizHawk-2.2.2/Movies by default

# How to turn a bk2 file into screenshots and memory

1. Put all of your .bk2 files and rom files you want to convert in "movies" folder and "roms" folder respectively
2. Rename your .bk2 files the same name as the corresponding rom files
3. Run "Working with Human Data" notebook

# Notes

Before running these scripts, a rom of any SNES game should be prepared.

Idealy there is no need to change action.lua and collect.lua unless bizhawk built-in functions are not efficient.

Be aware that the rom_path variable in all script is empty. It needs to be changed to the path to yourr rom file.

The lua path should be the relative path to the EmuHawk.exe instead of to the script itself.

# Tutorial Notebooks

1 - Scripting BizHawk from Python:

Showing how to feed lua code into BizHawk from python script.

2 - Comparing Exploration Progress:

Using attract mode and simple chaos monkey to get embeddings (5 minutes of play) and plot both datasets.

3 - Exploring a Game with RRT:

Using Rapidly-exploring Random Tree (RRT) to get data.

4 - Working with Human Data:

Turning bk2 files into screenshots and memory

5 - Training the Pix2Mem Model

Showing how to train a neural network using images and memory. Note that the dirs variable should be the path to the data folder containing a folder called screenshots and another folder called states. There should be respectively images and memory files in each folder. Run "Working with Human Data" for an example.
