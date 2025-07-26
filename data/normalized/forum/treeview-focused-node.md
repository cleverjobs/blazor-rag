# Treeview: Focused Node

## Question

**Hen** asked on 27 Jun 2024

The node of a treeview loses its focus and emphasis if another control element receives the focus. How can I keep the selected entry permanently?

### Response

**Dimo** commented on 01 Jul 2024

Hi Hendrik, The TreeView relies on standard browser focus behavior. There can only be one focused element on the page, so it's expected for the TreeView to lose its focus state when the user clicks or tabs somewhere else. On the other hand, the item selection is persisted as long as you use @bind-SelectedItems or update the collection in SelectedItemsChanged.

## Answer

**Hendrik** answered on 01 Jul 2024

Thank you Dimo, the hint with the SelectedItems did the trick !!!!
