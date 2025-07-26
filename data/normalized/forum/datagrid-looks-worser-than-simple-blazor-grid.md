# Datagrid looks worser than simple blazor grid

## Question

**Djo** asked on 11 Dec 2023

I made my first datagrid. I created very simple code just to get some data and to show it in the grid. Result is unacceptable. I attached a .png file to explain what I mean. Code looks like this: @page "/brorg" @using BezraSrv @using BezraSrv.Models <h3>Brorg</h3> <TelerikGrid Class="grid" Data=@bRORG Sortable="true" FilterMode="GridFilterMode.FilterMenu" ScrollMode="GridScrollMode.Virtual" Height="480px" RowHeight="60" PageSize="10" Size="@ThemeConstants.Grid.Size.Small"> <GridColumns> <GridColumn Field="@nameof(BezraSrv.Models.BRORG.ORGID)" Title="Org. id"></GridColumn> <GridColumn Field="@nameof(BezraSrv.Models.BRORG.NAZIV)" Title="Naziv"></GridColumn> </GridColumns> </TelerikGrid> <style> .width-100 { width: 100%; } .grid .k-grid-content tr { line-height: 32px; } </style> @code { [Inject] public DataService DataService { get; set; } protected IEnumerable<BezraSrv.Models.BRORG> bRORG; protected override async Task OnInitializedAsync() { bRORG=await DataService .GetBRORG(); } }

## Answer

**Djordje** answered on 12 Dec 2023

My bad. I missed to include "_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css"
