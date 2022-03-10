# Welcome to project Ergo - Part 2
---
## Rules
1. To be delivered by 23:59 GMT March 17th.
2. The delivery is a git repo link sent by email. Remember: the pushes have a timestamp!

---
## Scenario (continuation)

Your company is participating in a two-day hackathon promoted to study the energy mix of several countries. They send your group, the best team of Data Scientists in the company's roster. By analysing the energy mix of several countries, your company expects to contribute to the green transition by having a more savvy taskforce.

You spent the first day doing a lot of the code heavy lifting. It is now time to do some polishing. As you know your project might be picked up for an analysis presentation, you add a very brief introduction about your group on the README.md file. Be sure to add your name and your e-mail. It is time to add more features to the class so you can present the analysis in the showcase notebook.

## Goal

For this project, we will be using data from [Our World in Data](https://ourworldindata.org/). The dataset can be found [here](https://github.com/owid/energy-data?country=).

Use whatever python tools you find apropriate. We recommend seaborn for plotting.

Day two is beginning.

### Day 2, Phase 1: Extending the scope

- [Done - Edwin] Convert your code so that the year of the read dataframe is the __index__ and is in __datetime__ format.
- [Done - Edwin Make sure you are not using aggregated "\_consumption" columns. It makes no sense in using "renewables_consumption" if you are already using "solar_consumption", for example. You did not notice this on day one (well, if you did, the real group, not the group from the scenario hackathon, congratulatios. Data Science is also about detail). Check [the data dictionary of the dataset](https://github.com/owid/energy-data/blob/master/owid-energy-codebook.csv) and make sure you are not using repeated columns.


<div class="alert alert-info"> 
    <br>
    <b>Always read a data dictionary before analyzing a new dataset!</b>   
    <br>
    <br>
</div>

## Day 2, Phase 2: Enrichment and Preditcions

Each energy source has a different type of emission. Coal emits a lot of C02 while renewables have less emissions. C02 emmissions are measured in __gC02eq/kWh__: grams of C02 equivalent produced per kilo Watt hour of energy produced. Since CO2 is not the only gas released, one must account for all the emissions of the different gases released. Methane, for instance, is 20 times more potent as a green house gas (GHG) than CO2, for the same mass of gass. The __gC02eq/kWh__ metric does not provide the whole picture, but it is a  good way to start the analysis.

According to a recent united [nations report](https://unece.org/sites/default/files/2021-10/LCA-2.pdf), emissions for each source are (we'll use average values):

| Energy source | Emissions in gC02eq/kWh |
|---|---|
| Biofuel | 1450 |
| Coal | 1000 |
| Gas | 455 |
| Hydro | 90 |
| Nuclear | 5.5 |
| Oil | 1200 |
| Solar | 53 |
| Wind | 14 |


- [ ] Enrich the dataframe with a column called __emissions__ which is the total C02 emissions in tonnes of C02. 1 tonne = 1e6 grams. 1 TWh = 1e9 kWh: One Tera Watt hour.
- [ ] Alter the __fourth__ method from part 1 to plot emissions [on the right axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html) with dashed lines and corresponding colors.
- [ ] Employ an algorithm from the __ARIMA__ family to make a __prediction method__. As input, this method should receive a country identifier and number of prediction periods. The number of predicted periods must be >=1 and an __int__, otherwise it should __raise__ an Exception. This method should plot, side by side, two graphs: one with the predicted consumption and another with the predicted emissions. Make sure you plot the prediction with a different color! Test this for countries you previously selected.
- [ ] Develop a final method that makes a scatter plot between __emissions__ and __consumption__ for all countries. The size of the dots should be population. It is OK if this works only for the most recent years.

### Day 2, Phase 3: Cleaning up

- [ ] Add a yaml file with all the packages you used, a conda environment file. This file will be used to generate an environment where your code will be ran.
- [ ] Use sphinx to generate a __docs__ directory that will shocase the documentation of your code. Remember to comment .gitignore appropriately so everything is included.

___
### Last time:

Let's begin by telling a story.

Start by an overall analysis with the gapminder plot for the most recent year and the year 1990. What can you see as the major changes?

Choose **three** countries in the list. Any countries will do, but at least one must be a member of the EU. The EU has a [carbon tax](https://ember-climate.org/data/carbon-price-viewer/), which means carbon emmissions have a cost. This will be useful for later on. 

Use your methods to analyse the evolution of each country's energy mix. Describe briefly what the evolution of the mix is, both totally and relatively.

Check GDP evolution for each country you selected. Make a brief analysis for each country.

Check GDP total energy consumption for each country you selected. Make a brief analysis for each country.

Finish day one with a short overall analysis between energy consumption, population, and GDP.

### Day two

Continue to tell your story. Showcase all your methods from day two.

What about emissions? Are they rising for the countries you selected? How will they look like in 5 years (five years after the dataset ends, not from today)?

What about consumption? Is it rising for the countries you selected? How will it look like in 5 years?

What can you make of the relationship between __consumption__ and __emissions__?

Write a short analysis of what you learned from the analysis of the data. What would your recomendation to decarbonise be?

---
## Grading

Between the two parts, there are 20 gradable items in both Part 1 and 2. The last two items of Day 1, Phase 1 are not gradable. Each other item is worth 1/20.

<div class="alert alert-danger">
    <b> REMEMBER: IT IS OK TO PROTOTYPE CODE IN NOTEBOOKS, BUT THE FINAL CLASS MUST BE IN A SINGLE .py FILE! </b>
    <br>
    <b> The final delivery of the project is the "showcase" notebook. Don't place this notebook together with prototyping notebooks.</b>
    <br>
    <b> Prototyping notebooks must have their own separate directory.</b>
    <br>
    <b> We will only consider contents in your "master" repository before the end of the deadline.</b>
</div>
