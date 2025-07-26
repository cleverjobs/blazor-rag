# Issue with tooltips and editor template in tabstrip.

## Question

**Sar** asked on 01 Jul 2024

I have a data structure of orders and are listing those each in a tab within a tabstrip. From there I have 4 separate grids for 4 parts of the order. I don't know if this is related to being added in a tabstrip, but I cannot get tooltips to show in the grids or the editor template to show in edit when I click the GridCommandButton for Edit. Here is an example of my tooltip: if (item.WORK_ORDER !=null)
{ <span title="@item.WORK_ORDER"> </span> <TelerikTooltip TargetSelector="@( " # tooltip-target " + item.ID )" Width="350px" Height="250px" Position="@TooltipPosition.Right"> </TelerikTooltip> } And here is an example of how I have added into my tabstrip: <TelerikTabStrip ActiveTabIndex="@activeTab" ActiveTabIndexChanged="@TabChangedHandler" Scrollable="true" TabPosition="@TabPosition.Right" Width="100%" Height="100%"> @{
foreach (OrderData item in OrdersData)
{ <TabStripTab Class="@(item.TITLE==Title ? " selected ": "")" Title="@item.TITLE" Visible="@(item.PatternRecords.Count> 0 ? true : false)" @key="@item"> }
}

### Response

**Sara** commented on 03 Jul 2024

I have solved the problem with the tooltips. I didn't have the id set correctly within the span.
