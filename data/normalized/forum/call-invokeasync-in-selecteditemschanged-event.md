# Call InvokeAsync in SelectedItemsChanged event

## Question

**Flo** asked on 09 Jul 2020

Hello, I have blazor grid inside my custom component. I need to call InvokeAsync method on my EventCallback passed to this component. When I do that from SelectedItemsChanged event app gets crashed without any exception. I read the docs about async operations in this event ([https://docs.telerik.com/blazor-ui/components/grid/selection/overview#asynchronous-operations),](https://docs.telerik.com/blazor-ui/components/grid/selection/overview#asynchronous-operations),) but don't know how to workaround this.

## Answer

**Marin Bratanov** answered on 09 Jul 2020

Hi Tomasz, If you want to load that data on demand, you should use the OnRowClick event. The linked page contains a sample. Let me know how that works for you. Regards, Marin Bratanov

### Response

**Flotman** answered on 09 Jul 2020

I am not loading data on demand. I am using checkboxes (GridCheckboxColumn) to select items in grid (multiple selection), and when item is selected I need to call InvokeAsync on my EventCallback (with selected ids). I could use OnRowClick but how can I deal with "Select All" checkbox ?

### Response

**Marin Bratanov** answered on 09 Jul 2020

Hi Tomasz, Technologically, this may not work. It's not that errors are thrown, but that the framework does not repaint all the content. Since the originator of the event is the grid, that's all that might be repainted in this case. What you could do is to use a custom column where you can control the HeaderTemplate and respond to its clicks on a checkbox there in your own code. This will change the context of the event execution and you will be able to repaint the page. You can also alter the SelectedItems collection that the grid is bound to. Regards, Marin Bratanov

### Response

**Flotman** answered on 10 Jul 2020

How can I alter SelectedItems collection. It would be perfect if I could bind SelectedItems to collection with ids (from my grid Data model of course) only (IEnumerable<int>). All samples from [https://docs.telerik.com/blazor-ui/components/grid/selection/multiple](https://docs.telerik.com/blazor-ui/components/grid/selection/multiple) assumes that SelectedItems model is same type as Data model.

### Response

**Marin Bratanov** answered on 10 Jul 2020

Hi Tomasz, The SelectedItems is a collection of models. That's what people expect from the grid. So, to set them, you must: set the SelectedItems parameter of the grid to the corresponding collection (you can use one-way or two-way binding) populate the collection in the view-model as desired (e.g., by extracting the models from the grid data source by the IDs you have) Not all models have int32 IDs like that - often enough IDs for a model are GUIDs, strings, other integer types (such as long), or even other objects, which is why the grid lets you handle that according to your data. Regards, Marin Bratanov
