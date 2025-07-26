# Export Chart as image

## Question

**Iva** asked on 06 Oct 2020

Hello! It is possible to export TelerikChart as image?

## Answer

**Svetoslav Dimitrov** answered on 09 Oct 2020

Hello Ivan, In this demo application, we have added an example on how to export the Chart to a JPG file. You can also see an example of how to export the Grid to PDF and JPG in the Index.razor page. Regards, Svetoslav Dimitrov

### Response

**Nico** answered on 18 Dec 2020

Hallo! I tried this with a scatter chart, unfortunatelly it is not working. I have no explanation why, because there is no error message and the connection to blazor server will blow up and then the browser reconnects. @page "/export-chart" @using Telerik; @using Telerik.Blazor; @using Telerik.Blazor.Components @using QnSImt.BlazorApp.Services @inject ChartDrawingService DrawingService <TelerikButton Icon="@IconName.Image" OnClick="@ExportChartToJPG">Export to .jpg</TelerikButton> <div @ref="ExportChart"> <TelerikChart Height="480px" Width="640px"> <ChartTitle Text="Risikoanalyse Objektsicherheit ÖNORM B1300 & B1301"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Right"></ChartLegend> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Scatter" Data="@Series1Data" Name="Fassade und Gesimse" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Scatter" Data="@Series2Data" Name="Dach und Dachstuhl" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Scatter" Data="@Series3Data" Name="Allgemein genutzte Teile der Gesamtanlage" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Scatter" Data="@Series4Data" Name="Technische Anlagen der Anlage" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Scatter" Data="@Series5Data" Name="Brandschutz und Gefahrenvermeidung" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Scatter" Data="@Series6Data" Name="Einbruchschutz und Schutz vor Aussengefahren" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> <ChartSeries Type="ChartSeriesType.Scatter" Data="@Series7Data" Name="Gesundheits- und Umweltschutz" XField="@nameof(ModelData.X)" YField="@nameof(ModelData.Y)"> </ChartSeries> </ChartSeriesItems> @*<ChartValueAxes> <ChartValueAxis Color="green"> <ChartValueAxisTitle Text="Schadensausmaß"></ChartValueAxisTitle> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis Name="Schadensausmaß" Categories="@context.ausmassCategories" AxisCrossingValue="@context.crossingValues"></ChartCategoryAxis> <ChartCategoryAxis Name="Auftretenswahrscheinlichkeit" Categories="@context.auftretenCategories"></ChartCategoryAxis> </ChartCategoryAxes>*@<ChartXAxes> <ChartXAxis Min="0" Max="50"> <ChartXAxisLabels Template=""> </ChartXAxisLabels> <ChartXAxisTitle Text="Schadensausmass"></ChartXAxisTitle> </ChartXAxis> </ChartXAxes> <ChartYAxes> <ChartYAxis Min="0" Max="50"> <ChartYAxisTitle Text="Auftretenswahrscheinlichkeit"></ChartYAxisTitle> <ChartYAxisLabels> </ChartYAxisLabels> </ChartYAxis> </ChartYAxes> </TelerikChart> </div> @code { ElementReference ExportChart { get; set; } //Export the Chart to jpg async Task ExportChartToJPG() { var data=await DrawingService.ExportImage(ExportChart); await DrawingService.SaveAs(data, "MyExportedChartJPG.jpg"); } List<StockDataPoint> ChartProduct1Data { get; set; } protected override async Task OnInitializedAsync() { await GenerateChartData(); } async Task GenerateChartData() { ChartProduct1Data=new List<StockDataPoint>() { new StockDataPoint(new DateTime(2019, 1, 1), 39.88m, 40.12m, 41.12m, 39.75m, 3584700), new StockDataPoint(new DateTime(2019, 2, 1), 41.62m, 40.12m, 41.69m, 39.81m, 2632000), new StockDataPoint(new DateTime(2019, 3, 1), 42m, 42.62m, 43.31m, 41.38m, 7631700), new StockDataPoint(new DateTime(2019, 4, 1), 42.25m, 43.06m, 43.31m, 41.12m, 4922200), }; await Task.FromResult(ChartProduct1Data); } public class StockDataPoint { public StockDataPoint() { } public StockDataPoint(DateTime date, decimal open, decimal close, decimal high, decimal low, int volume) { Date=date; Open=open; Close=close; High=high; Low=low; Volume=volume; } public DateTime Date { get; set; } public decimal Open { get; set; } public decimal Close { get; set; } public decimal High { get; set; } public decimal Low { get; set; } public int Volume { get; set; } } public string[] auftretenCategories=new string[] { "SG", "G", "M", "H", "SH" }; public string[] ausmassCategories=new string[] { "SG", "G", "M", "H", "SH" }; public object[] crossingValues=new object[] { 0, 5 }; public class ModelData { public double X { get; set; } public double Y { get; set; } } public List<ModelData> Series1Data=new List<ModelData>() { new ModelData() { X=3, Y=3 }, }; public List<ModelData> Series2Data=new List<ModelData>() { new ModelData() { X=5, Y=3 }, }; public List<ModelData> Series3Data=new List<ModelData>() { new ModelData() { X=7, Y=3 }, }; public List<ModelData> Series4Data=new List<ModelData>() { new ModelData() { X=3, Y=5 }, }; public List<ModelData> Series5Data=new List<ModelData>() { new ModelData() { X=5, Y=5 }, }; public List<ModelData> Series6Data=new List<ModelData>() { new ModelData() { X=7, Y=5 }, }; public List<ModelData> Series7Data=new List<ModelData>() { new ModelData() { X=5, Y=7 }, }; }

### Response

**Marin Bratanov** answered on 21 Dec 2020

Hi Nico, I am attaching here a modified version of the sample project that uses the provided chart declaration and data, and seems to work fine for me. If comparing against it does not help you resolve the issue, I recommend you modify it to showcase the problem and open a support ticket where you can attach that broken project so we can have a look. Regards, Marin Bratanov

### Response

**Adam** answered on 11 Feb 2021

Hi Will this approach work with Blazor WASM? Thanks Adam

### Response

**Marin Bratanov** answered on 11 Feb 2021

Hi Adam, Yes, it would, that approach is JavaScript-based. I made the same sample in WebAssembly, it is attached to this post. Regards, Marin Bratanov

### Response

**Adam** answered on 11 Feb 2021

Thanks Marin - very helpful, got the example working fine. However if I try to output the chart to pdf by adding the following to Export_Chart.razor: <TelerikButton Icon="image" OnClick="@ExportChartToPDF">Export to .pdf</TelerikButton> //Export the Chart to pdf async Task ExportChartToPDF() { var data=await DrawingService.ExportPDF(ExportChart); await DrawingService.SaveAs(data, "MyExportedChart.pdf"); } Then i get an error. Ideally i would like to be able to e.g. output a div which contains several charts as a pdf. Thanks Adam

### Response

**Marin Bratanov** answered on 11 Feb 2021

Hello Adam, I'm afraid that right now this is not possible. The PDF exporting tool relies on the DOM to get things done, and the chart is not HTML, so it cannot become a PDF like that. Perhaps getting the images as binary data and sending them to a server endpoint for further processing, and generating a PDF there could be an option. Or, if you need report generation - a real reporting solution could let you do that. Regards, Marin Bratanov

### Response

**Adam** answered on 15 Feb 2021

Thanks for clarifying Marin. Being able to save as images is still really useful.

### Response

**Jack** answered on 16 Feb 2021

Need to look at the _Host.cshtml and add the <!-- We need these two Kendo libs + Pako, delivered through LibMan in the project --> also modify the Startup.cs and it works great.
