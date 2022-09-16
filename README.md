## Simple Python script to rename a file according to Plex naming convention

The scanners of Plex will work best if content is seperated and named ***MovieName (release year).ext*** or ***/TV Shows/ShowName/Season 02/ShowName – s02e17 – Optional_Info.ext***. This script will rename a file to this format and place them in the parent-folder (or create the folder if needed).

##### TV-show
```
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

##### Movie Example

```
Enter path to plex media folder (or leavy empty for default): plex/media
Enter path to the old file: projects/movies/uglyname.mkv
Enter format (avi, mkv etc): mkv
Enter movie or tv-show title: Avatar
Enter year released: 2009
Is tv-show? (leave empty for no): 

Directory 'plex/media/Avatar (2009)' created
Movie file 'plex/media/Avatar (2009)/Avatar (2009).mkv' created
```