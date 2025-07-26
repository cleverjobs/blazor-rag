# Need grid footer navigation buttons to go by record instead of page

## Question

**Dou** asked on 30 Nov 2022

I have a grid with Pageable="false," and I need footer navigation buttons to work for each record; clicking "Next" or "Previous" would highlight the row below or above the currently highlighted row. Same goes for "First" and "Last." Any thoughts or recommendations would be appreciated.

## Answer

**Timothy J** answered on 30 Nov 2022

You're going to need to have your own custom button, not the implicit ones from the grids pager. Next, You're going want to look @Blazor Grid - Single Selection - Telerik UI for Blazor and implement single selection and use SelectedItems to affect the selected row.
