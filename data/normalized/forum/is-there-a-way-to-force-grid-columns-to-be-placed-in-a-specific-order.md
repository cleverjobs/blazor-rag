# Is there a way to force grid columns to be placed in a specific order?

## Question

**Eth** asked on 14 Sep 2022

My telerik grid will occasionally place <GridColumn> components out of order from what I expect from the code. Is there a way to enforce the order that the columns will be placed on the grid? I've attached some code below and as you can see the grid columns "Total Pieces" and "Total % Total" should be the last two columns but for some users they will load in the middle of the grid. <TelerikGrid Data="@myGridData" @ref="@Grid" Width="100%" Height="100%" Groupable="true" Pageable="false" Sortable="true" EnableLoaderContainer="@ShowLoading" FilterMode="@GridFilterMode.FilterMenu"> <GridColumns> <GridColumn Field="field1" Width="110px" FieldType="@typeof(string)" Title="Field 1" /> <GridColumn Field="field2" Width="80px" FieldType="@typeof(int)" Title="Field 2" /> <GridColumn Field="field3" Width="130px" FieldType="@typeof(string)" Title="Field 3" /> @if (UnitNumberColumnNames is not null && UnitNumberColumnNames.Any())
{
foreach (var lengthColumnName in UnitNumberColumnNames)
{ <GridColumn Width="90px" Field="@lengthColumnName" FieldType="@typeof(decimal)" Title="@lengthColumnName" /> }
} <GridColumn Field="Total Pieces" FieldType="@typeof(decimal)" Title="Total Pieces" /> <GridColumn Field="Total % Total" FieldType="@typeof(decimal)" Title="Total % Total" /> </GridColumns> </TelerikGrid>

## Answer

**Dimo** answered on 15 Sep 2022

Hello Ethan, This is a Blazor framework phenomenon. To prevent it, set a @key for the columns. Regards, Dimo
