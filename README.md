![Discord](https://img.shields.io/discord/938048651144626217?style=plastic) 
![PyPI - License](https://img.shields.io/pypi/l/pygears?style=plastic)

# PyGears DSP Library
PyGears library is Free and Open Sourced DSP library created for use in [PyGears](https://www.pygears.org) framework.

## Table of content
- [PyGears DSP Library](#pygears-dsp-library)
  - [Table of content](#table-of-content)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Directory structure](#directory-structure)
  - [Contributing](#contributing)
    - [How to make a clean pull request](#how-to-make-a-clean-pull-request)
    - [How to pick module you can work on](#how-to-pick-module-you-can-work-on)
  - [Comunity](#comunity)
  - [License](#license)
  - [Credits](#credits)

## Features


## Installation
- Pull the code from GitHub and enter the lib root directory 

```
git pull https://github.com/PyGears/lib-dsp.git
cd lib-dsp
```
- Recomendation is to use a contained python virtual envirnement 
```
# creates a virtual envirnement under folder 'venv' (any name can be used)
python -m venv venv 
# activates venv in the current console
source venv/bin/activate
```
- Instalation of the DSP package
```
pip install -e .
# alternativelly 
# pip3 install -e .

```
- all dependencies should be checked and installed
-  Trial if installation is succesfull and package is usable:

```
cd lib_dsp/fir/test

python test_fir_single.py
```

## Usage
 
- Each dsp lib is contained in it's own directory under lib_dsp
  -  __design__ folder should be all pygears code that describes desin and which can be imported in the lib 
  - __verif__ folder should cotain all additional python code that can be reused for integration testin and verification 
-  __/test__ folder whithin each dsp module should contain tests used for verifying model functionality
    -  pytest framework was used for regression testing  
    - recomendation to use Makefile to define exact commands used to test and verify each lib item
- For testing suypport a common pytest additional code was is provided under __lib_dsp/conftest.py__
  - apart from standard pytest features here are additions defined for the lib:
    - --cosim -> can be used in tests to enable cosimulation
    - --seed -> providing fixed seed 
    - --num -> defining number of runs per test (bu default seed is incrementing function)
    - --random -> provide random seed to each of the tests (can be used in combination with --num)
  - additional pytest options and fixtures can be added for each individual lib item under 
    - ``<gear_name>/test/conftest.py``
    - ``<gear_name>/test/pytest.ini``
## Directory structure
- dsp_lib `root folder`
  - dsp_lib `library with gears`
    - dsp_gear_1
      - dsp_gear_1 `one specific gear`
        - design `design of gear`
        - verif `verification files for gear`
      - doc `local documentation about gear`
      - test `test files for gear`
      - demo `demo/example how gear is used`
    - dsp_gear_2
      - dsp_gear_2
        - design
        - verif
      - doc
      - test
      - demo
    - dsp_gear_n
      - design
      - verif
      - doc
      - test
      - demo
  - doc `top lvl documentation (includes local documentation)`
  - other folders
  - [license](https://github.com/PyGears/lib-dsp/blob/main/LICENSE)
  - [readme](https://github.com/PyGears/lib-dsp/blob/main/README.md)
  

## Contributing
If you want to contribute to a project and make it better, your help is very welcome. Contributing is also a great way to learn more about social coding on Github, new technologies and and their ecosystems and how to make constructive, helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.

### How to make a clean pull request
Look for a project's contribution instructions. If there are any, follow them.

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from `develop` if it exists, else from `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them!
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's [interactive rebase](https://help.github.com/articles/interactive-rebase). Create a new branch if necessary.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's `develop` branch if there is one, else go for `master`!
- ...
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete your extra branch(es).

And last but not least: Always write your commit messages in the present tense. Your commit message should describe what the commit, when applied, does to the code – not what you did to the code.

### How to pick module you can work on
1. Go to file named [list_of_dsp_gears_for_implementation](list_of_dsp_gears_for_implementation.md)
2. Find module that is not assigned to anyone
3. Assign module to yourself
   - Edit [list_of_dsp_gears_for_implementation](list_of_dsp_gears_for_implementation.md) by changing [ ] into [X] at the beggining of dash
   - Assignyourself like [ssredojevic] (https://github.com/ssredojevic)
      - Just remove space between brackets so Markdown works as it should
4. Open pull request only of this edited file
5. Develop module
6. Open pull request of your code

## Comunity
- [Website](https://pygears.org/)
- [Discord](https://discord.com/invite/N499SsBMVD)
- [Stackoverflow](https://stackoverflow.com/questions/tagged/pygears)
- [YouTube](https://www.youtube.com/channel/UCJs_yMeLLw9jRf6vYFVRp9g)

## License
[MIT](https://github.com/PyGears/lib-dsp/blob/main/LICENSE) License

## Credits
