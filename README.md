# The Sui developer newsletter repository

This repository contains the Sui developer newsletter data in Markdown format, as well as a couple of scripts that help us extract some data automatically.

# How to contribute content for the upcoming release

Community contributions are welcomed. Please submit a PR with the content you would like to add for the next release in the last `.md` file.  We'll do our best to keep this repository up-to-date and always have the next issue file ready for submissions, but if there is no newsletter file in the `bin` folder for the next release (check the date of the last `.md` file), please copy the last one, clean it up, and increment the integer in the filename.

We welcome content that is related to development on Sui such as apps, APIs, SDKs, tools, or other relevant content (e.g., technical blog posts, video tutorials, presentations, etc.) that might be of interest to developers building on Sui.

# Folder structure

* bin: is the folder where the newsletters will reside in .md files
* src: is the folder where the scripts and other any source code we need to automate different tasks

# Naming the newsletter

The simple idea I had was to simply name them incrementally: `sui-dev-newsletter-01.md`, `sui-dev-newsletter-02.md`, etc. This allows us to nicely switch from a weekly to a monthly or bi-weekly production, without needing to change the name. 
