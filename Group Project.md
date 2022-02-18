# Welcome to project Ergo
---

## Scenario

Your company is participating in a two-day hackathon promoted to study the energy mix of several countries. They send your group, the best team of Data Scientists in the company's roster. By analysing the energy mix of several countries, your company expects to contribute to the green transition by having a more savvy taskforce.

## Goal

For this project, we will be using data from [Our World in Data](https://ourworldindata.org/). The dataset can be found [here](https://github.com/owid/energy-data?country=).

Use whatever python tools you find apropriate. We recommend seaborn for plotting.

### Day 1, Phase 1

- [ ] One of you will create a gitlab repository (it does not matter who). __THE NAME OF THE REPOSITORY MUST BE "Group_XX" where XX is the number of your group! If you are group 3, then XX must be 03. Always use two digits!__
- [ ] Initialize the repo with a README.md file, a proper license, and a .gitignore for the programming language you will use.
- [ ] The one who created the repository will then give __Maintainer__ permissions to the rest of the group. Check under "Project Information" > "Members".
- [ ] Every element of the group clones the repository to their own laptops.

### Day 1, Phase 2

- [ ] The class you decide the create for the project has finally been named after a brief fight and is __PEP8 compliant, like the entire project__.

The class will have several methods, which you will __not__ develop in the master branch.  
Document everything!  
Make your calls compliant with __Static Type Checking__.

- [ ] One method will _download_ the data file into a __downloads/__ directory in the root directory of the project (main project directory). If the data file already exists, the method will not download it again.
- [ ] This method must also read the dataset into a pandas dataframe which is an attribute of your class. Consider only years after 1970, inclusively.

## Day 1, Phase 3

- [ ] Develop a second method that outputs a list of the available countries in the data set.
- [ ] Develop a third method that plots an area chart of the "\_consumption" columns. This method should have two arguments: a __country__ argument and a __normalize__ argument. The latter normalizes the consumption in relative terms: each year, consumption should always be 100%.
- [ ] The latter method should return a ValueError when the chosen country does not exist.
- [ ] Develop a fourth method that may receive a string with a country or a list of country strings. This method should compare the total of the "\_consumption" columns for each of the chosen countries and plot it, so a comparison can be made.
- [ ] Develop a fifth method that may receive a string with a country or a list of country strings. This method should compare the "gdp" column of each country over the years.
- [ ] Develop a sixth method that must be called __gapminder__. This is a reference to the famous [gapminder tools](https://www.gapminder.org/tools/#$chart-type=bubbles&url=v1). This method should receive an argument __year__ which must be an __int__. If the received argument is not an int, the method should raise a TypeError. This method should plot a scatter plot where __x__ is __gdp__, __y__ is __total energy consumption__, and the area of each dot is __population__. 

### Day 1, Phase 4

- [ ] Make a "showcase notebook" where you import your __Class__ and showcase all the methods you developed. Tell a story about your analysis and findings in the showcase notebook:

Let's begin by telling a story.

Start by an overall analysis with the gapminder plot for the most recent year and the year 1990. What can you see as the major changes?

Choose **three** countries in the list. Any countries will do, but at least one must be a member of the EU. The EU has a [carbon tax](https://ember-climate.org/data/carbon-price-viewer/), which means carbon emmissions have a cost. This will be useful for later on. 

Use your methods to analyse the evolution of each country's energy mix. Describe briefly what the evolution of the mix is, both totally and relatively.

Check GDP evolution for each country you selected. Make a brief analysis for each country.

Check GDP total energy consumption for each country you selected. Make a brief analysis for each country.

Finish day one with a short overall analysis between energy consumption, population, and GDP.

<div class="alert alert-danger">
    <b> REMEMBER: IT IS OK TO PROTOTYPE CODE IN NOTEBOOKS, BUT THE FINAL CLASS MUST BE IN A SINGLE .py FILE! </b>
    <br>
    <b> The final delivery of the project is the "showcase" notebook from Phase 4. Don't place this notebook together with prototyping notebooks.</b>
    <br>
    <b> Prototyping notebooks must have their own separate directory.</b>
    <br>
    <b> We will only consider contents in your "master" repository.</b>
</div>