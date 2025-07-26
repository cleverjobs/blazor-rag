# TreeView parenting, children and checked items

## Question

**Ram** asked on 28 Apr 2023

Hello, both in the docs and demos, the text says (emphasis mine) "the ParentId field which points to the Id of the item that will contain the current item", yet the model shows the field as "public int? Parent { get; set; }" without the Id at the end? Seems like one or the other is wrong? Also I don't see any mention if the Id fields have to be specifically int, or if they could be string for.ex.? Edit.: It actually seems that you can set the name of the ParentId Property, and that is done in the examples I linked. Still a bit confusing for people like me who don't read the whole thing. Secondly, would be nice if I didn't have to "pollute" my models with the "HasChildren" property. The TreeView is obviously looking at some things in the data (for.ex. it's looking for the one item with null as Parent and if the HasChildren is true, it's looking for them) so would be great if it would look through the data and see if there are children for a given item automatically. Now it feels I have to tell it twice, first with the Id/ParentID properties and secondly with HasChildren. Thirdly, currently the TreeView exposes the items that have been checked as the bindable CheckedItems collection. For this I think it would be easier if we could configure something like "my model has the boolean property ThisItemIsCheckedNow, use that as the checked indicator" and then, when checking items, that given property on the model would be true or false as the UI checkbox is checked/unchecked.

## Answer

**Dimo** answered on 02 May 2023

Hello Rami, Yes, "ParentId" is the default value of the Parent IdField parameter and you can change it. I agree the article is a bit confusing and we will fix it shortly. HasChildren is required for load-on-demand and flat data scenarios. If you use hierarchical TreeView data, you can omit it. We used to expect checkbox-related and expand-related properties in the TreeView model. However, this was inconsistent with our other components (e.g. Grid SelectedItems, etc.) and also, one could argue that it was "polluting" the model, so we changed the architecture. It doesn't make complete sense to keep UI-related information in the data. Regards, Dimo Progress Telerik
