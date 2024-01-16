# mizzou_spring_2024_nn
Neural networks class at the University of Missouri, Spring 2024

## Setup: Environment, Windows

### [Miniconda](https://docs.conda.io/en/latest/miniconda.html) Installation

**Miniconda** is the Anaconda (company) driven minimalistic conda installer for x86-like systems. Subsequent package installations come from the anaconda channels (default or otherwise).

[Download the 64 bit version](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)

This creates a base environment with numerous packages unlike Miniconda on other OS.

### Setup Environment

Open `Anaconda Prompt (Miniconda3)` using windows search and run the following:

```
conda create -n ci -y
conda activate ci
conda install pytorch torchvision cpuonly -c pytorch -y
conda install -c conda-forge matplotlib jupyter tqdm ipython pandas scikit-learn -y
```

## Setup: Environment, MacOS (M1)

### [Miniforge](https://github.com/conda-forge/miniforge) Installation

**Install [Homebrew](https://brew.sh)**

- Homebrew is a community package management repository for MacOS. Useful for installing popular packages via terminal interface. 

**Miniforge** is the community (conda-forge) driven minimalistic conda installer. It supports both ARM-like and x86-like systems, but has limited package selection (conda-forge channel only).

Open `Terminal` using spotlight search and run the following:

```
brew install wget
wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-MacOSX-arm64.sh .
zsh Mambaforge-MacOSX-arm64.sh
```

Additional Notes:
- Follow interactive terminal prompt for Miniforge installation, take the default paths. Allow to update the zsh config file.
- Update the shell environment via `source ~/.zshrc` or `source ~/.zsh_profile` depending on your setup. If you don't know, use the first command!

### Setup Environment

```
conda create -n ci -y
conda activate ci
conda install pytorch torchvision -y
conda install matplotlib jupyter tqdm ipython pandas scikit-learn -y
```

## Setup: NN Environment, Intel MacOS / Linux (e.g., Manjaro, Ubuntu, Fedora)

### [Miniconda](https://docs.conda.io/en/latest/miniconda.html) Installation

**Miniconda** is the Anaconda (company) driven minimalistic conda installer for x86-like systems. Subsequent package installations come from the anaconda channels (default or otherwise).

Grab the appropriate version of miniconda based on your system settings. 

For MACOS:

- Install **[Homebrew](https://brew.sh)**. Homebrew is a community package management repository for MacOS. Useful for installing popular packages via terminal interface.  
- Open `Terminal` using spotlight search and run the following:

```
brew install wget
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
zsh Miniconda3-latest-MacOSX-x86_64.sh
```

For Linux:
- Open terminal-like application and run the following:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
zsh Miniconda3-latest-Linux-x86_64.sh
```

Addtional Notes (MACOS and Linux):
- Follow interactive terminal prompt for Miniconda installation, take the default paths. Allow to update the zsh or bash config file.
- Update the shell environment: `source ~/.zshrc` or `source ~/.bashrc` depending on your setup. 
- `zsh` can be swapped with `bash` for commands above if you're using that shell.

### Setup Environment

Open terminal-like application and run the following:

```
conda create -n ci -y
conda activate ci
conda install pytorch torchvision cpuonly -c pytorch -y
conda install -c conda-forge matplotlib jupyter tqdm ipython pandas scikit-learn -y
```
