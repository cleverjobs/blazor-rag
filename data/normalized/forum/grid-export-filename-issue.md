# Grid export filename issue

## Question

**Dea** asked on 25 Apr 2023

When I export the gird I try to set the name of the file to be exported. As such: <GridExport> <GridExcelExport FileName="@msExportFileName" AllPages="@Revenue_ExportAllPages" OnBeforeExport="@Revenue_OnBeforeExcelExport" /> </GridExport> string msExportFileName="Rpt_"; public void Revenue_OnBeforeExcelExport(GridBeforeExcelExportEventArgs args) { msExportFileName="Rpt_ProductsCarriers_" + "Revenue"; ) When it goes into the Revenue_OnBeforeExcelExport the file name works out to be: "Rpt_" only. If I then click export again the file name="Rpt_ProductsCarriers_Revenue" How can I get the name the first time around to work? Note! the "ProductsCarriers" is hardcode above but actually comes from a DDL object the user has already chosen before it gets to this point. It can be different values depending on what the user chooses. Even hardcoded , the first time in ignores that above code. msExportFileName="Rpt_ProductsCarriers_" + "Revenue"; Stepping thru it the code above seems to be working, but then the file name is "Rpt_" on first attempt. Strange. Thanks Deasun.

## Answer

**Svetoslav Dimitrov** answered on 28 Apr 2023

Hello Deasun, I have opened a new bug report on your behalf - The value of the FileName parameter is not updated properly in the OnBeforeExport event handler. I have added your Vote for it and you are automatically subscribed to receive email notifications on status updates. As a small token of our appreciation, I have awarded your account with Telerik Points. In the public thread, I have added a workaround for the time being. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Peter** commented on 05 Sep 2024

Hello Telerik, This is not fixed correct? I attempted the workaround but it still only works the second time around. Thank you

### Response

**Dimo** commented on 05 Sep 2024

@Peter - indeed, the workaround stopped working with newer versions, so I removed it. Sorry about the confusion. I voted for the public item on your behalf. The popularity is relatively low, so it is still awaiting prioritization.

### Response

**Peter** commented on 05 Sep 2024

Thank you Dimo. Interesting how exporting to Excel is a low priority. Is there another possible workaround Dimo since the error occurs only on the first instance of the Excel Export button click?

### Response

**Dimo** commented on 05 Sep 2024

Exporting to Excel itself is an important feature, but changing the Excel file name in OnBeforeExport doesn't seem to be. A possible workaround is to prepare / set the file name before OnBeforeExport fires, if applicable.
