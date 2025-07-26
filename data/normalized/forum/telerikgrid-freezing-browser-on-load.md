# TelerikGrid freezing browser on load

## Question

**Eth** asked on 31 Aug 2022

I've got a TelerikGrid that occasionally loads a very large amount of data and when this happens it will freeze the entire webpage. I was wondering if there is a way to load the grid asynchronously, to allow users to still be able to click other things, or if there is a way to indicate to the user that a loading is occurring. Below is the code for my TelerikGrid and even though I have the line `EnableLoaderContainer="@ShowLoading"` it does not indicate that the grid is loading. <TelerikGrid Data="@model.DegradeTableRows" @ref="@Grid" Width="100%" Height="100%" EnableLoaderContainer="@ShowLoading" Groupable="true" Pageable="false" Sortable="true" FilterMode="@GridFilterMode.FilterMenu"> <GridColumns> <GridColumn Field="unitNumb" Width="110px" FieldType="@typeof(int)" Title="Unit Number" /> <GridColumn Field="grade" Width="100px" Title="Grade" FieldType="@typeof(string)" /> <GridColumn Field="length" Width="100px" FieldType="@typeof(string)" Title="Length" /> @if (SizeColumnNames is not null && SizeColumnNames.Any())
{
foreach (var sizeColumnName in SizeColumnNames)
{ <GridColumn Width="100px" Field="@sizeColumnName" FieldType="@typeof(int)" Title="@sizeColumnName" /> }
} <GridColumn Width="150px" Field="GrandTotal" FieldType="@typeof(decimal)" Title="Grand Total" /> </GridColumns> </TelerikGrid>

## Answer

**Dimo** answered on 01 Sep 2022

Hi Ethan, The Grid does not display a loading animation on initial load. You can use a separate loader. In general, there are two main ways to provide data to our components. We recommend the OnRead event in scenarios with a lot of data. Regards, Dimo
