# Exporting to Excel/CSV - Export both the current grid and another sub-grid

## Question

**Jef** asked on 07 Jan 2025

Hi, I am wondering if anyone has attempted this before and if it's possible. I have a use case where a user can click on a grid to expand details about that row, which shows as another grid. For example, in the image I have, I expand this row, and it shows a new grid below. When I choose export, I want to be able to export the rows I'm viewing as usual, but underneath each of those rows I want to also include the sub-grid rows. So for example, if an object has two sub-items in its sub-grid, the export for two objects would look like: Object 1 Sub Item 1 Sub Item 2 Object 2 Sub Item 1 Sub item 2 I'm assuming I have to do something under OnBeforeExcelExport to stage this, but how would I go about doing it? I have no idea what the syntax in this case should look like (as a matter of fact I don't quite understand what's going on in the default version of the method). Any help is appreciated!

## Answer

**Hristian Stefanov** answered on 08 Jan 2025

Hi Jeff, The Hierarchical Grid utilizes the DetailTemplate to display its child Grids. However, when it comes to exporting functionality in the Grid component, templates are not included in the export because the framework does not provide a way to retrieve them at runtime. This limitation is documented in the Notes section of the Export article ( see the second bullet point ). That said, a workaround is available to achieve custom hierarchical exporting functionality using the SpreadStreamProcessing library. For demonstration, you can refer to the following runnable project: Telerik Grid - Export to Excel Hierarchy. Regards, Hristian Stefanov Progress Telerik

### Response

**Jeff** commented on 08 Jan 2025

Hi Hristian, thank you for your reply. I'm still a bit confused, and unfortunately I'm not even sure where to begin to implement the SpreadStreamProcessing library into my application. Additionally, I should note that my two grids are actually not a hierarchy, but rather two entirely separate grids - when the user expands the row in the first grid, it's making an api call that generates a list of data relevant to the first grid item, and then displays that in a second grid. In other words, they are from two totally different models, so I'm not sure if this will work for me. Is there instead someway to perhaps insert data into an excel export, given that I already have the second list of data? For example, if I know that every object in List1 has associated objects organized in a List2, would it not be feasible to just set up the Export somehow so that it exports List1 and List2, without really referencing the grids, or is that not possible? Or at very least, insert some objects from List2 in between the default operation of exporting List1?

### Response

**Hristian Stefanov** commented on 09 Jan 2025

Hi Jeff, Thank you for clarifying your scenario and providing additional details. Although you are not using an actual hierarchical Grid but instead have two separate Grids, hierarchical Excel export still requires creating the Excel file manually using the Telerik Document Processing library. The project I previously linked demonstrates this approach. Additionally, here’s another example that showcases a similar method: Spreadsheet Binding Example. While this example uses the Spreadsheet component, the general approach applies to the Grid as well, as long as you can provide the data from both of your Grids. Please refer to the CreateExcelFileFromIEnumerable method in the example to see how the manual Excel file creation is implemented. In summary, exporting data to an Excel file from multiple Grids requires manually generating the file and passing the data from both components. If you encounter any challenges with the Telerik Document Processing library, ensure that you set the "Product" section of your ticket or forum post to " Telerik Document Processing." This will direct your question to the responsible team, who can provide specialized guidance for the library. Kind Regards, Hristian
