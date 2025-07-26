# Can a Grid be defaulted to show all the columns 'auto-fit' based on their content?

## Question

**Adr** asked on 10 Jun 2021

The Telerik Blazor Grid documentation on column widths mentions that: To allow the users to auto-fit the column widths to the content, enable column resizing - a double click on the border between the headers will have the grid adjust the column width according to the size of the data, headers and footers content. Is it possible to generate the grid so that all the columns are set to auto-fit the data by default, rather than it being something that the user has to trigger themselves?

## Answer

**Dimo** answered on 14 Jun 2021

Hello Adrian, Indeed, your question makes sense from end-user perspective, but I am afraid the Grid does not support such a behavior. There is an open feature request with a discussion inside that mentions some of the relevant caveats: [https://feedback.telerik.com/blazor/1513385-autofit-column-widths-on-data-load](https://feedback.telerik.com/blazor/1513385-autofit-column-widths-on-data-load) Regards, Dimo
