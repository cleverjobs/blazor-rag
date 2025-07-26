# Panelbar expand and collapse on a property instead of Expanded items list of objects

## Question

**Eri** asked on 23 Apr 2024

Is it possible to have the panel bar expand or collapsed based on a property (bool IsExpanded) for the list of items in the data property of the panel bar, instead of as a separate list of items bound to the ExpandedItems list of objects? I have a separate component with expand and collapse buttons. I have a global list of objects that are in a service. The Data property of the panel bar is set to this list of global items. When the Expand All button of the separate component is clicked, it sends a message to the application service to set an Expand for all items in the global list that is bound to the panel bar. The service sends out a notifystatechanged event. The problem is I do not want to maintain a completely separate list of objects just for which ones are in the ExpandedItems list. Would be nice to simply bind the expanded to a property of the global object thereby having the statechanged change the expanding and collapsing of the items in the panel bar. Is this possible? Haven't seen anything in documentation that seems to allow this. Right now it means that my application wide service needs to have a completely separate list of objects for the expanded items in this one panel bar component, so it can add and remove objects and then notifystatechanged back to the panel bar component. If not, is there any other way of doing this to have the panel bar get notified so it can then add and remove the expanded items object list? Please advise Thanks

## Answer

**Svetoslav Dimitrov** answered on 26 Apr 2024

Hello Eric, You are correct, currently, the PanelBar expands and collapses its items via the ExpandedItems collection and does not expose a field such as the ExpandedItemField. From what I understood you use buttons to expand and collapse items. When a button is clicked you manipulate the ExpandedItems collection and notify the PanelBar that a change has occurred. I can confirm that this is a good approach to achieving the desired behavior. At that point, I might say that changing how expanding and collapsing the items in the PanelBar works is a breaking change that will affect everyone who uses the component. We are always mindful when introducing breaking changes that will affect practically all of our clients who use the component. Regards, Svetoslav Dimitrov Progress Telerik
