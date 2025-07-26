# Chart tooltip formatting for currency?

## Question

**Dea** asked on 13 Jun 2023

When I try the following I just get the underlining number: 343526.3 <ChartSeriesTooltip Visible="true"> <Template> @(string.Format("{0:C2}", (context.FormattedValue as object))) </Template> </ChartSeriesTooltip> When I try, I get: <ChartSeriesTooltip Visible="true"> <Template> @(string.Format("{0:C2}", (context.DataItem as object))) </Template> </ChartSeriesTooltip> I am not sure what I am doing wrong here. the class tis attached to: public class MDRevNCostOverTime { [DisplayFormat(DataFormatString="{0:C}")] public decimal Series1 { get; set; } [DisplayFormat(DataFormatString="{0:C}")] public decimal Series2 { get; set; } }

## Answer

**Deasun** answered on 16 Jun 2023

Got it: string.Format("{0:C}", Convert.ToDecimal(objContext.FormattedValue.ToString())) works for me. :)

### Response

**Nadezhda Tacheva** answered on 16 Jun 2023

Hi Deasun, It looks like the cast and formatting are not successful with this syntax. I would generally recommend storing the DataItem from the context in a variable and using that for the formatting. Here is an example: [https://blazorrepl.telerik.com/mnOqlglu56p7vkZm58.](https://blazorrepl.telerik.com/mnOqlglu56p7vkZm58.) Can you please try this approach and let me know if the issue persists? If so, please modify the sample - replicate your exact configuration to reproduce the problem and send it to me for review. This will allow me to debug and try to find the root cause. Regards, Nadezhda Tacheva

### Response

**Deasun** commented on 16 Jun 2023

can you post your code in the forum thread? Those REPL links never work! All i get is a blank screen. Doesnt matter what browser I try.

### Response

**Nadezhda Tacheva** answered on 19 Jun 2023

Hi Deasun, I am glad that you've managed to find a solution that works for you. Meanwhile, I'm pasting my suggestion as you've mentioned the REPL link does not load: <TelerikChart> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Line" Name="Product 1" Data="@series1Data"> <ChartSeriesTooltip Visible="true"> <Template> @{
var TooltipText=context.DataItem as object;
}
@(string.Format("{0:C2}", TooltipText)) </Template> </ChartSeriesTooltip> </ChartSeries> </ChartSeriesItems> <ChartCategoryAxes> <ChartCategoryAxis Categories="@xAxisItems"> </ChartCategoryAxis> </ChartCategoryAxes> <ChartTitle Text="Quarterly revenue per product"> </ChartTitle> <ChartLegend Position="ChartLegendPosition.Right"> </ChartLegend> </TelerikChart> @code {
public List <object> series1Data=new List <object> () { 10, 2, 5, 6 };
public string[] xAxisItems=new string[] { "Q1", "Q2", "Q3", "Q4" };
} Note: If you want us to revise the issue you have with the REPL tool, you may open a dedicated ticket for that listing any possible console errors you might be getting. Other than that, you may try clearing the cache and site data to see if this helps. Regards, Nadezhda Tacheva
