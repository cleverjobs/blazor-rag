# How to TAB key through grid for Accessibility

## Question

**Chr** asked on 21 Nov 2023

I'm trying to figure out how/if you can tab through a grid. What I mean by that is my Grid has a header row with a checkbox. If the focus is there and I hit tab, it goes out to the browser controls and I can't focus on a row or the pagination controls using the keyboard. I have row-click enabled so I assume the user should be able to tab to a row and use Enter to simulate a click. Or tab down to the pagination controls and select another page. Here's how it works now after the page first loads, I hit tab and it selects the hamburger (Telerik menu) in the top-right corner (which I can't activate with the keyboard!), next it moves to the checkbox in the grid header and the third tab goes to the browser controls starting with the magnifying glass. I can't find anything in the documentation that talks about tab order so I'm stuck. Please point me at anything that defines how the tab order is setup for a grid. Here is my grid code in case it helps. <TelerikGrid Data="@RequestList" Pageable="true" @bind-PageSize="@PageSize" @bind-Page="@CurrentPage" Resizable="true" Sortable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu " OnRowClick="@OpenRequestDetailAsync" OnStateChanged="@((GridStateEventArgs<RequestDTO> args)=> GridStateChanged(args))" OnStateInit="@((GridStateEventArgs<RequestDTO> args)=> InitGridState(args))"> <GridToolBarTemplate> <TelerikCheckBox TabIndex="1" Id="chkPeriodFilter" OnChange="GetAllRequets" @bind-Value="FilterForPeriod"> </TelerikCheckBox> <label for="chkPeriodFilter"> View all requests </label> </GridToolBarTemplate> <GridSettings> <GridPagerSettings InputType="PagerInputType.Input" PageSizes="@PageSizes" ButtonCount="5" Adaptive="true" Position="PagerPosition.Bottom"> </GridPagerSettings> </GridSettings> <GridColumns> <GridColumn Field="ChangePeriodId" Width="5%" Visible="false" Title="ChangePeriodId" OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" vertical-aligned-cell " )" /> <GridColumn Field="RequestId" Width="5%" Title="ID" OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" vertical-aligned-cell " )" /> <GridColumn Field="SubmitDate" Width="9%" title="Requested Date" DisplayFormat="{0:MMM dd yyyy}" Sortable=true OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" vertical-aligned-cell " )" /> <GridColumn Field="SubmitUser" Width="15%" title="Requested By" Sortable=true OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" vertical-aligned-cell " )" /> <GridColumn Field="CurrentStatus" Width="9%" Title="Status" Sortable=true OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" vertical-aligned-cell " )"> <FilterMenuTemplate> @foreach(var status in RequestList.DistinctBy(x=> x.CurrentStatus).Select(x=> x.CurrentStatus))
{ <div> <TelerikCheckBox Value="@(IsCheckboxInCurrentFilter(context.FilterDescriptor, status.ToString()))" TValue="bool" ValueChanged="@((value)=> FilterStatus(value, status.ToString(), context))" Id="@($" status_ { status }")"> </TelerikCheckBox> <label for="@($" status_ { status }")"> @if (status==null)
{ <text> Empty </text> }
else
{
@status
} </label> </div> } </FilterMenuTemplate> </GridColumn> <GridColumn Field="RequestTypeName" Width="5%" Title="Type" Sortable="true" OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" vertical-aligned-cell " )"> <FilterMenuTemplate> @foreach(var status in RequestList.DistinctBy(x=> x.RequestTypeName).Select(x=> x.RequestTypeName))
{ <div> <TelerikCheckBox Value="@(IsCheckboxInCurrentFilter(context.FilterDescriptor, status.ToString()))" TValue="bool" ValueChanged="@((value)=> FilterType(value, status.ToString(), context))" Id="@($" status_ { status }")"> </TelerikCheckBox> <label for="@($" status_ { status }")"> @if (status==null) // part of handling nulls - show meaningful text for the end user
{ <text> Empty </text> }
else
{
@status
} </label> </div> } </FilterMenuTemplate> </GridColumn> <GridColumn Field="@(nameof(RequestDTO.Change))" Title="Change Description" OnCellRender="@( (GridCellRenderEventArgs e)=> e.Class=" vertical-aligned-cell " )"> <Template> @(new MarkupString((context as RequestDTO).Change)) </Template> </GridColumn> </GridColumns> </TelerikGrid>

## Answer

**Georgi** answered on 24 Nov 2023

Hello, Chris, Thank you for the provided image and code snippet! By design, the Grid has a Navigable property that enables keyboard navigation. I can see the property is missing from your Grid configuration. As for tab order, it follows the horizontal and vertical flow of the page. For example, left-to-right and top-to-bottom, header first followed by the main and, then, page navigation. For more complex components like the Grid, you can use the Arrow keys to walk through the inside elements like the Grid Cells. Note the Tab key can not be used to traverse the Grid cells, except during in-cell or inline editing. Lastly, there is a feature request that will allow you to customize the keyboard shortcuts, for example, the Tab key behaviour. If you are interested, you can vote for the item in our feedback portal, as this helps us prioritize based on community feedback. Additionally, you can follow the item to get notified of any status changes. Kind regards, Georgi Progress Telerik

### Response

**Chris** commented on 25 Nov 2023

The Navigatable property solved the issue. Thanks for that and the extended explanation.
