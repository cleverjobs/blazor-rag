# DataGrid row removal causes re-initialization of cell controls

## Question

**Jer** asked on 04 Dec 2023

Hi, I am trying to setup the ability for users to delete a row in a <TelerikGrid> <TelerikGrid
Data="@(Results)" EnableLoaderContainer="true" Pageable="true" Sortable="true" Resizable="true" FilterMode="GridFilterMode.FilterMenu" PageSize="15" SelectionMode="GridSelectionMode.Multiple" SortMode="@SortMode.Single" Height="70vh" @ref="@GridRef"> <GridColumn Title="Delete" Width="5vh">
<Template>
@if (context is MyModel model)
{
<div @key="@model.UniqueId">
<div class="icon-container" @onclick="@(()=> HandleDeleteClicked(model))">
<i class="far fa-trash font-icon-large"></i>
</div>
</div>
}
</Template>
</GridColumn> private async Task HandleDeleteClicked ( MyModel model ) {
Results.Remove(model);
} This part all works fine, it removes the row, and since 'Results' is an 'ObservableCollection<MyModel>' it updates the UI, perfect. The problem is I can't seem to get it so that every cell is not re-rendering/re-created when the delete happens. I have a column that has a sub-component inside it... <GridColumn Title="MyCustomColumn" Field="@nameof(MyModel.MyField)"> <Template> @{
@if (context is MyModel result)
{ <div @key="@result.UniqueId"> @{ <MyCustomComponent> </MyCustomComponent> } </div> }
} </Template> </GridColumn> 'MyCustomComponent' has an expensive API call in the 'OnParametersSetAsync' lifecycle method. Even though I have the @key attribute setup it seems to re-create the 'MyCustomComponent' for every row anytime a single row is deleted. This gets called for every row: // MyCustomComponent.razor.cs private Guid? ComponentInstanceId { get; set; } protected override Task OnInitializedAsync () {
ComponentInstanceId=Guid.NewGuid(); return base.OnInitializedAsync();
} The Id I am using for the key I can confirm is not changing. Is there a better way to help the grid know when it needs to re-create the cells? Thanks!

### Response

**Jeremy** commented on 04 Dec 2023

Follow-up I just realized that if I delete the very last row in the grid, the behavior is what I expect (no re-rendering/re-creating), so I'm wondering if this has to do with how the grid handles shifting the rows up when a item in the beginning/middle of the grid is removed?

## Answer

**Dimo** answered on 07 Dec 2023

Hello Jeremy, The last row is not the crucial one. The Grid will re-render the rows that come after the deleted one. Here is a test page, which shows this: [https://blazorrepl.telerik.com/cxlcYhFQ36tMvtq859](https://blazorrepl.telerik.com/cxlcYhFQ36tMvtq859) In general, the HTML re-rendering in our components is managed by the Blazor framework and its diffing algorithm. Our Grid implements some optimizations that prevent re-rendering when this is not necessary. However, these optimizations are not applied to column templates, because we can't know when and how they should re-render. So templates may refresh more often than regular cells. Regards, Dimo Progress Telerik
