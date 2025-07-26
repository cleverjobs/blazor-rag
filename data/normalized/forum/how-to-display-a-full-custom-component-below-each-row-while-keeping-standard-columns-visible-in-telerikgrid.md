# How to display a full custom component below each row while keeping standard columns visible in TelerikGrid

## Question

**Ken** asked on 25 Jun 2025

Hello, I’m working with the TelerikGrid for Blazor and I have a specific layout need. I would like to display a full custom component (for example, a "MailCard" or a detail panel) under each row of the grid, while still keeping the standard grid columns (like name, date, etc.) visible as usual. I explored the DetailTemplate, which allows me to show custom content per row, but it requires a manual click on the expand (+) button, and I haven't found any official way to auto-expand all rows by default — especially across pages. So my two questions are: Is there a way to embed a full custom component directly within a row, without using the DetailTemplate, while still keeping the columns aligned above? If not, is there a supported method to auto-expand all rows' DetailTemplate by default, even when paging is enabled? Thanks in advance for your help or suggestions. Best regards, Kenzi

## Answer

**Ivan Danchev** answered on 26 Jun 2025

Hello Kenzi, The DetailTemplate is the proper way to display content under the row. The other options such as column and row templates are used to set the content within the cells. With regard to expanding all detail rows, this can be done as demonstrated in this REPL example: [https://blazorrepl.telerik.com/mTYAGqEr02oPGHzu46](https://blazorrepl.telerik.com/mTYAGqEr02oPGHzu46) The approach involves calling the SetStateAsync method for the parent Grid in OnAfterRenderAsync, to expand its rows initially. Regards, Ivan Danchev Progress Telerik
