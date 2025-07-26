# DetailTemplate use all remaining space

## Question

**Nic** asked on 05 Jan 2021

Hello! I want to use the Grid ́s DetailTemplate to view another grid, let ́s call it detaildatagrid. Currently I have set the width of the detailsdatagrid to 65vw, because at 100% it will use two times of my monitor width and the horizontalscrolling is not working anymore. Is there a way to force the detaildatagrid to use the remaining seeable width? thank you & best regards Nico

## Answer

**Marin Bratanov** answered on 05 Jan 2021

Hello Nico, The DetailTemplate is just a row in the grid that has one <td> that spans all the data cells that "normal" rows have. Thus, setting the dimensions of the content inside is entirely up to you - using 100% width means that the content will be as wide as the row, and that is determined by the entire grid and the rest of its columns. If you have many columns and you don't want your content to be too wide, you could consider putting the details in a Window component that you show on a button click, instead of the DetailTemplate of the grid. Regards, Marin Bratanov
