# Modal on Modal

## Question

**Gia** asked on 28 Apr 2020

Hi I need to use a modal window with a grid inside that But I need to show a modal window on error when I edit items on grid Modal on Modal not work: the second window is not visible. Any solution ? Tnx

## Answer

**Marin Bratanov** answered on 28 Apr 2020

Hi Giampaolo, You can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1407791-support-for-multiple-nested-modal-windows.](https://feedback.telerik.com/blazor/1407791-support-for-multiple-nested-modal-windows.) Regards, Marin Bratanov

### Response

**Giampaolo** answered on 28 Apr 2020

OK tnx But ad idea can be to hide the original window and open another one But how is possible leave the grid in edit mode ? And after that continue with edit the cell ?

### Response

**Marin Bratanov** answered on 28 Apr 2020

Hello Giampaolo, If you hide the first dialog with the Visible parameter, it will remove its child components from the render tree and Blazor will dispose them, so you couldn't keep the grid in it "alive". Perhaps you can try to add a Class to it that is conditional, and raise a flag when the grid goes into edit/insert mode (that is, when the second modal is to show up) and try to set its display CSS rule to none. I posted a sample workaround like this in the

### Response

**Jeff** commented on 27 Apr 2021

Can you post a link to the "

### Response

**Marin Bratanov** commented on 28 Apr 2021

Hi Jeff, Here is the link to the original request for the original problem in this thread: [https://feedback.telerik.com/blazor/1407791-support-for-multiple-nested-modal-windows.](https://feedback.telerik.com/blazor/1407791-support-for-multiple-nested-modal-windows.) The feature is already available in our latest release and I recommend you simply upgrade to it (2.23.0 at the time of writing). As for hiding the window which seems to be what you need to behave differently - it is supposed to destroy all its content, this is how Blazor is supposed to operate. Implementing the following feature will let you prevent the disposal of the content: [https://feedback.telerik.com/blazor/1496745-minimizing-the-window-should-be-done-with-css-only-to-avoid-lost-content.](https://feedback.telerik.com/blazor/1496745-minimizing-the-window-should-be-done-with-css-only-to-avoid-lost-content.) I've added your Vote to it to raise its priority, and it contains a workaround too. --Marin
