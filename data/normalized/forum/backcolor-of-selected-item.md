# backcolor of selected item

## Question

**Ran** asked on 09 Nov 2019

Hi, Right now in my treeview the default behaviour seems to be that when the mouse goes over an item it is highlighted and when it leaves it's "unhighlighted". I'd like to be able to have the highlighted state be sticky when a user selects/clicks/expands an item. This is to make it clear to the user which item is currently selected. Currently if the mouse leaves the item, it is no longer highlighted. I guess that would mean that when they move the mouse over other items that are NOT selected there would be 2 items highlighted: the one that is currently selected and the one that is hovered over. So if they clicked on the new item, the "old" selected item gets unhighlighted. I'm certain there is some css gibberish that can do this, but I'm equally certain that my feeble mind can't quite figure it out. Any help would be greatly appreciated. Thanks ... Ed

## Answer

**Marin Bratanov** answered on 11 Nov 2019

Hi Ed, At the moment, the treeview does not have a selection feature. You can vote for and follow its implementation here: [https://feedback.telerik.com/blazor/1427582-select-and-multiple-select-of-items.](https://feedback.telerik.com/blazor/1427582-select-and-multiple-select-of-items.) For the time being, you would need to implement such functionality yourself through templates and you own event handlers, as shown in the comments and linked articles/pages. To get the click events you will need to use templates anyway, and those templates will let you add a conditional class to denote which item is selected. Regards, Marin Bratanov
