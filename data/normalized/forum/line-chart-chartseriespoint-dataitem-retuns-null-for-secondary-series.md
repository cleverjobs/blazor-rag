# Line Chart: ChartSeriesPoint.DataItem retuns null for secondary series

## Question

**Iva** asked on 12 Oct 2020

Code: 01. @page "/" 02. @layout MainLayout 03. 04. <TelerikChart> 05. <ChartTitle Text="Unrecoverable Errors Per Minute vs. Signal Level" /> 06. <ChartCategoryAxes> 07. <ChartCategoryAxis Type="@ChartCategoryAxisType.Category" /> 08. </ChartCategoryAxes> 09. <ChartValueAxes> 10. <ChartValueAxis> 11. <ChartValueAxisLabels Visible="true" /> 12. </ChartValueAxis> 13. </ChartValueAxes> 14. <ChartTooltip Visible="true"> 15. <Template> 16. @{ 17. // Null for ChartData2 series 18. var data=context.DataItem as ModelData; 19. <div class="card" style="font-size: 0.8rem; color: black"> 20. <span>@($"{data.Value}")</span> 21. <span>@($"{data.Type}")</span> 22. </div> 23. } 24. </Template> 25. </ChartTooltip> 26. <ChartSeriesItems> 27. <ChartSeries Type="ChartSeriesType.Line" 28. Data="@ChartData1" 29. CategoryField="@nameof(ModelData.Type)" 30. Field="@nameof(ModelData.Value)"> 31. </ChartSeries> 32. <ChartSeries Type="ChartSeriesType.Line" 33. Data="@ChartData2" 34. CategoryField="@nameof(ModelData.Type)" 35. Field="@nameof(ModelData.Value)"> 36. </ChartSeries> 37. </ChartSeriesItems> 38. </TelerikChart> 39. 40. @code { 41. public class ModelData 42. { 43. public string Type { get; set; } 44. public double Value { get; set; } 45. } 46. 47. public List<ModelData> ChartData1=new List<ModelData>() { new ModelData() { Type="S1", Value=1 } }; 48. public List<ModelData> ChartData2=new List<ModelData>() { new ModelData() { Type="S2", Value=5 } }; 49. } Getting runtine error "System.NullReferenceException" at line 18 while mouse hover on chartdata2 series point

## Answer

**Svetoslav Dimitrov** answered on 13 Oct 2020

Hello Ivan, Thank you for reporting that to us. The issue is connected to the way the context gets the DataItem. I have updated the Telerik Points for your account as a little thank you and token of appreciation. Having said that, I have logged a bug report on our Feedback Portal, which you can see from this link here. I have given your Vote for it to raise the popularity and you can Follow it to receive email notifications on status updates. Currently, when you remove the template the Tooltip will get the correct value, so that is the only viable workaround for the time being. Regards, Svetoslav Dimitrov

### Response

**Ivan** answered on 13 Oct 2020

Thanks for your feedback! Yes, for now, the default tooltip is sufficient. However, there is another workaround for displaying prompts through a template: to do this, you need to bind the value of the data series field with some unique identifier of the data model, get it through the FormattedValue context property, and then find the required element in the data collection by identifier.
