# Two way binding to SelectedItems and to SelectedItemsChanged event at the same time

## Question

**Moh** asked on 23 Sep 2020

Hi, Can I have two way binding to SelectedItems and to SelectedItemsChanged event at the same time like the followings: <TelerikTreeView Data="Items" @bind-SelectedItems="SelectedItems" @bind-SelectedItems:event="SelectedItemsChanged"> <TreeViewBindings> <TreeViewBinding IdField="Code" TextField="Title" /> </TreeViewBindings> </TelerikTreeView> working? As Blazor allows binding to event handlers by convensions?

## Answer

**Marin Bratanov** answered on 23 Sep 2020

Hello Mohammad, The framework does not allow using both two-way binding and the bindable event at the same time. You can read more about this here: [https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding](https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding) Regards, Marin Bratanov
