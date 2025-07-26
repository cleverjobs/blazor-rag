# Alternate column color

## Question

**Ger** asked on 12 Feb 2021

Hi, How could I get alternate COLUMN colors? Note, not alternate ROW colors. In actual fact, I don't just want alternating column colors, I want column 1 and 2 to have the same color, 3 and 4 a different color, then 5 and 6 the same as 1 and 2 and so on. Also, I want a cell to be completely filled with the particular color so I figure I have to work on the <td> level. I thought I had it by hooking the OnCellRender event but my logic falls apart when you start clicking on the grid! None of the properties on the GridCellRenderEventArgs object tells you which column's cell is being rendered. The Item property contains the entire row context. Unfortunately the cell value does not contain any information either in my case to identify the column of it's index. Thanks, Gerhard

## Answer

**Eric R | Senior Technical Support Engineer** answered on 16 Feb 2021

Hi Gerhard, Thank you for the detailed description of the issue. I was able to reproduce the same behavior. The way around this is to use Lambda Expressions for the OnCellRender event. Let me provide more details and and an example for how to do this below. Explanation Using Lambda Expressions adds more flexibility to Event Handlers in Blazor. For example, instead of only passing the GridCellRenderEventArgs to the OnCellRender event, also include a columnNumber argument. Let me show what that would look like. Grid Markup OnCellRender with Lambda The highlighted event shows how to add an additional argument to the OnCellRenderHandler. <TelerikGrid Data=@Products> <GridColumns> <GridColumn Field="@(nameof(Product.ProductId))" Title="ID" Editable="false" OnCellRender="@((GridCellRenderEventArgs e)=> OnCellRenderHandler(e, 1))" /> <GridColumn Field="@(nameof(Product.ProductName))" Title="Name" OnCellRender="@((GridCellRenderEventArgs e)=> OnCellRenderHandler(e, 2))" /> <GridColumn Field="@(nameof(Product.UnitsInStock))" Title="Units In Stock" OnCellRender="@((GridCellRenderEventArgs e)=> OnCellRenderHandler(e, 3))" /> <GridColumn Field="@(nameof(Product.Discontinued))" Title="Available?" OnCellRender="@((GridCellRenderEventArgs e)=> OnCellRenderHandler(e, 4))" /> <GridColumn Field="@(nameof(Product.UnitPrice))" Title="Unit Price" OnCellRender="@((GridCellRenderEventArgs e)=> OnCellRenderHandler(e, 5))" /> </GridColumns> </TelerikGrid> Code for OnCellRender public void OnCellRenderHandler ( GridCellRenderEventArgs args, int columnNumber ) { if (columnNumber % 2==0 )
{
args.Class="EvenCellFormatting";
} else {
args.Class="OddCellFormatting";
}
} Styles for Alternating Columns <style>.OddCellFormatting { background-color: red; color: white; font-size: 10px;
}.EvenCellFormatting { background-color: blue; color: white; font-size: 10px;
} </style> Output Wrapping Up For additional reference, I have attached a page that illustrates the above approach that can be added to any project. Please let me know if you need any additional information. Thank you for using the Blazor Forums. Regards, Eric R | Senior Technical Support Engineer

### Response

**Gerhard** answered on 17 Feb 2021

Hi Eric, Thank you for your answer. This is almost what I need. But, you have given me the part that I needed to do what I want - a way to pass the column number to the event handler. Much appreciated. Regards, Gerhard
