# Issue with TreeView+Modal

## Question

**Gia** asked on 11 May 2020

Hi I'm using a TreeView and sometimes when I click some nodes I have to open a modal windows that edit some values.. Ths issue is that when the modal window is open I can continue to change node in the treeview located below. Tnx

## Answer

**Marin Bratanov** answered on 11 May 2020

Hello, We are working on fixing the default z-index values on the AnimationContainer (used internally by the TreeView), and the fix will be live with our next release (planned for Wednesday): [https://feedback.telerik.com/blazor/1432348-modal-window-is-behind-treeview-items-and-animationcontainer](https://feedback.telerik.com/blazor/1432348-modal-window-is-behind-treeview-items-and-animationcontainer) Regards, Marin Bratanov
