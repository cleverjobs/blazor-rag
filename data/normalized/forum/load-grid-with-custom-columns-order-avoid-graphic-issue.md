# Load grid with custom columns order: avoid graphic issue

## Question

**Cla** asked on 25 Jul 2022

My goal is to load grid with a custom column order, in razor the grid is defined with a default column order: <TelerikGrid @ref="Grid" Data="Data"> <GridColumns> <GridColumn Field="UserName" /> <GridColumn Field="Name" /> <GridColumn Field="Surname" /> </GridColumns> </TelerikGrid> but user can change it, and the change persist, so the next time it show the grid, it need to have the custom grid order saved from the user. I don't want to persist all the grid state, only the column order, so i solved this task allow grid to be Reorderable and saving to db the column order. To load the custom order i tried using the OnStateInit event, get the column state from GridState.ColumnStates and setting the Index property. This approach is described in documentation: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-column-in-custom-component-is-last?_ga=2.55826989.723302907.1658393190-1092710656.1653913029#solution](https://docs.telerik.com/blazor-ui/knowledge-base/grid-column-in-custom-component-is-last?_ga=2.55826989.723302907.1658393190-1092710656.1653913029#solution) [https://docs.telerik.com/blazor-ui/components/grid/state?_ga=2.260109709.1455456748.1658732515-1092710656.1653913029#information-in-the-grid-state](https://docs.telerik.com/blazor-ui/components/grid/state?_ga=2.260109709.1455456748.1658732515-1092710656.1653913029#information-in-the-grid-state) Unfortunally, in the OnStateInit event the property GridState.ColumnStates has no columns, so my solution is to change the column state in the OnAfterRenderAsync event, reading GridState.ColumnStates (this time column states are loaded) and setting the Index property. This workaround work well but cause a graphic flicker, as when the event is fired, the grid is rendered with the original column order, then is changed based on code settings to ColumnState.Index property. This is a sample code of this problem: [https://blazorrepl.telerik.com/GmaBwJYt15pTBs8J53](https://blazorrepl.telerik.com/GmaBwJYt15pTBs8J53) Now, how can i avoid this behaviour allow the grid to render directly with the custom column order? There is another event when i can change the ColumnState.Index property allow to render correctly? Thanks

## Answer

**Dimo** answered on 28 Jul 2022

Hello Claudio, The Grid OnStateInit event expects the app to set the desired state (or parts of it) from scratch, instead of modifying an existing state. You are not required to set the whole Grid state. You can only adjust the settings that you need, for example - private async Task OnGridStateInit ( GridStateEventArgs<MyGridModel> args ) {
args.GridState.ColumnStates=JsonSerializer.Deserialize<List<GridColumnState>>( MySavedColumnState );
} The above code assumes that you have saved only the column state somewhere. Alternatively, save the whole Grid state, restore (deserialize) it and use only parts of it. Regards, Dimo Progress Telerik
