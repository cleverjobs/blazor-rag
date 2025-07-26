# Blazor Data Grid - Change data source for selected items

## Question

**Evg** asked on 21 Dec 2021

I have a grid that takes live data (like connection status of an item) from a specific endpoint of a controller. I want to take those live data only for selected items in the grid without changing grid' s columns. I mean that i want to change data source in the grid only for selected items. Is there an example of something like this? Thank you

### Response

**Evgenia** commented on 21 Dec 2021

It is a Blazor Web Assembly project

## Answer

**Dimo** answered on 23 Dec 2021

Hi Evgenia, It is possible to update a specific Grid row - there is no need to reload all items. You just need to find the row in the Grid's Data collection and change its values. Here is a simple example that shows two different ways to do it. Make sure to get familiar with these resources as well: Documentation: Refresh Grid Data Knowledge Base: Force a Grid to Refresh @using System.ComponentModel.DataAnnotations

<p>Select a row:</p>

<TelerikGrid Data="@GridData" SelectionMode="GridSelectionMode.Single" @bind -SelectedItems="@SelectedRows" Width="400px">
<GridColumns>
<GridColumn Field="@nameof(GridModel.Text)" />
</GridColumns>
</TelerikGrid> @if (SelectedRows.Any())
{
<p>Update it via the form...</p>

<TelerikForm Model="@SelectedRows.FirstOrDefault()" Orientation="FormOrientation.Horizontal" Width="400px" OnValidSubmit="@RefreshGrid">
<FormValidation>
<DataAnnotationsValidator />
</FormValidation>
<FormItems>
<FormItem Field="@nameof(GridModel.Text)" />
</FormItems>
</TelerikForm>

<p>... or via this button:</p>

<TelerikButton OnClick="@UpdateRow">Update Selected Row</TelerikButton>
} @code {
List<GridModel> GridData { get; set; }=new List<GridModel>();

IEnumerable<GridModel> SelectedRows { get; set; }=new List<GridModel>(); void RefreshGrid()
{ var index=GridData.FindIndex( x=> x.ID==SelectedRows.FirstOrDefault().ID);

GridData[index]=SelectedRows.FirstOrDefault(); // not necessary here //GridData=new List<GridModel>(GridData); } void UpdateRow()
{ var index=GridData.FindIndex( x=> x.ID==SelectedRows.FirstOrDefault().ID);

GridData[index].Text="Row updated: " + DateTime.Now.ToLongTimeString(); // refresh Grid Data instance GridData=new List<GridModel>(GridData);
} protected override void OnInitialized()
{ for (int i=1; i <=5; i++)
{
GridData.Add( new GridModel() { ID=i, Text="Text " + i.ToString() });
}
} public class GridModel
{ public long ID { get; set; }

[Required] public string Text { get; set; }
}
} Regards, Dimo
