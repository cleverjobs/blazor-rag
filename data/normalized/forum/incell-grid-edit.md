# Incell grid edit

## Question

**RobRob** asked on 06 Jun 2023

I've use the Telerik WPF grid for years and have recently started to move away from WPF dev. to Blazor dev. In WPF to instigate an edit the user can click a row, then double click a cell and start to edit it which works perfectly because selection of the row(s) can not start an edit. In Blazor the Incell grid edits are started as soon as the user clicks the grid removing the option to select one or many rows. My applications require both of these interactions but this method of grid edits doesn't seem to be compatible with selection of rows etc. Is there any way of changing the behaviour of how these Incell grid edits are started? (ideally in the same way the WPF version in cell edits work) or are there likely to be ways of changing this behaviour in future with newer updates? Many thanks, Rob

## Answer

**Radko** answered on 08 Jun 2023

Hello Rob, Indeed, both the incell edit and row selection are triggered by a click within a cell. If you do require both, then one solution is to do selection through a checkbox column, as described in the following article: Grid Selection - Notes on Editing. If you would indeed like to keep the behavior from your previous app and prefer triggering both actions, If you would like to keep the behavior from your previous application, then you should be able to achieve what you are after by hooking to the various events the TelerikGrid exposes. We have a knowledge base article that demonstrates how to simultaneously trigger both actions: Row Selection in Edit with InCell EditMode. If I understand correctly, the behavior you are after is slightly different from the one in this article, as you would like for the first click to trigger selection, while a second click on an already-selected item to trigger edit, but hopefully this example will serve you as a base. Regards, Radko
