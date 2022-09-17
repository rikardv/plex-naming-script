## Simple Python script to rename a file according to Plex naming convention

-The scanners of Plex will work best if content is seperated and named ***/Movies/MovieName (release year).ext*** or for TV-shows ***/TV Shows/ShowName/Season 02/ShowName – s02e17 – Optional_Info.ext***. This script will rename your file to this format and place them in the parent-folder (or create the folder if needed).

- Run with ```python3 plex-rename.py```

##### TV-show
```
/TV Shows
   /Band of Brothers (2001)
      /Season 01
         /Band of Brothers (2001) - s01e01 - Currahee.mkv
```

##### Movie
```
/Movies
   /Avatar (2009)
      Avatar (2009).mkv
   /Batman Begins (2005)
      Batman Begins (2005).mp4
      Batman Begins (2005).en.srt

```

##### TV Show example

```
Enter path to the old file: /Users/rikard/Downloads/uglyFile.mkv 
Enter path to plex media folder (or leave empty for default): /Users/rikard/PlexMediaFolder
Enter format (avi, mkv etc): mkv
Is tv-show? (leave empty for no): yes
Directory '/Users/rikard/PlexMediaFolder/TV Shows' created
Enter tv show name: the grand tour
Enter season nr: 4
Enter episode nr: 4
Directory '/Users/rikard/PlexMediaFolder/Tv Shows/The Grand Tour (2016)' created
Directory '/Users/rikard/PlexMediaFolder/Tv Shows/The Grand Tour (2016)/Season 04' created
Moving file. Please wait...
Tv show file '/Users/rikard/PlexMediaFolder/TV Shows/The Grand Tour (2016)/Season 04/The Grand Tour (2016) - s04e04 - Carnage a Trois.mkv' created
```