# Multi Column Headers with a border in Excel download

## Question

**Dea** asked on 20 Jan 2025

In the attached solution I have two Multi Column Headers - Product (containing ID and Product Name) and Details (containing In Stock, Unit Price, Discontinued and Release Date). I want the Excel download to reflect this, and to have a black border around all cells. By default the multi column headers just take a single cell, it looks like this: If I use worksheetExporter.MergeCells to merge the Product and Details cells, it looks better, but the border is gone from the right hand side of Details. Can you advise how I can see the cells merged correctly but retain the border? Thanks in advance, Dean

### Response

**Nadezhda Tacheva** commented on 23 Jan 2025

Hi Dean, During the built-in export, we generally merge the multi-column headers by design. See this example for reference: [https://blazorrepl.telerik.com/cpEPGHPP59kJMgsE04.](https://blazorrepl.telerik.com/cpEPGHPP59kJMgsE04.) I believe cells get mixed up while you are iterating them with the SpreadStreamProcessing and then you need to manually merge them. It is most likely possible to add the border to the desired cells that are missing it. However, I think there may be an easier and simpler solution for the behavior you want to achieve. You may consider using the SpreadProcessing library instead (see example here ). It is a bit simpler as you can directly import the stream to a Workbook and you don't need to create it manually. I will modify your app to showcase the difference and I will send it additionally by tomorrow.

### Response

**Nadezhda Tacheva** commented on 24 Jan 2025

Hi Dean, While preparing the example, I found some issues using the SpreadProcessing library in Interactive WebAssembly rendering mode. More specifically, the problem is with the import of the stream to a workbook. I will additionally revise this matter with the Document Processing team but if your actual app uses Interactive WebAssembly rendering mode, it will not be possible to use the SpreadProcessing to achieve the desired result for the time being. As for the current approach of using the SpreadStreamProcessing, I got some more details from the Document Processing team on the current behavior. It appears that this is expected as SpreadStreamProcessing skips the empty cells. Thus, when you are iterating the first row, only the Product and Details cells are taken into account and this is why only they have borders. Then, after the cells are merged with their right ones that don't have a border. The only option I can suggest is to go through the cells after the merge and apply the border to all cells again.

### Response

**Dean** commented on 28 Jan 2025

Are you able to help me with the idea of going through the cells after the merge and applying the border to all cells again? When I try this the cells get unmerged and I am back to square one.

### Response

**Yoan** commented on 31 Jan 2025

Hello Dean, My name is Yoan, from the Document Processing team and I am joining this discussion to address your latest questions. The results you are experiencing with the current implementation are expected. That is due to the nature of the SpreadStreamProcessing library and its optimization for performance. The rowImporter.Cells (for the first row) collection contains only the two cells with values (" Product " and " Details "). This is why the format is successfully set to them but the rest of the cells are skipped because they are not in the collection in the first place. Additionally, merging a selection of cells does not transfer the format of one cell to the rest which is why some neighboring borders are lost. One more thing to keep in mind is that the execution order of the commands is really important. The Merge operation must be the last operation before disposing of IWorksheetExporter, so the cell format must be set beforehand, to all cells that are going to be merged, even the empty ones. With all that context in mind, I am attaching for your disposal a modified project that takes this into consideration and uses an alternative approach, to determine the rows and cells that need formatting. Feel free to test and examine it for yourself and do not hesitate to let me know if you have any questions. I remain at your disposal in the meantime. Regards, Yoan
