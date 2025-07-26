# Dynamically enabling PageSize Sortable FilterMode Not working

## Question

**Way** asked on 05 Nov 2021

Upon sending the values to the attributes for the TelerikGrid the UI part of them displays, but I noticed even though I send default 5 for the pagesize it loads the full list regardless. The Sortable columns on the grid has the icon, but when clicking it actually doesn't trigger off anything. Filter shows up the icon, but when i click it nothing happens. Just to make the paging in footer of the grid show up for dropdownlist to select row size i had to upgrade to 2.28 to make it work with GridPagerSettings. I am sure someone else has experience this, can any assistance happen here. below is what i have in the component. <TelerikGrid @ref="grid" Data="@Rows" Class="@GetCssClasses()" OnRowClick="@HandleRowClick" Pageable="@HasPages" PageSize="@RowsPerPage" TotalCount="@TotalRowCount" Sortable="@IsSort" FilterMode="GridFilterMode.FilterMenu" OnRead="@HandleDataRequest" ScrollMode="@scrollMode" @bind-Page="@CurrentPage" Height="100%" RowHeight="54" SelectionMode="@SelectionMode" SelectedItemsChanged="((IEnumerable<Row> rows)=> HandleMultiSelect(rows))" OnRowRender="@((args)=> OnRowRender(args))"> <GridSettings> <GridPagerSettings InputType="PagerInputType.Buttons" PageSizes="@PageSizesList" ButtonCount="3" /> </GridSettings> <GridColumns> <CascadingValue Name="Table" Value="@this">@Columns</CascadingValue> </GridColumns> </TelerikGrid>

## Answer

**Hristian Stefanov** answered on 09 Nov 2021

Hi, I noticed that the provided code snippet has the PageSize parameter together with GridPagerSettings PageSizes. In this case, the Grid applies only the PageSize parameter, and not the selected page size from the PageSizes list. This is expected because the PageSize parameter in Grid with a GridPagerSetting PageSizes requires handling of the PageSizeChanged event. That being said, another approach to achieve the desired functionality is to use " @bind-PageSize="@RowsPerPage"" in the Grid syntax instead of " PageSize="@RowsPerPage". Additionally, sorting and filtering are internal operations. When the OnRead event is used, the internal operations are disabled, and you need to perform them all in the OnRead event. For more information about the OnRead event specifics, you can refer to our documentation for manual operations - Manual DataSource Operations. Regards, Hristian Stefanov Progress Telerik
