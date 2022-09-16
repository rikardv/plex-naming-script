from genericpath import exists, isfile
import os
import shutil
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

# change this to your default plex media folder
destination_dir = '/Volumes/share/'

old_file_path = input(bcolors.OKBLUE + 'Enter path to the old file: ')
new_file_path = input(bcolors.OKBLUE + 'Enter path to plex media folder (press enter default): ')
if new_file_path:
    destination_dir = new_file_path
format = input(bcolors.OKBLUE + 'Enter format (avi, mkv etc): ')
title = input(bcolors.OKBLUE + 'Enter movie or tv-show title: ')
year = input(bcolors.OKBLUE + 'Enter year released: ')
is_tv_show = input(bcolors.OKBLUE + 'Is tv-show? (press enter for no): ')

# extra inputs
if is_tv_show:
    season = input(bcolors.OKCYAN + 'Enter season nr: ')
    episode = input(bcolors.OKCYAN + 'Enter episode nr: ')
    episode_title = input(bcolors.OKCYAN + 'Enter episode title: ')

first_directory = title + ' ' + '(' + year + ')'
path = os.path.join(destination_dir, first_directory)

if os.path.isdir(path):
    if not is_tv_show:
        print(bcolors.FAIL + "The folder '% s' already exists...", path)
        sys.exit()
else:
    os.mkdir(path)
    print(bcolors.OKGREEN + "Directory '% s' created" % path)

if is_tv_show:
    ## Example of output
    # TV Shows/Band of Brothers (2001)/Season 01/Band of Brothers (2001) - s01e01 - Currahee.mkv
    s_title = "Season "
    s_nr = ""
    epis_nr = ""
    if int(season) > 10:
        s_title += season
        s_nr = "s%s" % season
    else:
        s_title += "0%s" % season
        s_nr = "s0%s" % season

    if int(episode) > 10:
         epis_nr = "e%s" % episode
    else:
         epis_nr = "e0%s" % episode
        
    season_folder_path = os.path.join(path, s_title)
    if not os.path.isdir(season_folder_path):
        os.mkdir(season_folder_path)
        print(bcolors.OKGREEN + "Directory '% s' created" % season_folder_path)
    episode_file_name = "%s - %s%s - %s.%s" % (first_directory, s_nr, epis_nr, episode_title, format)
    final_tv_path = os.path.join("TV Shows", season_folder_path, episode_file_name)
    if os.path.isFile(final_tv_path):
       print(bcolors.FAIL + "The file '% s' already exists...", final_tv_path)
    
    print(bcolors.HEADER + "Moving file. Please wait...")
    shutil.move(old_file_path, final_tv_path)
    print(bcolors.OKGREEN + "Tv show file '% s' created" % final_tv_path)
    
else:
    ## Example of output
    # Movies/Avatar (2009)/Avatar (2009).mkv
    movie_file_name = "%s.%s" % (first_directory, format)
    final_movie_path = os.path.join("Movies", path, movie_file_name)
    if os.path.isfile(final_movie_path):
        print(bcolors.FAIL + "The file '% s' already exists...", final_movie_path)
        sys.exit()
    else:
        print(bcolors.HEADER + "Moving file. Please wait...")
        shutil.move(old_file_path, final_movie_path)
        print(bcolors.OKGREEN + "Movie file '% s' created" % final_movie_path)

