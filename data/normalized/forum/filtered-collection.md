# Filtered collection

## Question

**Ric** asked on 19 Dec 2019

I am sure I am missing something but after filtering the grid, how do I get a list of the filtered items without having to loop through the grid or something?

## Answer

**Marin Bratanov** answered on 20 Dec 2019

Hi Rick, It is very rare that you can get the filtered data from a grid. Perhaps our jQuery grid is the only exception because its data source is an entirely separate component that does the actual filtering and data operations with the data and the grid uses it and just passes parameters to it. Perhaps you would be able to achieve this in Blazor when either (or both) of the following are implemented: state persistence so you can get the current filters the user has and apply them to your full data collection: [https://feedback.telerik.com/blazor/1414050-save-grid-layout](https://feedback.telerik.com/blazor/1414050-save-grid-layout) exporting because maybe it will provide an event where only the current grid data will be available so you can customize the export output (I cannot guarantee at this point whether that will happen, exporting in blazor is much different than other web suites we've had architecturally and it needs to be reviewed in detail first): [https://feedback.telerik.com/blazor/1431614-export-grid-to-excel](https://feedback.telerik.com/blazor/1431614-export-grid-to-excel) At the moment you can hook up the OnRead event to implement all operations with your own code and this will let you store the current filter settings so you can apply them. That said, what is the purpose of getting the filtered data from the grid? The grid's goal is to show it to the user and that's already available, and the only other use cases I can think of are exporting and state persistence. Am I missing something? Regards, Marin Bratanov

### Response

**Rick** answered on 20 Dec 2019

Yep, exporting is the exact reason. Would like to let uses filter and look at the data in the grid and if they want to do more with the filtered data, they can export just that.

### Response

**Marin Bratanov** answered on 20 Dec 2019

Hello Rick, In that case I suggest you Vote for and Follow the item about export - by default it should export the current filtered data of the grid, I imagine. If you come up with other scenarios or needs, especially after it gets implemented, you can open a new feature request. For the time being I'd encourage you to add any specifics you'd like to see from the export feature as a comment to its feature request so they can be considered when work starts. Regards, Marin Bratanov
