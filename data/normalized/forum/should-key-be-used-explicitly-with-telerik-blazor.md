# Should @key be used explicitly with Telerik Blazor?

## Question

**TedTed** asked on 14 Jul 2022

Hi, the standard Blazor programming docs recommend using the @key marker with components that are generated in a loop at runtime, which would be the Grid, TreeList, etc., however, I have not seen this @key marker used in any of the Telerik Blazor demos or sample code. Is setting of the @key marker done automatically by Telerik Blazor for the Grid, TreeList, etc., or is that something we should be doing somehow as we write apps using these components? Optimising using @key – Blazor University (blazor-university.com)

## Answer

**Dimo** answered on 15 Jul 2022

Hello Ted, We use @key a lot in our source code, especially in data-driven components. We don't (and can't) do it automatically for customer markup, so feel free to use it whenever you are creating components in a loop. Most of our examples don't need @key, but we still use it sometimes, for example for dynamic Grid columns. Regards, Dimo

### Response

**Ted** commented on 15 Jul 2022

Dimo, Thanks for the answer and link. However, I do not think that the linked example is correct. The point of the @key value is to uniquely identify each element in the grid or tree list, independent of its index or position in the list. Obviously setting @key to the index of the element will not serve any benefit and might even cause issues. The @key value needs to be something like a primary key for the element that is unique across all other possible elements in the grid or tree list and is unrelated to the index of the item in the list. For a tree list in particular, there is a <TreeListColumn> element, but I don't have access to the "context" at that element level. How would I set the @key value to an actual instance value (e.g., the Id of the instance at the particular row)? I'm not seeing a way to do this, and I'm now wondering if the TreeList and Grid should have some mechanism to specify the @key value for each element, like a new callback parameter at the TreeListColumn level that passes in the "context"?

### Response

**Dimo** commented on 15 Jul 2022

The column objects don't (and can't) have relationship to data items (rows), because for one column instance there are many rows. Columns don't need such a relationship for unique identification either. You can use anything unique within the columns collection, for example the field names. I will double-check about the @key values and indexes. In the meantime, I am curious if you can break the above example as it is implemented now. I enabled column reordering and index keys seems to work well enough. Column reordering in the UI doesn't reorder the column instances in the Grid declaration. Index @key values may be problematic if a collection of tags (components) is generated in such a way, so that the order of the tags in the loop can change at runtime. I tested this too and still did not break the Grid behavior.

### Response

**Ted** commented on 15 Jul 2022

Dimo, There is a really good example of how the @key value is used to optimize Blazor rendering here: Optimising using @key – Blazor University (blazor-university.com). The @key value should always be a unique value identifying the element independent of the element's index at any given state. The reason is that the index of an item could change between renderings (i.e., drag and drop a row in the tree list), and Blazor will know which exact elements changed based upon the @key value that is independent of the index at any given time. I'm not sure what Telerik Blazor is doing under the covers with the @key value, and I'm not saying that the rendering will completely break with an incorrect @key value, but if you read the above article, it's pretty easy to understand that the @key value needs to be unique across all renderings of the tree list, even when indexes change. I'm not seeing a way to set the @key value in our code in the TreeList for each row. Can you think of a way to do that currently that I'm missing? I want to set the @key value for each rendered row in the TreeList to a value I pull from the "context" for each row.

### Response

**Dimo** commented on 15 Jul 2022

The TreeList rows ( <tr> elements to be specific) already have @keys set internally. The @key value is the data item. The rows are not exposed as declarative components in the TreeList declaration, hence the developer can't set it on their own.

### Response

**Ted** commented on 15 Jul 2022

Dimo, Sweet! That is what I was hoping!
