# Grid, Virtual ScrollMode and Erratic Scrolling

## Question

**Joh** asked on 29 Oct 2023

I'm trying to figure out how to get smooth scrolling experience when virtul scroll mode is used. Some of the cells in my data can contain a couple, or over 100 words (or more), and when scrolling, the rows skip and jump in an obvious way, and it's not acceptable. I've tried to wrap my head around the RowHeight property without really understanding what it means. As each row in my data can be of different height, setting the proper RowHeight gets inpossible. What is the recommended solution in scenarios like mine? The users would like to see all the content of the cells. I coded up my own virtual scroll table in javascript some time ago, where I calculated the row height for each row, depending on the text content of the cells, and that made it possible to calculate the total virtual height of the table achieve smooth scroll. Is there a way to do the same for the TelerikGrid? I'd like to convert to Blazor and TelerikGrid, to get the benefits of sorting, filtering and all that. Using virtual scroll IS probably necessary because there can be hundreds of thousand rows, and the users would prefer to not using paging... Appreciate any tips here. Grid code: <TelerikGrid Data="@MyData" Size="@ThemeConstants.Grid.Size.Small" ScrollMode="GridScrollMode.Virtual" Sortable="true" FilterMode="@GridFilterMode.FilterRow" RowHeight="100" PageSize="50" Width="1000px" Height="600px"> <GridColumns> <GridColumn Title="#" Width="100px"> <Template> @{
var row=context as ExpandoObject;
var rowIndex=MyData.IndexOf(row) + 1;
}
@rowIndex </Template> </GridColumn> @{
foreach (var item in MyData.First())
{ <GridColumn Field="@item.Key" FieldType="@item.Value.GetType()" Title="@item.Key.Replace(" _ "," ")" Width="@(item.Key.EndsWith(" 3 ") ? " 300px ": " 75px ")"> </GridColumn> }

} </GridColumns> </TelerikGrid> Just a sample picture of sample data in a sample table:

## Answer

**Hristian Stefanov** answered on 01 Nov 2023

Hi Johan, I confirm that the Virtual Scrolling feature indeed relies on a fixed 'RowHeight' to function accurately and determine the appropriate set of items to retrieve from the data source. Therefore, when employing virtual scrolling, the recommended approach is to set the 'RowHeight' to a value that accommodates the longest text content you intend to display. However, if you wish to maintain a lower 'RowHeight' to avoid overly tall rows, especially in cases where certain cells contain an extensive amount of text, you have the option of displaying an ellipsis for the lengthier text. Subsequently, you can utilize our Tooltip component, for instance, to provide access to the complete text. Should you require additional information or further assistance, please do not hesitate to reach out. I would be glad to help. Regards, Hristian Stefanov Progress Telerik

### Response

**Johan** commented on 01 Nov 2023

I agree, my solution will be to only use virtual scroll if more than a certain amount of rows, and use an elipsis in virtual scrolls, with a tooltip or similar to display full cell content. Still, I know it is possible to get full virtual scroll with variable row height, because I've done it, so I wish it was at least tried, or that a template allowed for each row to set it's individual row height!

### Response

**Hristian Stefanov** commented on 06 Nov 2023

Hi Johan, I'm glad to hear that the ellipsis approach I suggested will work for you. Regarding the feasibility of implementing virtual scrolling with variable row heights, I want to clarify that it can be technically accomplished. Nevertheless, it's worth emphasizing that this approach, while feasible, isn't recommended because the new dimensions will cause issues with the scrolling logic. The optimal performance of the virtual scrolling functionality depends on fixed row heights and no dynamic calculations. For a more comprehensive understanding of this feature and its nuances, I encourage you to explore the " Notes " section in our Virtual Scrolling documentation. Kind Regards, Hristian
