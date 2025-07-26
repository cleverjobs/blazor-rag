# Chart within a TileLayout does not resize when resizing the tile item

## Question

**Rom** asked on 13 Jan 2023

Hi there, I'm facing a problem with charts in a tile layout. I have a TileLayout in my applicaton and added some charts (which are in another component) to it. I checked the documentation about TileLayout and resizing so I followed those steps. Please check out my code: Razor MainPage: <TelerikTileLayout Columns="5" ColumnWidth="300px" Reorderable="true" Resizable="true" OnResize="TileItemResize"> <TileLayoutItems> <TileLayoutItem HeaderText="My Item Text" RowSpan="2"> <Content> <TurnoverComparisonWidget @ref="TurnoverComparisonRef" SelectedWidget="widget" IsLoad="true"> </TurnoverComparisonWidget> </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> Razor TurnoverComparisonWidget: <TelerikChart @ref="ChartRef" Height="100%"> <ChartTooltip Visible="true"> </ChartTooltip> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Data="ChartData" Field="@nameof(ChartDataItem.Value)" CategoryField="@nameof(ChartDataItem.CategoryName)"> <ChartSeriesLabels Visible="true" Format="{0:C2}"> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> </TelerikChart> C# MainPage: public TurnoverComparisonWidget TurnoverComparisonRef { get; set; } private void TileItemResize ( ) {
TurnoverComparisonRef.Refresh();
} C# TurnoverComparisonWidget: public TelerikChart ChartRef { get; set; } public void Refresh ( ) {
ChartRef.Refresh();
} But the chart is not resizing when I resize the tile layout item. It just stays the same size and never changes. Did I forget anything? I can't figure it out. Best Regards, Roman

## Answer

**Yanislav** answered on 18 Jan 2023

Hi Roman, I've reviewed the code snippets you've shared and everything seems fine to me. I've tried to reproduce the problem in a REPL example and everything seems to be working correctly. The Chart is refreshed when the tile is resized. Can you spot something different in the scenario you have? In order to further assist you, may I ask you to prepare an example or modify the REPL sample I've shared above, so the unexpected behavior is reproducible and send it back to me for further review? This way, I will be able to observe the issue and provide further guidance on handling the case. Thank you in advance! Regards, Yanislav
