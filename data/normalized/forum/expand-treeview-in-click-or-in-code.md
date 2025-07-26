# Expand TreeView in click or in code

## Question

**Mar** asked on 05 Nov 2021

Hi setting the Expanded property of the node object don't expand the selected node. Do I really need to load everything again to expand a node? I need to trigger the click event and expand a node in code. As a minimum I would like to expand a node on click if it has children

### Response

**Marin Bratanov** commented on 06 Nov 2021

With this, a better way through a collection will become available: [https://feedback.telerik.com/blazor/1448095-expanded-items-handling-feedback-requested](https://feedback.telerik.com/blazor/1448095-expanded-items-handling-feedback-requested) Through this, item properties will be tracked to cause a rerender: [https://feedback.telerik.com/blazor/1498147-track-changes-in-properties-when-treeview-is-bound-to-observable-collection](https://feedback.telerik.com/blazor/1498147-track-changes-in-properties-when-treeview-is-bound-to-observable-collection) I've added your Vote for both of them to raise their popularity, and you can click the Follow button for status updates emails.
