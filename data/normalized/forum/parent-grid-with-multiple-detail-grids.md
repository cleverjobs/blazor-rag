# Parent grid with multiple detail grids?

## Question

**Dea** asked on 19 Jan 2023

Ok I have a need for the grid to do the following; Parent grid row Child grid 1 detail rows Child grid 2 detail rows Child grid 3 detail rows Parent grid has 1 set of columns. And each of the children grids have a different set of columns to each other. Hope that make sense. From your example doc: <TelerikGrid Data="salesTeamMembers"> <DetailTemplate> @{ var employee=context as MainModel; <TelerikGrid Data="employee.Orders" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="OrderId"></GridColumn> <GridColumn Field="DealSize"></GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate> <GridColumns> <GridColumn Field="Id"></GridColumn> <GridColumn Field="Name"></GridColumn> </GridColumns> </TelerikGrid> My understanding is; This is the parent data, <TelerikGrid Data="salesTeamMembers"> this would be the first child grid, <DetailTemplate> for a 2nd child grid would I just add another one of these tags, <DetailTemplate> lining it up to the public List <DetailsModel> Orders { get; set; } in the main model? something like: public class MainModel { public int Id { get; set; } public string Name { get; set; } public List <Child1DetailsModel> Orders { get; set; } public List <Child2DetailsModel> Orders { get; set; } } public class Child1DetailsModel { public int OrderId { get; set; } public double DealSize { get; set; } } public class Child2DetailsModel { public int RecID { get; set; } public double ItemValue { get; set; } }

### Response

**Deasun** commented on 24 Jan 2023

So I ended up with something like this: <TelerikGrid @ref="@gridLineDetails" Data="@GDLineDetails" AutoGenerateColumns="true" Pageable="true" Sortable="true" Class="custom-row-colors" FilterMode="@GridFilterMode.FilterRow"> <GridToolBar> <GridCommandButton Command="ExcelExport" Icon="file-excel">Export to Excel</GridCommandButton> <label class="k-checkbox-label"><TelerikCheckBox @bind-Value="@LineDetails_ExportAllPages" /> Export All Pages</label> </GridToolBar> <GridExport> <GridExcelExport FileName="@msExportFileName" AllPages="@LineDetails_ExportAllPages" OnBeforeExport="@LineDetails_OnBeforeExcelExport" /> </GridExport> <DetailTemplate Context="LineDetail"> @{ var Line=LineDetail as LineDetails; <TelerikGrid Data="Line.LinesRecurRev" AutoGenerateColumns="true" Pageable="true" Sortable="true" Class="custom-row-colors" FilterMode="@GridFilterMode.FilterRow"> </TelerikGrid> } </DetailTemplate> <DetailTemplate Context="LineDetail"> @{ var Line=LineDetail as LineDetails; <TelerikGrid Data="Line.UsageRev" AutoGenerateColumns="true" Pageable="true" Sortable="true" Class="custom-row-colors" FilterMode="@GridFilterMode.FilterRow"> </TelerikGrid> } </DetailTemplate> </TelerikGrid> And the Parent to the first child grid worked fine as expected. When I added in the 2nd DetailsTemplate it appears to have over written the first one. So I only get 1 detail child grid appearing the last one listed it seems. I need help get that 2nd one to appear too. { and I have 2 more child grids to go :) }

### Response

**Deasun** commented on 24 Jan 2023

Got it! Google search finally came up with the answer. 1 DetailTemplate, multiple grids within it. <DetailTemplate> @{ var user=context as MainModel; <TelerikGrid Data="user.Orders" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="OrderId"></GridColumn> <GridColumn Field="DealSize"></GridColumn> </GridColumns> </TelerikGrid> <hr /> <TelerikGrid Data="user.Addresses" Pageable="true" PageSize="5"> <GridColumns> <GridColumn Field="City"></GridColumn> <GridColumn Field="Street"></GridColumn> <GridColumn Field="Number"></GridColumn> </GridColumns> </TelerikGrid> } </DetailTemplate>

## Answer

**Deasun** answered on 24 Jan 2023

Answered it above!

### Response

**Deasun** commented on 24 Jan 2023

As a side note! Is it possible when exporting to excel it could export the children grids too?

### Response

**Yanislav** answered on 24 Jan 2023

Hello Deasun, I'm glad to hear you were able to find a solution and now the structure is as per the requirement. Including the child Grid in the exported file is possible. You can review the following example : [https://github.com/telerik/blazor-ui/tree/master/grid/export-to-xlsx-hierarchy](https://github.com/telerik/blazor-ui/tree/master/grid/export-to-xlsx-hierarchy) It demonstrates how you can include the child Grids in the exported excel document. The approach requires a custom implementation and is not supported out of the box. It is this way since the template can contain any HTML (which is not directly "translatable" to an Excel format). In our documentation, you can find more information about the Excel export specifics. I hope this helps. Regards, Yanislav
