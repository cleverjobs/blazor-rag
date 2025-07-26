# TelerikChart format days not working for da-DK culture

## Question

**Mar** asked on 11 Feb 2022

*** UPDATE If I remove the set culture code, then it works ** Adding Format="{0:d}" to this code Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor. works fine. If I try to do the same I get this: First Format="{0}" Using Format="{0:d}" I get this. Same when I use any other formats like Format="{0:yyyy.MM.dd}" When not using any kind of format. Not good enough. Missing the year <TelerikChart RenderAs="RenderingMode.Canvas"> <ChartTitle Text="Prices" /> <ChartTooltip Visible="true" /> <ChartLegend Position="ChartLegendPosition.Bottom" /> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="" Data="@Details.PriceGraphs" DashType="@DashType.Solid" CategoryField="@nameof(InstrumentPriceGraph.UpdateDate)" Field="@nameof(InstrumentPriceGraph.Price)"> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Min="@_yMinValue" Max="@_yMaxValue" /> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Type="ChartCategoryAxisType.Date" BaseUnit="ChartCategoryAxisBaseUnit.Days"> <ChartCategoryAxisLabels Step="2" Format="{0:d}"> <ChartCategoryAxisLabelsRotation Angle="-45" /> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart> Setting the culture in Blazor wasm Program.cs var culture=new CultureInfo( "da-DK" );
culture.DateTimeFormat.ShortDatePattern="dd-MM-yyyy";
CultureInfo.DefaultThreadCurrentCulture=culture;
CultureInfo.DefaultThreadCurrentUICulture=culture;

### Response

**Hristian Stefanov** commented on 16 Feb 2022

Hi Martin, Let's cover the three mentioned formats below and the missing year without using a format. I'm ready to share my observations as I tested the described scenario. Format - {0} The result from this format is expected even without setting a culture in the app. This is the way the {0} format is presented with the current Chart setup here. Format - {0:d}, {0:yyyy.MM.dd} I tested these formats in an app with a culture set in the Program.cs file as required. As a result, the formats are displayed as expected on my machine. I'm attaching a sample project I used for testing and a screenshot of the result. Please run it and test to see the result as well. Missing year without any kind of formats The year is missing due to the BaseUnit parameter. Currently, it is set to ChartCategoryAxisBaseUnit. Days. With the current set, the day is important to show. As a result, the Chart shows only the day and month. I hope you find the above information helpful. Let me know if you run across any problems. Thank you.
