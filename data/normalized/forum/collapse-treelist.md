# Collapse Treelist

## Question

**Pet** asked on 14 Dec 2023

Hello! I am using Telerik.UI.for.Blazor version 5.0.0., I have a page with a treelist. I want all items to be collapsed when the page is loaded and the treelist is displayed for the first time. How do I do this?

## Answer

**Georgi** answered on 18 Dec 2023

Hello, Petteri, You can configure the expanded state of the items through the TreeList State. The TreeList exposes two state events: OnStateInit - fires when the TreeList is initialized. OnStateChanged - fires when the user makes a change to the component's State, like sorting, filtering, paging, editing and so on. To collapse all items on initialization, handle the OnStateInit event and pass an empty collection to the ExpandedItems field of the state object. See an example here: [https://docs.telerik.com/blazor-ui/components/treelist/state#set-treelist-options-through-state.](https://docs.telerik.com/blazor-ui/components/treelist/state#set-treelist-options-through-state.) Let me know if additional information is needed. Best regards, Georgi Progress Telerik

### Response

**Petteri** commented on 19 Dec 2023

Yes, that works. Thank you very much!
