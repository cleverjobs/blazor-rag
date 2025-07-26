# Grid Export to Excel - keep UI Culture

## Question

**TomTom** asked on 18 Aug 2020

Hi, Is there a way to keep the UI culture info when exporting a grid to Excel? I have a date field which is displayed in the browser as dd/MM/yyyy which is how I want it. But when exported to Excel it becomes MM/dd/yyyy. I set the UI culture in the blazor Program.Main. var culture=new CultureInfo("en-GB"); CultureInfo.DefaultThreadCurrentCulture=culture; CultureInfo.DefaultThreadCurrentUICulture=culture; System.Threading.Thread.CurrentThread.CurrentCulture=culture; System.Threading.Thread.CurrentThread.CurrentUICulture=culture; I am using the WebAssembly version of Blazor. Thanks, Tom

## Answer

**Marin Bratanov** answered on 18 Aug 2020

Hi Tom, The excel export uses a format that Excel understands, because there is a mismatch between the .NET culture date formats and what Excel recognizes as dates. I've updated the Notes section of the Excel Export docs with the format we use for dates and numbers. I've also made the following feature request on your behalf for the grid to allow you to set custom format strings: [https://feedback.telerik.com/blazor/1481023-custom-format-for-excel-export-per-column.](https://feedback.telerik.com/blazor/1481023-custom-format-for-excel-export-per-column.) Regards, Marin Bratanov

### Response

**Tom** answered on 18 Aug 2020

Thanks for the feature request Marin.
