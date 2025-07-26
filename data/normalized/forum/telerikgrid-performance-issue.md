# Telerikgrid performance issue

## Question

**Afr** asked on 17 Apr 2023

Hi, I am using Telerikgrid to display the data which I am loading from database. At a time there can be only couple of 100 records return from database. There is no custom formatting or any calculation when loading the data in the grid. I am not using the paging. I am still seeing the records are loading in the grid very slowly. What can be done to improve the performance? Thanks & regards, Afreen

## Answer

**Dimo** answered on 20 Apr 2023

Hello Afreen, The general recipe is to reduce the number of UI refreshes and the number of rendered components on the page. The latter can mean: Using paging with a reasonable page size. Using row virtualization (instead of paging, but you will still set a PageSize ). Using column virtualization if you have a lot of columns. Also, you can rely on OnRead data binding, so that the Grid does not receive all items from the database at the same time. This applies especially in WebAssembly scenarios, so that you can offload the browser from data operations. We have some performance tips in our documentation as well. Finally, 200-300 items is not that much, so the performance issue may be outside the Grid. Here is a REPL test page, which is a WebAssembly app, so the .NET runtime, data operations and HTML rendering all occur in the same browser thread, which makes things slower. Regards, Dimo Progress Telerik
