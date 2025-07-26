# Issue with virtual scrolling after migration Telerik.Blazor.UI to version 3.0

## Question

**Dan** asked on 31 Jan 2022

Hi, I've migrated my project to version 3.0 and I've issue with row virtualization. Before migration virtualization was working fine. Version 2.30 <TelerikGrid Data=@_items TotalCount=@_browseDataManager.TotalCount OnRead=@ReadItems PageSize="10" Height="100%" RowHeight="40" Pageable="false" Sortable="true" ScrollMode="GridScrollMode.Virtual"> <GridColumns> <GridColumn Field="@(nameof(UnitOfMeasureDTO.Code))" Title=@_localizer[ " Form_UnitOfMeasure_Code "] Width="100px" Locked="true" /> <GridColumn Field="@(nameof(UnitOfMeasureDTO.ShortName))" Width="200px" Title=@_localizer[ " Form_UnitOfMeasure_ShortName "] Locked="true" /> <GridCommandColumn Width="150px" Context="UnitOfMeasureCommands"> <GridCommandButton OnClick="@((args)=> Edit(args.Item as UnitOfMeasureDTO))" Icon="edit"> </GridCommandButton> <GridCommandButton OnClick="@((args)=> Delete(args.Item as UnitOfMeasureDTO))" Icon="delete"> </GridCommandButton> </GridCommandColumn> </GridColumns> <GridToolBar> <GridCommandButton OnClick="@(()=> Create())" Icon="add"> @_localizer["Title_Crud_Add"] </GridCommandButton> </GridToolBar> </TelerikGrid> protected async Task ReadItems ( GridReadEventArgs args ) {
_browseDataManager.CurrentSkip=args.Request.Skip;
_browseDataManager.CurrentPageSize=args.Request.PageSize; await GetDataAsync();
IsBusy=false;
} Version 3.0 I've noticed that parameter TotalCount has removed from grid control. <TelerikGrid Data=@_items OnRead=@ReadItems PageSize="10" Height="100%" RowHeight="40" Pageable="false" Sortable="true" ScrollMode="GridScrollMode.Virtual"> <GridColumns> <GridColumn Field="@(nameof(UnitOfMeasureDTO.Code))" Title=@_localizer[ " Form_UnitOfMeasure_Code "] Width="100px" Locked="true" /> <GridColumn Field="@(nameof(UnitOfMeasureDTO.ShortName))" Width="200px" Title=@_localizer[ " Form_UnitOfMeasure_ShortName "] Locked="true" /> <GridCommandColumn Width="150px" Context="UnitOfMeasureCommands"> <GridCommandButton OnClick="@((args)=> Edit(args.Item as UnitOfMeasureDTO))" Icon="edit" /> <GridCommandButton OnClick="@((args)=> Delete(args.Item as UnitOfMeasureDTO))" Icon="delete" /> </GridColumns> <GridToolBar> <GridCommandButton OnClick="@(()=> Create())" Icon="add"> @_localizer["Title_Crud_Add"] </GridCommandButton> </GridToolBar> </TelerikGrid> Error Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100]
Unhandled exception rendering component: Object reference not set to an instance of an object.
System.NullReferenceException: Object reference not set to an instance of an object.
at Telerik.Blazor.Components.Grid.GridRowCollection`1[[Hyperion365.Web.Shared.DTOs.UnitOfMeasureDTO, Hyperion365.Web.Shared, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]].BuildRenderTree(RenderTreeBuilder __builder)
at Microsoft.AspNetCore.Components.ComponentBase.<.ctor>b__6_0(RenderTreeBuilder builder)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment, Exception& renderFragmentException)

## Answer

**Daniel** answered on 31 Jan 2022

I've read breaking changes [https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/3-0-0](https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/3-0-0) I've added parameter TItem and removed Data. <TelerikGrid TItem="AnaliticDTO" OnRead=@ReadItems PageSize=@((int)_browseDataManager.CurrentPageSize) Height="@DataHeight" RowHeight="@DataRowHeight" Pageable=@DataPageable Sortable=@DataSortable ScrollMode="@DataGridScrollMode"> <GridColumns> <GridColumn Field="@(nameof(AnaliticDTO.Code))" Title=@_localizer[ " Form_Analitic_Code "] Width="100px" Locked="true" /> <GridColumn Field="@(nameof(AnaliticDTO.ShortName))" Width="200px" Title=@_localizer[ " Form_Analitic_ShortName "] Locked="true" /> </GridColumns> </TelerikGrid> protected async Task ReadItems ( GridReadEventArgs args ) {
CurrentSkip=args.Request.Skip;
CurrentPageSize=args.Request.PageSize;
CurrentSortDescriptor=args.Request.Sorts; await GetDataAsync(); args.Data=_items;
args.Total=_browseDataManager.TotalCount; IsBusy=false;
} Virtualization seems to be working after migration to 3.0.
