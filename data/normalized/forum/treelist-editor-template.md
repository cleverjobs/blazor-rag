# TreeList Editor Template

## Question

**Ren** asked on 29 Apr 2021

Hi, Is it possible to specify different editor templates for different levels in hierarchical data? What I am trying to do is to build a hierarchical structure for grouping items. The list of items is specified so, in the grouping hierarchy, I want to select an item as the child element of the lowest grouping level rather than typing the name of the item and resolving if it exists. I thus want for the lowest level, to have a combobox rather than an editbox. The data items presented in the treelist have a property to bind to. Thanks for any suggestions. Renier Pretorius

## Answer

**Marin Bratanov** answered on 30 Apr 2021

Hello Renier, I made this public page on your behalf where you can Follow the implementation of such functionality in the component: [https://feedback.telerik.com/blazor/1517790-different-editor-templates-for-different-levels.](https://feedback.telerik.com/blazor/1517790-different-editor-templates-for-different-levels.) If your models already have some distinction (flag) in them, you can already use it with some conditional markup in the editor template. Regards, Marin Bratanov Progress Telerik

### Response

**Renier Pretorius** commented on 30 Apr 2021

Hi Marin, I ended up creating a custom onclick eventhandler for the edit command and based on the level of the relevant item, either return so that the default edit action follows or set the iscancelled flag on the eventarg and launch a modal window with a selection grid. This also enabled me to select multiple items to create multiple child elements in the treelist at the same time. I will bear the conditional markup in mind for future use cases Regards Renier

### Response

**Marin Bratanov** commented on 30 Apr 2021

That's a perfectly valid solution, cancelling a built-in command is a great way to customize the behavior of the component.
