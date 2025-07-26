# How to Excel Export multiple grids to the same file using worksheets

## Question

**Enz** asked on 03 Feb 2022

Hello, How can we export multiple telerikgrids to the same excel file ? When using the built-in export it's easy to get one file per grid, but is there any way (maybe using the MemoryStream) to merge those files together into one file with multiple worksheets ?

## Answer

**Matthias** answered on 04 Feb 2022

Hi Enzo, one possibility is to change the following example. I also use a customized variant of it. Telerik-Example This gives you more control - but the columns should be present in all workbooks. Alternatively, you can use the standard method, save it on the server and then load and merge it with Telerik Spread Processing. best regards
