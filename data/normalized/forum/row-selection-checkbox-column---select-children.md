# Row Selection / CheckBox Column - Select Children

## Question

**Sco** asked on 09 Sep 2020

When using multiple selection in the TreeList... i have the checkbox column as one of the columns and SelectChildren is set to true. The checkbox works great to select its children... but when clicking the row... it only selects the row you click on... and breaks the checkbox select children behavior... i am using 2 way binding for the selected items to preselect certain rows as well.. How can I get the row selection to adhere to the same select children rule of the checkbox column?

## Answer

**Marin Bratanov** answered on 09 Sep 2020

Hi Scott, Would it be useful to you if the row selection could be configured to only work through the checkboxes in the select column, and not through a row click, like we have it requested for the grid here? At the moment, the only other solution I can suggest is hooking to the SelectedItemsChanged event and recursively adding all the required child items to the collection you get as a parameter before populating the SelectedItems of the treelist. Regards, Marin Bratanov

### Response

**Scott** answered on 10 Sep 2020

Yes what you have linked in the grid sounds good... it would be useful to disable clicking the row to check the checkbox especially if the checkbox is set to select it's children.. .because clicking the row won't select the children... I will try to hookup up the SelectedItemsChanged and do it manually... i just thought I read somewhere that if you are using two-way binding for the selected items, you could not also use the SelectedItemsChanged event...hopefully i just misread that...

### Response

**Marin Bratanov** answered on 11 Sep 2020

Hi Scott, I made this page where you can Follow the implementation of such a feature: [https://feedback.telerik.com/blazor/1484271-select-rows-only-with-checkboxes-clicking-the-rows-to-not-affect-selection.](https://feedback.telerik.com/blazor/1484271-select-rows-only-with-checkboxes-clicking-the-rows-to-not-affect-selection.) As for using two-way bindign and the <Parameter>Changed event - the framework does not allow that, the internal way two-way binding works is to use that event already, so you can't use it a second time. You can read more about the general concept here: [https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding](https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding) Regards, Marin Bratanov
