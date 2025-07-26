# disable underlying component

## Question

**n/an/a** asked on 29 Mar 2022

Hello, I have a parent component that holds a pop up window. When the window pops up (is visible) then the parent component becomes disabled (no user interaction with the parent - underlying component - is possible). Within this window, I have another Dialog window that will pop up upon closing the window, if a certain condition is not met. When this Dialog pops up, the underlying component (which in this case is the pop up window) doesn't become disabled. Instead, the effect will take place again on the parent component. How would I make the 'disable' effect take place on the window located in the parent component, and not on the parent component, upon the popping up of the Dialog? Thank you.

## Answer

**Marin Bratanov** answered on 29 Mar 2022

Hello, Check if you are hitting this issue: [https://feedback.telerik.com/blazor/1515146-predefined-dialogs-don-t-cover-a-modal-dialog-when-the-telerikrootcomponent-parent-does-not-have-display-flex](https://feedback.telerik.com/blazor/1515146-predefined-dialogs-don-t-cover-a-modal-dialog-when-the-telerikrootcomponent-parent-does-not-have-display-flex) and if so - whether the workaround helps. You can then click the Vote and Follow buttons to raise its popularity and get status update emails. Regards, Marin Bratanov Progress Telerik
