# Autofit not working

## Question

**Eri** asked on 21 Feb 2023

Hey, I have a grid with columns that are being generated dynamically on load based on a dynamic object. Everything is loading ok, but for some reason the AutoFitAllColumnsAsync doesn't seem to be working. I can't even resize the individual columns using the mouse. I am loading 117 pages (15 rows per page) of data, but the sorting works fine. Is there any reason you can think of that the resizing wouldn't work? Here is my grid code TelerikGrid @ref="@Grid"
Data="@GridData"
Pageable="true"
@bind-PageSize="@PageSize"
Sortable="true"
FilterMode="GridFilterMode.None"
Resizable="true"
Reorderable="true"
EditMode="GridEditMode.None"
Navigable="true"
Class="slim-grid-paddings"> <GridSettings> <GridPagerSettings InputType="PagerInputType.Input" PageSizes="@_appSettings.PageSizes" ButtonCount="5" Adaptive="true"> </GridPagerSettings> </GridSettings> <GridToolBarTemplate> <GridCommandButton Command="custom" Icon="@FontIcon.MaxWidth" Size="sm" OnClick="@(()=> Grid.AutoFitAllColumns())"> Auto-fit </GridCommandButton> <span class="k-toolbar-spacer"> </span> <GridCommandButton Command="ExcelExport" Icon="@FontIcon.FileExcel" Size="sm"> To Excel </GridCommandButton> <span title="Searches the items in the below grid." class="tooltip"> <GridSearchBox DebounceDelay="200" Placeholder="Search" Size="sm" Fields="@SearchFields"> </GridSearchBox> </span> </GridToolBarTemplate> <GridColumns> @if (GridData !=null && GridData.Any())
{
var firstItem=GridData.First();
var dictionaryItem=(IDictionary<string, object>)firstItem;

var fields=dictionaryItem.Keys;

foreach (var item in dictionaryItem)
{ <GridColumn Field="@item.Key" FieldType="@typeof(string)"> </GridColumn> }
} </GridColumns> </TelerikGrid>

## Answer

**Svetoslav Dimitrov** answered on 24 Feb 2023

Hi Eric, I have prepared a sample application where the Grid is bound to an ExpandoObject and the AutoFitAllColumnAsync method works as expected. You can see the demo app as an attached file. Can you check the application and compare it against your own and see if there are any differences that are causing the issue? If this does not help you move forward, modify the app and send it back to us so that the issue is reproducible. Regards, Svetoslav Dimitrov

### Response

**Eric** commented on 28 Feb 2023

So after a bunch of experimenting it looks like the problem happens if the grid is first initialize with a list of ExpandoObjects that has a null property value in it. It seems to handle the nulls after the first load, but if there is a null property anywhere in the object property value, it will error out for any of the more complex grid features. Sorting, Filtering, autofitting, etc.. I did see mention of this in one of the examples. Not sure if this should be considered a bug or not, but that is the problem. I would think it should at least show some kind of error to help people track it down.

### Response

**Tsvetomir** commented on 03 Mar 2023

Hi, Eric, Indeed, due to Blazor-specific limitations, the initial autofitting is not supported out-of-the-box. We do have a knowledge base article that shows how to use the auto fit on initial load: [https://docs.telerik.com/blazor-ui/components/grid/columns/resize#limitations](https://docs.telerik.com/blazor-ui/components/grid/columns/resize#limitations) Additionally, when binding the grid to a complex ExpandObject, the data operations such as filtering and sorting might not work automatically, as mentioned in the note here: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-binding-to-expando-object](https://docs.telerik.com/blazor-ui/knowledge-base/grid-binding-to-expando-object)
