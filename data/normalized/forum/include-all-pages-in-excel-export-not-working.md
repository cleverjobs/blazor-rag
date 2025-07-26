# Include all pages in Excel export not working

## Question

**Lic** asked on 28 May 2020

Hi If i export my data to excel, only the current page is shown. The "AllPages" flag is set to true. I load my data via "OnRead", because i need to implement pagination by myself. How can i achieve this. Kind regards Matthias

## Answer

**Marin Bratanov** answered on 28 May 2020

Hi Matthias, With OnRead, AllPages cannot be exported because the grid Data only has the current page: [https://docs.telerik.com/blazor-ui/components/grid/export/excel#notes:](https://docs.telerik.com/blazor-ui/components/grid/export/excel#notes:) If you are using the OnRead event, only the current page of data will be exported, because that's all the grid has at the time of the export action. That said, it would, indeed, be great if that were possible, so I logged an improvement idea whose implementation you could follow here: [https://feedback.telerik.com/blazor/1469312-include-all-pages-in-excel-export-should-work-with-onread](https://feedback.telerik.com/blazor/1469312-include-all-pages-in-excel-export-should-work-with-onread) Regards, Marin Bratanov
