# Title with a category axis?

## Question

**Dat** asked on 10 Oct 2019

I have a date category x-axis which is currently auto fitting. It is somewhat redundant however I was trying to add a title to the axis and I ran into issues. Is that supported? I can easily add titles to a value axis. Without the line "ChartCategoryAxisTitle" it works correctly however with no title. Code: <ChartCategoryAxes> <ChartCategoryAxis BaseUnit="ChartCategoryAxisBaseUnit.Fit" Type="ChartCategoryAxisType.Date" MaxDateGroups="10" /> <ChartCategoryAxisTitle Text="Time" /> </ChartCategoryAxes> Error: blazor.server.js:15 [2019-10-10T18:39:17.853Z] Error: System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.ChartCategoryAxisTitleBase.AddSelfToParent() at Telerik.Generated.Blazor.Components.ChildComponent.OnInitialized() at Telerik.Blazor.Components.ChartCategoryAxisTitleBase.OnInitialized() at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync()

## Answer

**Marin Bratanov** answered on 11 Oct 2019

Hi Patrick, In the chart, child elements are nested under their parent - so the concrete axis title must go under the axis tag. Generally, tags that begin with the same name get nested in one another. For example, ChartCategoryAxis can contain ChartCategoryAxis Title and ChartCategoryAxis Labels, but you can't put those two inside ChartCategoryAx e s Here's an example I made for you (a screenshot of the result is attached at the end): <TelerikChart> <ChartCategoryAxes> <ChartCategoryAxis BaseUnit="ChartCategoryAxisBaseUnit.Fit" Type="ChartCategoryAxisType.Date" MaxDateGroups="10"> <ChartCategoryAxisTitle Text="Time"> </ChartCategoryAxisTitle> </ChartCategoryAxis> </ChartCategoryAxes> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Name="Product 1 (SUM)" Data="@chartData" Field="@nameof(MyDataModel.Product1)" CategoryField="@nameof(MyDataModel.MySharedCategories)" Aggregate="ChartSeriesAggregate.Sum"> <ChartSeriesLabels Visible="true"> </ChartSeriesLabels> </ChartSeries> <ChartSeries Type="ChartSeriesType.Column" Name="Product 2 (COUNT)" Data="@chartData" Field="@nameof(MyDataModel.Product2)" Aggregate="ChartSeriesAggregate.Count"> <ChartSeriesLabels Visible="true"> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> </TelerikChart> @code {
public class MyDataModel
{
public DateTime MySharedCategories { get; set; }
public int Product1 { get; set; }
public int Product2 { get; set; }
}

public List <MyDataModel> chartData=new List <MyDataModel> ()
{
new MyDataModel() { MySharedCategories=new DateTime(2019, 11, 11), Product1=1, Product2=2 },
new MyDataModel() { MySharedCategories=new DateTime(2019, 12, 15), Product1=2, Product2=3 },
new MyDataModel() { MySharedCategories=new DateTime(2019, 12, 19), Product1=3, Product2=4 },
new MyDataModel() { MySharedCategories=new DateTime(2019, 12, 28), Product1=4, Product2=5 },
};
} Regards, Marin Bratanov

### Response

**Datafyer** answered on 11 Oct 2019

Thank you. That makes perfect sense. Not sure why I didn't notice the title tag was not nested. Errors during design time would certainly be helpful.

### Response

**Marin Bratanov** answered on 13 Oct 2019

Hello Patrick, It's good to hear you have things working. On design-time errors - in Blazor there isn't the same design-time surface as in, say WebForms or WinForms, and at the moment, our options in this regard are extremely limited. In fact, the framework gets confused by components from the project and inner tags (see here ) and by nesting (see here ). We have it on our radar to see if we can do anything, but it seems like we need to wait for the framework to implement something like showing only the allowed tags under a parent tag. Regards, Marin Bratanov
