# Need example or suggestions for editing nodes of hierarchical data (json)

## Question

**Bit** asked on 16 Oct 2019

Have a need that might be able to handle it with a Treeview. Need to allow a user to edit a few nodes of a json file, then save the changes. treeview demo Found this javascript-based example of editing json in the browser. Probably more features than I need. [https://github.com/josdejong/jsoneditor](https://github.com/josdejong/jsoneditor) If nothing else, I think with the Blazor Treeview as-is, could I use the following approach? - Load json data into the tree structure - Place a single input field somewhere near the tree (eg. at the top) - Use a template of some sort that includes an "onclick" event - The onclick event loads the item text or value into the input field for editing - Provide a "save changes" button that takes current values of the data in the tree, serializes back to json and saves over the top of the file. Sound reasonable?

## Answer

**BitShift** answered on 16 Oct 2019

Or better-yet, two-way binding from a json file? Would like to see an example of this, if possible.

### Response

**Marin Bratanov** answered on 17 Oct 2019

Hi, The treeview (and the rest of our data bound components) require a collection (usually something that inherits IEnumerable) to bind to. It is then up to the application to provide that collection, and the underlying data source can be anything - JSON files, a remote WebAPI endpoint, a local service (e.g., with a SQL database) and so on. On editing - at the moment only the grid offers editing abilities and this is done through events - you receive the new data in the CRUD events so you can transfer it to the underlying data source the application uses. The same would hold true for such an editing in the treeview - you need to provide it with a collection of models so it populates. You can have the desired buttons or click handlers in the template of the items, and use the project logic to update the data source. The tricky part for the time being may be updating the treeview data, so you may want to Follow and Vote for this feature: [https://feedback.telerik.com/blazor/1433824-binding-to-observablecollection.](https://feedback.telerik.com/blazor/1433824-binding-to-observablecollection.) In the meantime, you may want to try the approach for updating the data from my post on 19 Jun 2019 from the following thread: [https://feedback.telerik.com/blazor/1409112-the-grid-does-not-update-on-data-source-change.](https://feedback.telerik.com/blazor/1409112-the-grid-does-not-update-on-data-source-change.) Regards, Marin Bratanov
