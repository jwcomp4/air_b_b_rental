# Using Git and GitHub

## Brief Overview

- We're going to use git and GitHub to serve as our version control throughout the process of developing our project. 
- Git allows us to efficiently track changes to the relevant files by tracking only the changes we make without making new complete copies every time we update or edit a file.
- GitHub will serve as our central place for collaborating on the various parts of the project. 
	- We will use remote repositories connected to the git repositories on our individual machines to streamline collaboration and teamwork.
- Branches will enable us to work individually on the various aspects of the project while protecting the integrity and functionality of our main/production branch.

## Overall Process for Using Git, GitHub, and Branches

- Steps for using git/GitHub
	1. Navigate to our GitHub repo and clone it to your machine using `git clone <repo URL>`
	[Air BnB Repo](https://github.com/jwcomp4/airbnb_rental)

	2. Note that this will put the most recent updates onto your machine, but every other time you must first pull from the GitHub repo to update files on your computer
		- Simply navigate to the apporpriate directory on your machine and use the `git pull` command in Terminal or Bash.

	3. Our GitHub has the following remote branches:
		- main
		- dashboard
		- database
		- github
		- machine_learning
		- presentation 

		* In order to work on one of those remote branches, you must create that branch on your local machine
		* Create the local branch by using the `git checkout -b <branch name>` in Terminal or Bash
		* This command both creates the branch on your machine and switches from the main branch to the new git branch.
		* After you have created branch and want to navigate to it later, use the `git checkout <branch name>` command in Terminal or Bash
		* To see a list of the branches on your machine and what branch you're currently using, use the `git branch` command in Terminal or Bash.

	4. After creating and switching to the appropriate branch, make the necessary changes to the code and save changes. 

	5. Follow the normal commands for staging, committing and pushing changes:
		- `git status`
		- `git add <file name>`
		- `git commit -m "commit message here."`
		- `git push`

		* note that the first time you use `git push` you may receive the following error: “Fatal: The current branch machine_learning has no upstream branch. To push the current branch and set the remote as upstream, use git push -- set-upstream origin <branch name>”

		* If you receive that error use the following command in Terminal or Bash: `git push -- set-upstream origin <branch name>`

	6. After pushing to the appropriate branch, we can review the code and merge into the main branch on GitHub.

	For a detailed tutorial on Git and GitHub refer to this Real Python article:

	[Git/GitHub Real Python](https://realpython.com/python-git-github-intro/)

	## GitHub Branch Merge Schedule


	- We will merge branches on Monday, Wednesday, and Friday at 8a Central Time.
	
		* John will review changes before merging.
		* If there are any issues, team members will be contacted via Slack to make any necessary edits.

	- Make sure to perform a `git pull` after each merge *before you start working on the project*