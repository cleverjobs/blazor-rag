# Completely remove hierarchy indicator

## Question

**Ric** asked on 14 Jun 2020

I searched and saw there was a thread on not showing the indicator if there were no children, is there a way to hide the indicator in ALL cases? I am not using the indicator to open/close the nested grids. What I am doing currently, is I have a checkbox in certain columns if the data in that column is really more than what the column can contain, so I make a nested grid for the additional data if they want to see more information. Because the checkbox is doing the event, the indicator is not needed.

## Answer

**Marin Bratanov** answered on 15 Jun 2020

Hi Rick, Perhaps using the RowTemplate will let you define all columns and the expanded state of the rows based on the checkbox and its model value - a similar example is available in the "Master-Detail View" section about halfway through this blog post: [https://www.telerik.com/blogs/why-blazor-grid-templates-will-make-you-question-everything.](https://www.telerik.com/blogs/why-blazor-grid-templates-will-make-you-question-everything.) Alternatively, you'd have to hide the first column of the grid with CSS, then use the Grid State to set the expanded hierarchy items, and this can become cumbersome, I think, especially when filtering and sorting come into play. Regards, Marin Bratanov
