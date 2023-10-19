# The Sui developer newsletter repository

This repository contains the Sui developer newsletter data in Markdown format, as well as a couple of scripts that help us extract some data automatically. 

# Folder structure

* bin: is the folder where the newsletters will reside in .md file
* src: is the folder where the scripts and other any source code we need to automate different tasks

# Naming the newsletter

The simple idea I had was to simply name them incrementally: `sui-dev-newsletter-01.md`, `sui-dev-newsletter-02.md`, etc. This allows us to nicely switch from a weekly to a monthly or bi-weekly production, without needing to change the name. 

# How to contribute with data for the upcoming release

* if there is no newsletter file in the `bin` folder for the next release, please copy the last one and increment the integer in the filename. 
* submit a pull request with the text you'd want to add in the newsletter or directly commit to the repository

