# ChartCategoryAxisLabels HTML Template

## Question

**Ole** asked on 07 Jun 2021

Is there any way to place HTML code into Template for category-axis? Documentation suggests one way like this: <ChartCategoryAxisLabels Template="#=value#"> </ChartCategoryAxisLabels> But I need to realize more complicated tasks. For example, show image instead of simple text (place url into on of the categories and then show it through <img> tag). Now, I сouldn't do anything more than: <ChartCategoryAxes> <ChartCategoryAxis Name="chartCategories" Categories="@NumberCategoriesData"> </ChartCategoryAxis> <ChartCategoryAxis Name="pictureCategories" Categories="@PictureCategoriesData"> <ChartCategoryAxisLabels Template="#=value#"> </ChartCategoryAxisLabels> </ChartCategoryAxis> </ChartCategoryAxes> <ChartValueAxes> <ChartValueAxis AxisCrossingValue="@crossingPoints"> </ChartValueAxis> </ChartValueAxes> If there isn't more options to solve this approach, is it already planned to add or not?

## Answer

**Eric R | Senior Technical Support Engineer** answered on 09 Jun 2021

Hi Oleg, At this time, the Label Templates can only contain plain-text as outlined in the Chart Label Templates documentation. As a result, I have gone ahead and created a feature request for this which can be found at Allow Html Code in Label Template request. Additionally, I have cast a vote on your behalf which will increase the priority of the item. I encourage following it to receive future status updates. In the meantime, please let me know if you need any additional information. Thank you for using the UI for Blazor forums and providing the feedback. Regards, Eric R | Senior Technical Support Engineer Progress Telerik

### Response

**Oleg** commented on 10 Jun 2021

Thanks a lot for your support!
