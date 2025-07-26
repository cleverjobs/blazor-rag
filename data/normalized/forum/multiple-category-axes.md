# Multiple category axes

## Question

**Nik** asked on 04 Oct 2021

I would like to have two or more category axes, where in this example, I would like all the months for each year to be displayed above the year. Both year and month should use the same value series "YAxis". But I can't figure out how to get this result. How it looks now: How it should look: Code: <div style="height: 80vh;"> <TelerikChart Height="100%"> <ChartLegend Visible="false" /> <ChartTooltip Visible="true" Background="white" Color="black"> <Template> <div> <strong> @context.SeriesName: </strong> @string.Format("{0:N0}", Convert.ToDouble(context.FormattedValue.ToString().Replace('.', ','))) </div> </Template> </ChartTooltip> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Data="Data" Field="Value" CategoryField="Month"> </ChartSeries> <ChartSeries Visible="false" Data="Data" Field="Value" CategoryField="Year" CategoryAxis="secondAxis"> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Min="0"> <ChartValueAxisLabels Format="{0:N0}"> </ChartValueAxisLabels> <ChartValueAxisTitle Text="Value"> </ChartValueAxisTitle> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis> </ChartCategoryAxis> <ChartCategoryAxis Name="secondAxis"> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart> </div> @code { public class ModelData { public int Year { get; set; } public string Month { get; set; } public int Value { get; set; }
} public List <ModelData> Data=new List<ModelData>()
{ new ModelData() { Year=2019, Month="Jan", Value=1000 }, new ModelData() { Year=2019, Month="Feb", Value=2554 }, new ModelData() { Year=2019, Month="Mar", Value=9000 }, new ModelData() { Year=2020, Month="Jan", Value=5250 }, new ModelData() { Year=2020, Month="Feb", Value=3400 }, new ModelData() { Year=2020, Month="Mar", Value=7540 }, new ModelData() { Year=2021, Month="Jan", Value=4570 }, new ModelData() { Year=2021, Month="Feb", Value=7860 }, new ModelData() { Year=2021, Month="Mar", Value=1670 },

};
} NuGet might be missing when downloading the example. Thanks Regards, Nikolas

## Answer

**Nikolas** answered on 05 Oct 2021

Found a fix, maybe a solution? I changed the class ModelData to have a Combined property, where the property is used to bind the series to category axis. Then using the ChartCategoryAxisLabels to templete what property should be displayed, in this case Month instead of Combined. How it looks now: Code: <div style="height: 80vh;"> <TelerikChart Height="100%"> <ChartLegend Visible="false" /> <ChartTooltip Visible="true" Background="white" Color="black"> <Template> <div> <strong> @context.SeriesName: </strong> @string.Format("{0:N0}", Convert.ToDouble(context.FormattedValue.ToString().Replace('.', ','))) </div> </Template> </ChartTooltip> <ChartSeriesItems> <ChartSeries Type="ChartSeriesType.Column" Data="Data" Field="Value" Name="Value" CategoryField="Combined"> </ChartSeries> <ChartSeries Visible="false" Data="Data" Field="Value" CategoryField="Year" CategoryAxis="secondAxis"> </ChartSeries> </ChartSeriesItems> <ChartValueAxes> <ChartValueAxis Min="0"> <ChartValueAxisLabels Format="{0:N0}"> </ChartValueAxisLabels> <ChartValueAxisTitle Text="Value"> </ChartValueAxisTitle> </ChartValueAxis> </ChartValueAxes> <ChartCategoryAxes> <ChartCategoryAxis> <ChartCategoryAxisLabels Template="#=dataItem.Month#"> </ChartCategoryAxisLabels> </ChartCategoryAxis> <ChartCategoryAxis Name="secondAxis"> </ChartCategoryAxis> </ChartCategoryAxes> </TelerikChart> </div> @code { public class ModelData { public int Year { get; set; } public string Month { get; set; } public int Value { get; set; } public string Combined { get; set; }
} public List <ModelData> Data=new List<ModelData>()
{ new ModelData() { Year=2019, Month="Jan", Value=1000, Combined="2019Jan" }, new ModelData() { Year=2019, Month="Feb", Value=2554, Combined="2019Feb" }, new ModelData() { Year=2019, Month="Mar", Value=9000, Combined="2019Mar" }, new ModelData() { Year=2020, Month="Jan", Value=5250, Combined="2020Jan" }, new ModelData() { Year=2020, Month="Feb", Value=3400, Combined="2020Feb" }, new ModelData() { Year=2020, Month="Mar", Value=7540, Combined="2020Mar" }, new ModelData() { Year=2021, Month="Jan", Value=4570, Combined="2021Jan" }, new ModelData() { Year=2021, Month="Feb", Value=7860, Combined="2021Feb" }, new ModelData() { Year=2021, Month="Mar", Value=1670, Combined="2021Mar" },

};
} If anyone knows another way around this, please let me know. Thanks Regards, Nikolas

### Response

**Emil** commented on 05 Oct 2021

This only works if you have the same amount pr year. If a year is missing some months, the axis will not display as intended. In the image below 2001, 2002, 2003 all have 12 months, and 2004 only have 3. Is there a different solution or a fix to this? And is it possible to change the color of the axisseperatorline? Best Regards, Emil
