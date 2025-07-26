# Allow delayed grid loading with OnRead handler

## Question

**Cla** asked on 03 Jul 2023

I have a grid loaded with the OnRead event handler to allow server paging. Now, in the component OnAfterRender event i read some grid settings with an async request to server and then i update the grid state with Grid.SetState. This approch work well but cause the grid to load twice: the first one by default OnRead call on component load, and the other one when the call to get settings complete and update the grid state. There is a way to delay the grid load, to be done only when i have read the grid settings, so only one load occurs? Thanks

## Answer

**Yanislav** answered on 06 Jul 2023

Hello Claudio, If I understand correctly, you're looking to delay the initial loading of data that occurs before loading the Grid properties (when the OnAfterRender event is executed). If that's the case, you can conditionally render the Grid and display a loading indicator until the properties are loaded. @if (ShouldRenderGrid)
{
<TelerikGrid TItem="SampleModel" OnRead="@OnGridRead"...
} else {
<div>Loading...</div>
}

<p> OnGridRead fired at: @LastOnRead </p>

@code { private List<SampleModel> GridData { get; set; } private bool ShouldRenderGrid { get; set; } protected override void OnAfterRender ( bool firstRender ) { if (firstRender)
{
LoadProperties();
ShouldRenderGrid=true;
}
} By implementing this approach, you can ensure that the Grid properties are loaded before rendering the Grid. Consequently, the OnRead event will be triggered once the properties are loaded. I hope this helps! Regards, Yanislav

### Response

**Claudio** answered on 10 Jul 2023

Hi Yanislav, the problem is caused by gridState.SetStateAsync method who raise a new grid load. even if i show the grid when i have all data available, i need to call SetStateAsync for applying it to the grid, for example to show the sort direction icon on column header: you can reply the issue with this sample: [https://blazorrepl.telerik.com/GnkhbEPo35292Wnm43](https://blazorrepl.telerik.com/GnkhbEPo35292Wnm43) In this sample the grid read count is 2, i want to have a single read Thanks

### Response

**Claudio** answered on 12 Jul 2023

I also tried to manage the problem using OnStateInit event. With this event i can set the order of columns (setting args.GridState.SortDescriptors=... ) but i can't set the columns Width or Index or Visible attributes because args.GridState.ColumnStates is an empty list, and adding new GridColumnState object does not allow to specify the GridColumnState.Field property. so i can use OnStateInit to set the filter / sort but i still have to use OnAfterRender -> Grid.SetStateAsync to set the columns Width / Index / Visible properties, but when i invoke Grid.SetStateAsync the grid raise the OnRead event... there is a solution who allow a single OnRead call?

### Response

**Yanislav** answered on 13 Jul 2023

Hello Claudio, In general, GridState contains information about the Grid options. However, the properties that can be changed are the ones meant for the end user to manipulate, such as sorting and filtering. The column settings are typically declared by the developer. Therefore, you can bind the Grid data, column fields, and column settings to properties and load them when the OnInitialized event is triggered. On the other hand, options that end users can modify, such as sorting, can be set when the OnStateInit handler is triggered. Please review the following REPL example, which demonstrates this approach: [https://blazorrepl.telerik.com/GnaLlREr57m4xaHG24](https://blazorrepl.telerik.com/GnaLlREr57m4xaHG24) Please review the example and let me know if this approach meets your requirement. Regards, Yanislav
