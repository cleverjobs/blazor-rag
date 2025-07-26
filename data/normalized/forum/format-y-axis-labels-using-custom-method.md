# Format y-axis labels using custom method

## Question

**Fab** asked on 05 Oct 2022

Hello, We need to have string labels in our y-axis Actually we have an int that matches to an Enum and instead of int number we want to print the Enum string representation Based on the docs we can either use the Format expression or a Template but none of them allow us for example to use the expression ((MyEnum)value).ToString() How can we do? Also, is it possible to use Category axis on the ordinate (the y axis) ? Thanks

## Answer

**Marin Bratanov** answered on 08 Oct 2022

Hello Fabio, You can define the categories of the chart in several ways, and this lets you define your own strings you want to put there by shaping the data you give to the chart. So, when preparing the chart data source, you can extract the desired string (even localize them if you will) and simply put them in the chart data, no need for any hard to maintain customization on the component itself - it renders what you give it. Please review this article to see the different ways (in short - setting the Categories of the x-axis; or using the CategoryField of the series): [https://docs.telerik.com/blazor-ui/components/chart/data-bind](https://docs.telerik.com/blazor-ui/components/chart/data-bind) The y-axis is always numerical, though, so it can't show categories. If you implement a sort of template, you could render text instead of numbers based on some internal app logic, but it is not a main feature of the chart. Regards, Marin Bratanov Progress Telerik

### Response

**Fabio** commented on 10 Oct 2022

Hello Marin, I've no problem with X asix, just with Y and reading about template I didn't managed to have a way to put a dynamic text based on the Y value (in our scenario we want to put a translated text based on the Y value. To put this in practice, let see our current chart: This is a typical tachograph chart and instead of legends, we like to add an Y axis where at each value we print a text. I've built this using an Area chart (btw, I miss a chart that allows to create a column with different width, to do that I have to use an area and create 0-value points before and after the min and max of the column I want to generate) Each colored area you see has a different height, so for instance the green area has a value of 2 (Resting), yellow has a value of 4 (Available) and so on. Instead of a simple legend we may want to add labels on the Y based on the series height (we need to translate it so it has to be dynamic) I didn't found a way to specify a template that allows me to do so, is it possible?

### Response

**Dimo** commented on 13 Oct 2022

Hello Fabio, My suggestion is to use a Chart axis label template. These templates are JavaScript-based, so you can implement a JavaScript object that returns the required string label from the enum value. You can even generate the JavaScript object with C# code, so that there is no repetition of the enum declaration. <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Area" Data="@ChartData" CategoryField="@nameof(ChartModel.Hour)" Field="@nameof(ChartModel.Value)"> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis> <ChartValueAxisLabels Template="@ValueAxisLabelTemplate"> </ChartValueAxisLabels> </ChartValueAxis> </ChartValueAxes> </TelerikChart> @* suppress-error allows script tags in Razor components *@<script suppress-error="BL9992"> var enumValues={ 1: "One", 2: "Two", 3: "Three", 4: "Four" }; function getLabelText ( intValue ) { var stringValue=enumValues[intValue]; return stringValue ? stringValue : "";
} </script> @code { private List<ChartModel> ChartData { get; set; } private string ValueAxisLabelTemplate { get; set; }="#=getLabelText(value) #"; protected override void OnInitialized ( ) {
ChartData=new List<ChartModel>(); var rnd=new Random(); for (int i=1; i <=23; i++)
{
ChartData.Add( new ChartModel ( ) {
Hour=i,
Value=rnd.Next( 1, 5 )
});
}

base.OnInitialized();
} public class ChartModel { public int Hour { get; set; } public int Value { get; set; }
} public enum ChartYValue
{
One=1,
Two=2,
Three=3,
Four=4 }
}

### Response

**Fabio** commented on 14 Oct 2022

Hello Dimo, this is a nasty fix that defeat blazor purpose but at least would solve our specific need, thanks afaik your blazor chart are just a proxy over your js version of the chart, do you have any plan to have native blazor charts in your roadmap (pure informative question)?

### Response

**Dimo** commented on 18 Oct 2022

@Fabio - the assumption is not correct. We do reuse some of the Chart and Editor's JS code in several products, but the components themselves are true native Blazor components. They are not wrappers.
