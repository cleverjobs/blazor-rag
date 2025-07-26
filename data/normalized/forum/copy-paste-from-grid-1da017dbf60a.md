# Copy/Paste from grid

## Question

**Lar** asked on 17 Mar 2021

When drag my mouse over the text in a grid row to copy/paste into an excel spreadsheet, the font is Arial size 4. In this scenario I wouldn't be using the export to Excel feature (although I've turned that on for users that want to do that), a user just wants to copy and paste a single row in the grid. Is there a way to change how 'default' font & size when doing this? I don't view this as a major issue, just trying to save a few clicks for the end-users that want to copy/paste in this way.

## Answer

**Marin Bratanov** answered on 18 Mar 2021

Hi Larry, Copying from the browser is not something that we can control, the browser and the OS have full control over that. Browsers copy all the styles of an element and it paste them in apps that support rich text (such as web pages, Word, Excel) - in recent years Chromium even includes the background-color of the <body> not just of the element you selected. I am not aware of a way to stop this, I'm afraid, and it seems people aren't either - the "solutions" revolve around using Ctrl+Shift+V to paste as plain text, or using clipboard manager tools to do that paste-as-plain-text, or pasting in notepad first (which simply does not support rich text) - example StackOverflow thread. That said, there is an idea you can consider - adding a button that will put the desired content as plain text in the clipboard. For example, by taking the selected rows of the grid, serializing their models to tab-separated content (this is what Excel copies and can also paste). You could, for example, integrate this into a context menu of the grid row if you want it specific to a row. You can also Follow this enhancement idea where the grid could do something like that for you. The downside is that it will be quite difficult to put the actual user selection in the clipboard, and that would work better with serializing the entire row models. Besides, it will require some shift in the way the user interacts with the page and that may not always happen, some people will keep using Ctrl+C and Ctrl+V. Regards, Marin Bratanov Progress Telerik
