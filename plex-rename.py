from genericpath import exists, isdir, isfile
import os
import shutil
import sys
import requests
import json


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


# change this to your default plex media folder
destination_dir = '/Volumes/share/'

# themoviedb api key
tv_api_key = ""

# omdb api key
movie_api_key = ""

# directory settings
old_file_path = input(bcolors.OKCYAN + 'Enter path to the old file: ')
new_file_path = input(
    bcolors.OKCYAN + 'Enter path to plex media folder (or leave empty for default): ')

if new_file_path:
    destination_dir = new_file_path

# format and tv-show/movie settings
format = input(bcolors.OKCYAN + 'Enter format (avi, mkv etc): ')
is_tv_show = input(bcolors.OKCYAN + 'Is tv-show? (leave empty for no): ')

if is_tv_show:
   # request for tv show data
    destination_dir = os.path.join(destination_dir, 'TV Shows')
    if not os.path.isdir(destination_dir):
        os.mkdir(destination_dir)
        print(bcolors.OKGREEN + "Directory '% s' created" % destination_dir)
    tv_search_string = input(bcolors.OKCYAN + "Enter tv show name: ")
    tmdb_request = requests.get(
        "https://api.themoviedb.org/3/search/tv?api_key=%s&language=en-US&page=1&query=%s&include_adult=false" % (tv_api_key, tv_search_string))
    tmdb_res = tmdb_request.text
    parse_json = json.loads(tmdb_res)
    if parse_json["results"]:
        tv_show_id = parse_json["results"][0]["id"]
        title = parse_json["results"][0]["name"]
        year = parse_json["results"][0]["first_air_date"].split("-", 1)[0]

    season = input(bcolors.OKCYAN + 'Enter season nr: ')
    episode = input(bcolors.OKCYAN + 'Enter episode nr: ')
    tmdb_details_request = requests.get(
        "https://api.themoviedb.org/3/tv/67557/season/%s/episode/%s?api_key=%s&language=en-US" % (season, episode, tv_api_key))
    tmdb_details_res = tmdb_details_request.text
    parse_tmbdb_details = json.loads(tmdb_details_res)
    episode_title = parse_tmbdb_details["name"]

else:
    # request for movie data
    destination_dir = os.path.join(destination_dir, "Movies")
    if not os.path.isdir(destination_dir):
        os.mkdir(destination_dir)
        print(bcolors.OKGREEN + "Directory '% s' created" % destination_dir)
    search_string = input(bcolors.OKCYAN + "Enter movie title")
    res_api = requests.get(
        "http://www.omdbapi.com/?apikey=%s&t=%s" % (movie_api_key, search_string))
    res_data = res_api.text
    parse_json = json.loads(res_data)
    if parse_json:
        title = parse_json["Title"]
        year = parse_json["Year"]


# Manually add
if not title or not year:
    title = input(bcolors.OKCYAN + 'Enter movie or tv-show title: ')
    year = input(bcolors.OKCYAN + 'Enter year released: ')

if not os.path.isdir(destination_dir):
    os.mkdir(destination_dir)

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
    # Example of output
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
    episode_file_name = "%s - %s%s - %s.%s" % (
        first_directory, s_nr, epis_nr, episode_title, format)
    final_tv_path = os.path.join(
        "TV Shows", season_folder_path, episode_file_name)
    if os.path.isfile(final_tv_path):
        print(bcolors.FAIL + "The file '% s' already exists...", final_tv_path)

    print(bcolors.HEADER + "Moving file. Please wait...")
    shutil.move(old_file_path, final_tv_path)
    print(bcolors.OKGREEN + "Tv show file '% s' created" % final_tv_path)

else:
    # Example of output
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
