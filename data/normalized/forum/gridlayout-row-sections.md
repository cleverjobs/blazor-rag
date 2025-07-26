# GridLayout row sections?

## Question

**Dea** asked on 31 Jan 2023

Ok I use a gridlayout for the page. I would like to put a border around some of the rows, for different logical sections. See the blue areas, thats where I would like to setup a border for each section. Not seeing a way to do that. Any ideas? Thanks See image:

## Answer

**Dimo** answered on 02 Feb 2023

Hi Deasun, The CSS Grid concept includes "cell" elements, but not "rows" or "columns". As a result, there is no suitable element to apply the border to. The desired appearance is possible only if you adjust the border styles of each "cell" and don't use gaps between the cells. ---------- ---------- ----------
| cell 1 cell 2 cell 3 |
---------- ---------- ---------- Regards, Dimo
