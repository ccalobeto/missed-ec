# sv

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

## Setup Python
Choose your python virtual environment in your VS Code placed in the botton. In my case `3.12.3('py312':conda)` and restart.

## Download CSV files
Go to [Ecuador datos abiertos](https://www.datosabiertos.gob.ec/dataset/personas-desaparecidas), download the excel files and convert them to csv files. Be careful with ',' for decimals in google sheets. Move the converted files to `static/data/input`.
Check support data cardinality if necessary.

# A quick preparation of bulk files
- Import xls files to google sheets and remove special characters (like "~", "'", ",").

- Prepare categories csv file, no accents and MAYUSC.  

- Rename columns.

## Executing scripts 
Run these scripts

To install your python libraries
```javascript
npm run python:dependencies
```

To load a csv file, clean and generate one cumulated csv file
```javascript
npm run data:generate
```

To generate a json file with all summaries for your svelte project
```javascript
npm run data:summary
```

## Template
- Go to [svelte-starter](https://github.com/the-pudding/svelte-starter) and  click **Use this template** button.

- Clone the repo and install dependencies.

- You are going to use `layercake` package so you need to turn of **runes**
in `svelte.congif.js`.

- Follow the commits as a project template of what to do. With this you can manage scrollytelling and charts.




