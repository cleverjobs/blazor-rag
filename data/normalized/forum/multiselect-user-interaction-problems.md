# MultiSelect user interaction problems

## Question

**gfk** asked on 17 Feb 2022

Customer feedback about the TelerikMultiSelect is that it is not obvious about how to interact with it. Note that we are using it like a traditional ComboBox, the user does not expect to type into the control or use the search facility. There are only modest numbers of items so it's easiest to just open the list and select items. The following usage problems have been noticed: The control initially looks like a TextBox and when the cursor moves over it, it changes to a beam and the user thinks they are supposed to type something. Typing does open the list and attempt to find a match, but the users aren't using that feature. Clicking in white space opens the item list. It's not obvious this gesture is needed. As items are selected, the remaining white space in the control has unpredictable size, and it can become small (see attached png). You have to carefully click in the white space to open/close the list. Items 2 and 3 are the most irritating. As a workaround, I was considering putting a small button to the right of each MulitSelect, then clicking that button would toggle the open/close state. This would create the mock appearance of a ComboBox. However I can't find any way of toggling the open state in code. Any comments or suggestions on these points would be very welcome. Greg
