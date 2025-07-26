# Displaying a nested collection

## Question

**Mar** asked on 20 Sep 2021

Hi: Several of the columns I'm trying to display in the grid are collections of strings or integers. Will I need to convert those collections to a string format, for example, comma-separated before the data is presented to the grid? Thanks

## Answer

**Kristian** answered on 23 Sep 2021

Hi Marc, You can either create a new property that normalizes the collection as a string and pass the property to the grid or you can pass the collection and add a template that tells how the collection should be rendered. Both approaches are valid and each of them has pros and cons. It mostly depends on do you want the grid to work with only local data (all of the data is already preloaded in the grid) or you want to filter/group/sort remotely (in the API or DB) The option with the string will give you filtering, grouping and sorting of these strings out of the box, but these operations will work only with the loaded data. If you try to pass the filter/sort/group to a remote server or DB, it won't work since they don't know the normalized property. On the other hand, directly passing the collection will require writing custom code for the sorts and filters, but once it's implemented, the filters and sorts could be sent to a remote server and it will work as expected. Keep in mind that if you want to edit the column, you may want to implement a custom editor template since the default editor won't fit the collection type. Regards, Kristian Progress Telerik
