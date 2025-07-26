# Grid and SubGrids?

## Question

**Dea** asked on 27 Apr 2023

I have a main grid that can have 300+ rows. Within that each row can be expanded to a sub grid with say 100 rows. And then each row within that has 4 sub grids that can have 20-30 rows. I have it built and working but on large accounts this runs way too slow! Each grid has its own class and there are loops filling in each grid. I am looking for a faster way to load those grids. I am wonder if I could be pointed in the direction of an example that shows say how to load each sub grid on the fly when its parent grid is expanded. Thanks in advance. Deasun

### Response

**Deasun** commented on 27 Apr 2023

Ok got this working using sub razor pages connected to each other passing parameters. My current issue is the sub grids don't seem to be pushing the parent rows down far enough to see the children's details grids. See what I mean: the lineid 285422 has 4 children sub grids! only seeing the first one. How does one force it to show all the grids? Each grid atm has a size height of 400px.

### Response

**Dimo** commented on 28 Apr 2023

The browser's DOM inspector is your best friend in this case - there is some HTML element inside the <DetailTemplate>, which does not expand and clips the child Grids. See which is this element and what styles it has that prevent it from expanding (e.g. fixed height, etc.).

## Answer

**Deasun** answered on 09 May 2023

Fixed this using grid heights setting.
