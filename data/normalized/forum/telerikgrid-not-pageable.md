# TelerikGrid not Pageable

## Question

**Jak** asked on 11 Apr 2024

I'm having trouble with my grid where I am unable to page through my results. I have 200 items in the grid and when I click on any of the buttons on the pager nothing happens. Here is my code Bonus points if someone can make me understand why my Tooltip isnt working either lol. <TelerikGrid class="NewPairsGrid" Data="@Pairs" AutoGenerateColumns="false" RowHeight="15" Height="1000px" Pageable="true" PageSize="25"> <GridColumns> <GridColumn Title="Pair Info" width="200px"> <Template Context="dataItem"> <div> @DisplayTokenImage(dataItem as EthPairTradeInfoVDto)
@($"{(dataItem as EthPairTradeInfoVDto).TokenSymbol} / {(dataItem as EthPairTradeInfoVDto).LpTokenSymbol} - {(dataItem as EthPairTradeInfoVDto).TokenName}") </div> </Template> </GridColumn> <GridColumn Title="Total Price ETH" width="150px"> <Template Context="dataItem"> <div> @FormatPrice(dataItem as EthPairTradeInfoVDto) </div> <div> @if (dataItem is EthPairTradeInfoVDto ethPairTradeInfoVDto)
{
var UsdPrice=ethPairTradeInfoVDto.CurrentPriceUsd.GetValueOrDefault();
@if (UsdPrice> 0)
{
@($"${UsdPrice} USD")
;
}
else
{
@("Looking for USD Price.../")
;
}
} </div> </Template> </GridColumn> <GridColumn Field="PairCreatedTimeStamp" Title="Token Age" width="75px"> <Template Context="dataItem"> @if (IsLessThanHour(dataItem as EthPairTradeInfoVDto))
{ <i class="fas fa-leaf"> </i> }
@if (dataItem is EthPairTradeInfoVDto ethPairTradeInfoVDto)
{
var timestamp=CalculateElapsedTime(dataItem as EthPairTradeInfoVDto); <span class="tooltip-target"> @timestamp </span> <TelerikTooltip TargetSelector=".tooltip-target" Width="250px" Height="150px" Position="@TooltipPosition.Right"> <Template Context="ttipContext"> <span> Timestamp: @(ttipContext.DataAttributes) </span> </Template> </TelerikTooltip> }
@* @CalculateElapsedTime(dataItem as EthPairTradeInfoVDto) *@</Template> </GridColumn> </GridColumns> </TelerikGrid>
