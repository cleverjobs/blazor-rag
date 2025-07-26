# Grid custom sort with multiple grids

## Question

**Mic** asked on 10 Aug 2022

How do you identify which grid raised the OnRead event to be able to do custom sorting on a grid when there are more than one grid? For example, say I have multiple grids created in a loop Razor: @for (int i=0; i <_someData.Count(); i++)
{
int gridIndex=i; <TelerikGrid Data=@_someData.ElementAt(i) OnStateChanged="@((GridStateEventArgs<SomeData> args)=> OnGridStateChangedHandler(args))" OnRead="@OnGridRead" @ref="@GridRefList[gridIndex]".... } Code: @code {

TelerikGrid <SomeData> [] GridRefList { get; set; }

private async Task OnGridRead(GridReadEventArgs args)
{
// Which grid raised this event?
}
} How can I determine which grid fired the event so that I can load it with the correct data? All of the examples and links seem to only work with a single grid. Eg [https://www.telerik.com/forums/custom-sorting-and-filtering](https://www.telerik.com/forums/custom-sorting-and-filtering) [https://docs.telerik.com/blazor-ui/components/grid/manual-operations](https://docs.telerik.com/blazor-ui/components/grid/manual-operations)

### Response

**Dimo** commented on 12 Aug 2022

When using OnRead, the Grid expects you to set the new data to an event argument property ( args.Data ). From this point of view, there is no need to know the Grid instance and the correct Grid will always get the correct data. On the other hand, do not use OnRead together with Data with versions 3.0 and above. In case you need to know which Grid raised the event, due to some other app logic, then use a lambda, similar to how you are doing it with OnStateChanged. The lambda will allow you to pass extra parameters to the event handler.
