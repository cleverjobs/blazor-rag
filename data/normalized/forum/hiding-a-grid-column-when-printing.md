# Hiding a Grid Column When Printing

## Question

**Sco** asked on 13 Jan 2021

I want to hide the GridCommandColumn when the user prints the page. What's the best way to handle it so the entire column does not display or take up any space?

## Answer

**Nadezhda Tacheva** answered on 14 Jan 2021

Hi Scott, The Grid Columns have Visible parameter which allows you to programmatically show/hide certain columns (including the Command column). You can use it to define which columns will be visible when printing. As example of such setup you can find in this project for printing Grid in our public repository. We are using the JS Interop to invoke the browser printing engine and some custom CSS to hide all the unnecessary elements on the page (since we only want to see and print the Grid). In the second example you will see a Grid with Command column that is hidden when printing. It is achieved by using a flag to indicate when the Grid is in print mode and then set the Visible parameter of the Command column depending on that flag. Regards, Nadezhda

### Response

**Scott** answered on 19 Jan 2021

We have this working but I do not think this is the optimal solution. I would like to make a feature request that we can use print style based CSS instead. Something like bootstrap does here: [https://getbootstrap.com/docs/4.1/utilities/display/#display-in-print](https://getbootstrap.com/docs/4.1/utilities/display/#display-in-print) Or being able to simply apply the bootstrap class to a column would work as well. For example: <GridCommandColumn Class="d-print-none"> ... </GridCommandColumn> What we are seeing, when the user closes the print dialog, the user interface is still in print mode until the page can re-render. We have applied a progress indicator, but using print based CSS would eliminate this need. Is it possible today to simple apply a CSS class to GridCommandColumn or a GridColumn?

### Response

**Nadezhda Tacheva** answered on 20 Jan 2021

Hi Scott, At the moment you can set a custom CSS class to a row or cell using the OnRowRender and OnCellRender events. They both receive event arguments that expose a Class field in which you can set your custom CSS class. However, since as per the Grid's structure the column headers and footer are separate elements, they will not be affected by the styling you apply to the rows/cells. Therefore, I also consider Class parameter for the columns will be a very useful feature to add as it will allow styling the column headers as well. We currently have an opened feature request for setting CSS class to the header cell of the column in our public

### Response

**Scott** answered on 20 Jan 2021

Thank you. I look forward to the new feature. That would also mean using the browser print method would work as well as a custom print button. What we are seeing, when the user closes the print dialog, the user interface is still in print mode until the page can re-render. FYI: It's not stuck in print mode, there is just a delay trying to change the UI back to the non-print view as the grid changes back. This is also happening on switching into print mode but it is hidden behind print preview. That is why I had to add a progress indicator.

### Response

**Nadezhda Tacheva** answered on 21 Jan 2021

Hi Scott, If you are experiencing a noticeable delay, another approach could be to take some steps towards performance improvement. A couple ways to achieve that are as follows: Activate Virtual scrolling - it is an alternative of the Pager that improves the performance by loading the data as the user scrolls. The Grid also provides virtual scrolling for columns as known as Virtualized columns. Reduce the page size - displaying less data on a page reduces the loading time and thus also speeds up the application performance. Regards, Nadezhda

### Response

**Scott** answered on 21 Jan 2021

Yes, we have the page size set to 100 which seems to be the sweet spot for our users. Our delay is about 1 - 3 seconds. I'll try virtual scrolling as well. Thanks
