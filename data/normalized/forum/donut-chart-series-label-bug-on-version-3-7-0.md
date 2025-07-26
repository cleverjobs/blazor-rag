# Donut Chart Series Label Bug on version 3.7.0

## Question

**Ind** asked on 06 Jan 2023

I upgraded Telerik Blazor from version 3.6.1 to 3.7.0 and the Donut Chart is broken when the series value is 0. This is the differences: This is my REPL link [https://blazorrepl.telerik.com/QnuFkUly444cSYuJ13](https://blazorrepl.telerik.com/QnuFkUly444cSYuJ13) copied from your demo page [https://demos.telerik.com/blazor-ui/chart/donut-chart](https://demos.telerik.com/blazor-ui/chart/donut-chart) I just change some of the values to 0. Just change the Telerik Blazor package version to see the difference

## Answer

**Hristian Stefanov** answered on 11 Jan 2023

Hi Indra, Thank you for explaining that good what you are experiencing at the moment. The described change in the Donut Chart behavior is due to a bug that was fixed in 3.7. That change applies to all Telerik suits (jQuery, Angular, React, etc.). I'm sorry for the inconvenience that it caused. Before 3.7, when there was an item with "Value=" 0 "", the 0 was not visible. Now the fix is that every value is visible, which includes 0. That way, the user will see all the Donut Chart data source information displayed. Still, you can hide the 0s like before the fix by modifying the LabelTemplate. Here is an example of how you can achieve it: @using Telerik.Blazor <TelerikChart> <ChartTitle Text="What is you favourite sport?"> </ChartTitle> <ChartLegend Visible="true" Position="ChartLegendPosition.Top"> </ChartLegend> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Donut" Data="@Data" Field="@nameof(ModelData.Value)" CategoryField="@nameof(ModelData.Category)"> <ChartSeriesTooltip Visible="true" Context="item"> <Template> @item.Percentage.ToString("P") </Template> </ChartSeriesTooltip> <ChartSeriesLabels Position="ChartSeriesLabelsPosition.OutsideEnd" Visible="true" Background="transparent" Template="@MySeriesTemplate"> </ChartSeriesLabels> </ChartSeries> </ChartSeriesItems> </TelerikChart> @code { public string MySeriesTemplate="# if (value !=0) { # #=dataItem.Category# - #=percentage*100 #% #}#"; public class ModelData
{
public string Category { get; set; }
public int Value { get; set; }
}

public List <ModelData> Data=new List <ModelData> ()
{
new ModelData()
{
Category="Football",
Value=0
},
new ModelData()
{
Category="Basketball",
Value=0
},
new ModelData()
{
Category="Volleyball",
Value=0
},
new ModelData()
{
Category="Rugby",
Value=0
},
new ModelData()
{
Category="Tennis",
Value=10
}
};
} Please run and test it to see the result. Let me know if it suits your needs. Regards, Hristian Stefanov Progress Telerik

### Response

**Indra** commented on 13 Jan 2023

Adding the conditional logic in the Series Label Template works for us. Thanks Hristian.
