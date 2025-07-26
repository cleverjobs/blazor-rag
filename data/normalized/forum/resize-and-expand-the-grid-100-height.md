# Resize and Expand the Grid 100% Height

## Question

**Gra** asked on 11 Dec 2019

This is an example of how it was done using Kendo UI - [http://dojo.telerik.com/EviNI](http://dojo.telerik.com/EviNI) Is there a way of doing the same with the Blazor grid?

## Answer

**Marin Bratanov** answered on 11 Dec 2019

Hi Graham, The underlying concept is the same - you need to have an HTML structure that provides the desired dimensions for the layout you are looking for. So, you should create a <div> element to hold the grid and have that element stretch to the desired size - whether CSS alone will suffice will depend on the layout and goal you have. Then, add a TelerikGrid in it and set its Height="100%". If you want to calculate dimensions dynamically, you can use JS Interop in a fashion similar to the example for responsive charts we have. The idea is that JS Interop will calculate the needed dimensions from the DOM and pass them along to the C# code - in this example a static class is used because it's easiest to call from JS Interop. Once you have the data in the view model, you can use it as a parameter value. Regards, Marin Bratanov

### Response

**Graham** answered on 12 Dec 2019

I have tried to adapt the Responsive Chart example but the Grid component does not have a Refresh() method. Is there another way of getting the grid to re-render after the window resizes? protected async Task ResizeChart() { // now that you know the size of the chart container changed, re-render the chart ChartRef.Refresh();

### Response

**Marin Bratanov** answered on 12 Dec 2019

Hello Graham, If you resize the div holding the grid, and the grid has Height="100%", the browser should re-render it without extra steps. If you want to set the grid height yourself, read the Height parameter from a field in the view model, and set that field from the event the JS Interop will raise. You may need to call StateHasChanged() at that point. The grid should not need such a Refresh method, it is specific to the charts. Regards, Marin Bratanov

### Response

**Shawn** answered on 12 Jun 2020

Can we get some example code that shows a Grid at 100%,100% and resizes as I resize the browser window?

### Response

**Marin Bratanov** answered on 13 Jun 2020

Hi Shawn, Another customer of ours made the following sample that shows one way to do this (an a few other things he uses): [https://github.com/telerik/blazor-ui/tree/master/grid/adjust-height-with-browser](https://github.com/telerik/blazor-ui/tree/master/grid/adjust-height-with-browser) Regards, Marin Bratanov
