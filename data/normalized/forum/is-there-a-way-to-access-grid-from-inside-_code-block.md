# Is there a way to access grid from inside @code block?

## Question

**WeiWei** asked on 26 Nov 2019

once a grid is declared in markup, and for columns that are sortable, reorderable and resizable. I want to persist that settting from grid UI and later apply those settings back to grid, in @code section (some event handler handles save column setting, apply column settings)? this requires @code block to be able to access the grid object and the columns inside it. it is possible?

## Answer

**Wei** answered on 26 Nov 2019

I added @ref in grid markup and declared the grid in @code block. this.grid.GridColumns this returns renderFragment object, how do I get each column and its properties thanks

### Response

**Marin Bratanov** answered on 26 Nov 2019

Hello Wei, You can Follow the implementation of such a feature in the following page (I added your Vote for you): [https://feedback.telerik.com/blazor/1414050-save-grid-layout.](https://feedback.telerik.com/blazor/1414050-save-grid-layout.) It would require a lot of other things as base though, such as programmatic filtering, sorting and so on (also available in our Feedback Portal if you want to follow them - here, here, here, here ). The way to get information for columns is to define a view model with the data you want and use that to fill in the columns collection. A similar example is available in the following pages: in the following feature request my last post shows an example of a foreach loop to generate columns based on a view model, even if a rather simple one: [https://feedback.telerik.com/blazor/1434835-preserve-column-order-when-showing-hiding-columns-dynamically.](https://feedback.telerik.com/blazor/1434835-preserve-column-order-when-showing-hiding-columns-dynamically.) in this article for the tab strip, in the last example, tabs are created from a view model and you can use similar approach for the grid columns: [https://docs.telerik.com/blazor-ui/components/tabstrip/overview.](https://docs.telerik.com/blazor-ui/components/tabstrip/overview.) You can use this approach to apply settings to the grid when it initializes, but extracting that information is mostly unavailable at the moment. You could handle the OnRead event to implement all read operations yourself, and to store the DataSourceRequest object from which you could extract information about filter, sort and group state, but it would not be easy, and information about column sizes and orders is not available there. Regards, Marin Bratanov

### Response

**Wei** answered on 26 Nov 2019

Thanks for the answer, I think we will wait for Telerik team to expose the proper API for column setting read and apply to implement this function in our project.
