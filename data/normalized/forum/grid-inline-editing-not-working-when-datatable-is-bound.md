# Grid Inline Editing not working when datatable is bound

## Question

**Cip** asked on 25 May 2021

Hi everyone, I have binded a datatable to my grid and the Edit Mode was set to Inline. In an Editor template I have added for example TelerikNumericTextBox like this: <TelerikNumericTextBox Arrows="@false" Value="@((decimal)dataRow[col.ColumnName])" ValueChanged="@((decimal value)=> { OnDecimalCellValueChange(col.ColumnName, value); })" /> No when I want to edit the value this error appears System.InvalidOperationException: Telerik.Blazor.Components.TelerikTextBox requires a value for the 'ValueExpression' ValueExpression is provided automatically when using 'bind-Value'.See more at [https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression](https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression) I have read the details from that link but it doesn't seam to work, I don't have a model but a datatable binded to my grid. Is there in this situation a solution? Best regards, Cipri

## Answer

**Ciprian Daniel** answered on 27 May 2021

I've changed the implementation suggested here: [https://feedback.telerik.com/blazor/1418456-bind-to-datatable](https://feedback.telerik.com/blazor/1418456-bind-to-datatable) To this implementation: [https://demos.telerik.com/blazor-ui/grid/data-table](https://demos.telerik.com/blazor-ui/grid/data-table) And then I found the answer in this post: [https://www.telerik.com/forums/call-setstate-on-a-grid-that-has-an-onread-handler](https://www.telerik.com/forums/call-setstate-on-a-grid-that-has-an-onread-handler) It was an issue regarding the call of the method .SetState() followed by OnRead Thank you, Cipri
