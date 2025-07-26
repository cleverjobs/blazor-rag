# Grid ExcelExport and dates

## Question

**Dea** asked on 30 Jul 2021

Hi, When exporting data from a grid using ExcelExport, the dates are visible when viewed from Excel, but not when using Open Office or Google Sheets. Is there any reason for this? Can it be addressed, as increasing numbers of people use these methods for viewing Excel files. [https://demos.telerik.com/blazor-ui/grid/export-excel?_ga=2.141805431.450598280.1627570618-522564835.1576660522](https://demos.telerik.com/blazor-ui/grid/export-excel?_ga=2.141805431.450598280.1627570618-522564835.1576660522) Output file is attached - see final column in Open Office or Google Sheets. Thanks, Dean

### Response

**Nadezhda Tacheva** commented on 04 Aug 2021

Hello Dean, We are in process of further investigating this scenario along with the development team. We will get back to you with more details as soon as possible.

## Answer

**Nadezhda Tacheva** answered on 24 Aug 2021

Hi Dean, Thank you for your patience! I was able to investigate the described behavior with the Document Processing team whose libraries we actually use to export the Grid to Excel. Generally speaking, when it comes to Excel formatting Telerik supports the available Microsoft Standards. To cover the described scenario the Document Processing team made some changes regarding exporting dates - an alternative exporting approach will be applied that should be recognized by other spreadsheet applications. The change will be available in the next version of the Document Processing Libraries and we have scheduled testing procedures. In case they are successful, the update will be included in the upcoming version 2.27.0 of Telerik UI for Blazor. I have opened a public post in our

### Response

**Dean** commented on 25 Aug 2021

Thanks for the update!
