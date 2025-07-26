# Blazor Grid Export ? { alternating Colors }

## Question

**Dea** asked on 09 Jan 2023

When export the grid to excel is there a way to tell it to use the row colors the grid shows on the page? Thanks.

## Answer

**Nadezhda Tacheva** answered on 12 Jan 2023

Hi Deasun, The Grid allows you to customize the exported file before it reaches the client. It exposes Export Events that you can handle to set different options to the file or get the whole file and configure it as needed through the RadSpreadProcessing library. The following knowledge base article demonstrates how to get the file in the OnAfterExport event to set background color to the desired cells: Custom cell formatting of the exported file with RadSpreadProcessing I hope it will help you with the implementation on your side. Please let us know if any other questions appear in the meantime. Regards, Nadezhda Tacheva

### Response

**Deasun** commented on 13 Jan 2023

Thanks. Will review that.
