# Add column to grid on export not showing the Title

## Question

**Coo** asked on 25 Aug 2022

I have a TelerikGrid that I want to export to Excel or CSV, but before I export it I want to add a column. I add the column and set it's Field & Title, which when exported the Field data is shown but not the Title. I have followed the documentation and created a hidden column, then using the OnBeforeExport event, added the column to the list but still the Title does not export. Am I missing something?

## Answer

**Dimo** answered on 08 Sep 2022

Hi Alistair, I confirm this is a valid bug and I logged it on your behalf in our issue portal. I hope this is not a major show stopper for you, or that you can use the suggested workaround with the dynamic column width. I also awarded you some Telerik points for bringing the issue to our attention. Regards, Dimo

### Response

**Nadezhda Tacheva** answered on 30 Aug 2022

Hi Alistair, I've been testing the scenario by handling the OnBeforeExport event to add a hidden column in the Excel or CSV exported file. On my end it looks like the specified Title is accordingly displayed in the exported file. You may test it as well: [https://blazorrepl.telerik.com/GwuidEuW37b6JcXq45.](https://blazorrepl.telerik.com/GwuidEuW37b6JcXq45.) The newly added column for the ProductId field has a "Product Id" title. In order to move forward, you may send us an isolated sample that reproduces the issue you are experiencing. Thus, we will be able to debug it and find the root cause for this behavior. Thank you in advance! Regards, Nadezhda Tacheva

### Response

**Coops** commented on 30 Aug 2022

Hi Nadezhda Tacheva, Thanks for looking at this, I will try to sort a sample out to upload. The main difference in our scenario is that we are using the 'OnRead' event of the grid to get our data. If your sample is altered to get the data using the 'OnRead' event to retrieve from a data source, will it still work? Would this be the key to solving the issue?

### Response

**Coops** commented on 30 Aug 2022

After doing some investigation and creating a sample project ( [https://blazorrepl.telerik.com/GGuMHObk30JeSoON52](https://blazorrepl.telerik.com/GGuMHObk30JeSoON52) ), I think that it is when a template is applied. If the 'Source' columns are removed then the title appears, but with them it does not.

### Response

**Nadezhda Tacheva** commented on 02 Sep 2022

Hi Alistair, Thank you for the provided sample! I managed to reproduce the described behavior on my end, too. Generally speaking, it is expected that the Template is not exported. This is a known specifics of the export which you can find listed in the Notes section. However, in the example you are using a Template for another column and not for the non-visible one that you are programmatically adding during the export. That said, the Template should not be an issue. It looks to me that the behavior occurs when using Multi Column Headers, though. I will additionally revise it with our development team and I will get back to you to provide details. Thank you for your patience in the meantime!
