# Select row on key up or down

## Question

**Ada** asked on 19 Feb 2021

Is there a way to select the entire row automatically when a user presses key up or key down?

## Answer

**Marin Bratanov** answered on 22 Feb 2021

Hello Adam, To extend the selection you should also hold down the Shift key. You can find the full list of available shortcuts and see them in action in our online demo for keyboard navigation in the grid: [https://demos.telerik.com/blazor-ui/grid/keyboard-navigation.](https://demos.telerik.com/blazor-ui/grid/keyboard-navigation.) Doing that only on the Up/Down key would create an ambiguous action - the focused row would also change the selection, and such ambiguity is not something we should allow. Regards, Marin Bratanov

### Response

**Danny** commented on 30 Jul 2021

Hello Marin, I think it would not be Ambiguous, since in the WindowsForm Grid it is handled simple with the up and down key, forcing the user to press one more key on the web, as it forces him to do more work, it would be good That will let one get that keyDown event from the grid for one to work at will.

### Response

**Marin Bratanov** commented on 02 Aug 2021

Let's keep this in one of your other threads about this, for example this public one that has several examples: [https://www.telerik.com/forums/how-to-get-a-keydown-event-in-a-row-or-in-the-grid](https://www.telerik.com/forums/how-to-get-a-keydown-event-in-a-row-or-in-the-grid)

### Response

**Paul** answered on 20 May 2022

Hi I want to move a row down while in Inline edit, is this possible? Even when cell is numeric control with its own up and down arrows? This way i can change the value of one column for multiple records fast. This also means that when entering the next cell in the newly selected row must go in Inline edit automatically, and the row i leave must be update automatically. Eric

### Response

**Marin Bratanov** commented on 22 May 2022

Hi Eric, while I am not sure I completely understand the goal, I can suggest a few things to consider depending on what you are after: using OnRead so you can manually modify the order of the rows in the current page (see this as well) based on what custom buttons are clicked in the row see this article on how you can predefine data in the model that you initiate insert for wait for a s preadsheet component as it has a different UX and data goals than a grid that may suit you better (make sure to Vote for that and Follow it if that is the UX you are looking for) consider the InCell editing as it responds differently to key and tab presses
