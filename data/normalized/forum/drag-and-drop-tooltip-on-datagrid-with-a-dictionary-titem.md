# Drag and Drop tooltip on Datagrid with a dictionary TItem

## Question

**Mar** asked on 19 May 2025

Hi. I've got a TelerikGrid set up to use aTItem of Dictionary<string, int> (for example). I'm having an issue with the tooltip when I perform a row drag and drop in that the value shown is "null". I've attached a stripped down example of this, and its equivalent of where the Dictionary has been replaced with a class. We can't go down that route though as the data is dynamic in structure when supplied to the grid. Any help appreciated.

## Answer

**Nadezhda Tacheva** answered on 22 May 2025

Hi Mark, With the current configuration of the Grid using a Dictionary<string, int>, the Grid cannot actually read and process the items. The component is only able to render values in the cells as you are using Column Templates where you are specifying the content for the cells. If you remove the Templates, you may notice that the Grid cells are empty which indicates that the Grid cannot process the data. If you want to keep the current configuration with the Dictionary<string, int> you will also need a DragClueTemplate where you can specify the content to be rendered in the tooltip shown upon dragging. This feature, however, is not yet available - you may vote for it to increase its popularity and follow it to get status updates. As an alternative, I recommend altering the Grid data binding, so the component can process the data and you are able to perform data operations. See the following resources for reference: [https://www.telerik.com/blazor-ui/documentation/knowledge-base/grid-binding-to-expando-object](https://www.telerik.com/blazor-ui/documentation/knowledge-base/grid-binding-to-expando-object) - here you can check binding the Grid to ExpandoObject which may also work in your case. [https://demos.telerik.com/blazor-ui/grid/data-table](https://demos.telerik.com/blazor-ui/grid/data-table) - this demo shows binding to DataTable but the key point is that the data is reshaped, so the Grid works with a Dictionary<string, object> as TItem. Regards, Nadezhda Tacheva Progress Telerik
