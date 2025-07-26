# Dropdowns within column template

## Question

**Ric** asked on 12 Nov 2020

What is the best way to handle dropdowns sitting in a grid within a column template? @bind-Value doesn't work well because it sets the selected value of every dropdown in the grid. I want to be able to send the class object from the current row in the grid to a method on dropdown change, and also know what the new value is of the dropdown.

## Answer

**Marin Bratanov** answered on 13 Nov 2020

Hello Rick, The dropdowns are editors and generally belong in the editor template so changes to the model values can be handled in the standard way. If you do want to keep them in the column template, you should ensure you bind the Value to the current row model and not to a generic field in the view-model shared among all instances use a lambda expression in their OnChange handler to pass the current row model so that you know which instance to update use the OnChange handler to update your actual database Regards, Marin Bratanov

### Response

**Rick** answered on 13 Nov 2020

Thanks Marin, I came to the same conclusion this morning and was able to get it to work that way. I would have preferred letting the user just scan down the grid and flip a dropdown and reset something about the row without having to click edit first but no big deal, it works. Thanks!

### Response

**Marin Bratanov** answered on 13 Nov 2020

Hi Rick, You could use the dropdown in the cell template, just make sure to bind to the correct value from the row, and to update the data source correctly. Regards, Marin Bratanov
