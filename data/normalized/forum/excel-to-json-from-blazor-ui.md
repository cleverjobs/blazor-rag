# Excel to JSON from Blazor UI

## Question

**Art** asked on 02 Nov 2021

Requirement: Blazor UI web app -> user select and upload excel file Blazor UI web app -> convert this excel into JSON (column names to properties, column values to values) Question: What would be the best way to achieve this? Is there any component/library that we can use? Thanks, Artem

### Response

**Dimo** commented on 05 Nov 2021

Hello Artem, The uploading part can be done with our Blazor Upload component. Once you have the file on the server, you can use another product of ours - the Telerik Document Processing library: Import the Excel file using the XlsxFormatProvider Iterate the cells and get the cell values. Use the features built in the System.Text.Json namespace to serialize the object to JSON
