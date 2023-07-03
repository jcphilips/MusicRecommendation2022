# Best Albums of 2022 Recommender

- [Best Albums of 2022 Recommender](#best-albums-of-2022-recommender)
  - [Introduction](#introduction)
  - [Usage](#usage)
  - [Limitations](#limitations)
  - [TODO](#todo)

## Introduction

This application uses [Pitchfork's The 50 Best Albums of 2022](https://pitchfork.com/features/lists-and-guides/best-albums-2022/) to recommend albums based on a genre a user selects.

**Disclaimer:** This project is in no way affiliated with Pitchfork. Data has been scraped from Pitchfork and that's about it. For full album reviews please check the Pitchfork website.

## Usage

1. Download the latest release file.
2. Unzip the file contents and navigate to the folder.
3. Open the terminal and change the working directory to the unzipped folder.
4. Type `python3 main.py` in the terminal window.
5. Enter a genre you would like to explore.
6. Select an album from that genre based on the list number.
7. Follow instructions on-screen to continue or quit the application.

## Limitations

- All album metadata is limited to data available on Pitchfork and, more specifically, data on [Pitchfork's The 50 Best Albums of 2022](https://pitchfork.com/features/lists-and-guides/best-albums-2022/). Hence album data is limited to those 50 albums.
- Searching is only possible between genres.
- Searching is currently directional and it is not possible to reverese from a selection.

## TODO

- [ ] Implement a frontend interface to improve UI/UX.
- [ ] Implement a feature to show similar albums based on genre.
- [ ] Expand album selection to all albums released since 2000.
- [ ] Add options to show artist profile.
- [ ] Add links to albums, reviews, etc. (This seems a bit extensive and time consuming.)
