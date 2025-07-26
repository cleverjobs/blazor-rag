# TelerikGrid Programmatic Tooltips

## Question

**Jak** asked on 15 Apr 2024

I have a grid that is populated with data from my Database using a DTO and a controller and I have the tooltip working but my issue is that it is the same tooltip for each row in my grid and I can't quite figure out what to do. Here is my grid code, I thought me doing the render would fix it but it doesnt. Any ideas at all would be appreciated <TelerikGrid class="NewPairsGrid" Data="@Pairs" AutoGenerateColumns="false" RowHeight="15" Height="1000px" Pageable="true" PageSize="25" Sortable="true"> <GridColumns> <GridColumn Field="PairCreatedTimeStamp" Title="Token Age" width="75px"> <Template Context="dataItem"> @if (dataItem is EthPairTradeInfoVDto ethPairTradeInfoVDto)
{
var timestamp=CalculateElapsedTime(dataItem as EthPairTradeInfoVDto); <span class="tooltip-target"> @timestamp </span> <TelerikTooltip TargetSelector=".tooltip-target" Width="auto" Height="auto" Position="@TooltipPosition.Right"> <Template Context="tooltipContext"> <span> @RenderTooltipContent(ethPairTradeInfoVDto.PairCreatedTimeStamp) </span> </Template> </TelerikTooltip> </Template> </GridColumn> RenderFragment RenderTooltipContent(DateTime? pairCreatedTimeStamp)=>
builder=>
{
if (pairCreatedTimeStamp.HasValue)
{
builder.OpenElement(0, "span");
builder.AddContent(1, $"Pair Timestamp: {pairCreatedTimeStamp.Value}");
builder.CloseElement();
}
};
