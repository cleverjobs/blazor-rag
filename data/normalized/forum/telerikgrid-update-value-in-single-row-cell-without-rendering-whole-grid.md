# TelerikGrid : Update value in single row/cell without rendering whole grid

## Question

**Geo** asked on 23 May 2023

Hi, Rendering the whole TelerikGrid in Blazor can be slow when there are lots of rows. How do I update the value in a single cell or row, without re-rendering the whole grid?

## Answer

**Luis Michel Silva** answered on 25 May 2023

If you have all the data at once and you are using the Telerik Grid in Blazor, the ToDataSourceResult(request) extension method provided by Telerik can help manage the operations for you. The ToDataSourceResult(request) method simplifies the process of handling data operations like sorting, filtering, and paging on the server side. It takes a DataSourceRequest object as input and returns a DataSourceResult object that contains the processed data. By using the ToDataSourceResult(request) method and properly configuring the grid, you can easily manage data operations like sorting, filtering, and paging on the server side without manually implementing each operation. Remember to customize the data processing logic in the ToDataSourceResult method based on your specific requirements and data source. Blazor Grid - Manual Operations - Telerik UI for Blazor

### Response

**Nadezhda Tacheva** answered on 26 May 2023

Hi George, We've made some improvements in this regard in UI for Blazor 4.1.0. You can find some more details here: [https://feedback.telerik.com/blazor/1594018-triggering-edit-mode-leads-to-re-renders-in-other-cells.](https://feedback.telerik.com/blazor/1594018-triggering-edit-mode-leads-to-re-renders-in-other-cells.) In addition, you may also consider options for improving the Grid performance such as passing small chunks of data through the OnRead event and using the ToDataSourceResult(request) extension method as Luis mentioned. Regards, Nadezhda Tacheva Progress Telerik
