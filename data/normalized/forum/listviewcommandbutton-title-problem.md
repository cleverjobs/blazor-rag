# ListViewCommandButton Title Problem

## Question

**BobBob** asked on 06 Oct 2020

The Title attribute on the ListViewCommandButton does not appear to work. I have a button defined like this: <ListViewCommandButton Command="Edit" Enabled="@Ticket.Active" Class="float-right ml-1" Icon="@IconName.Edit" Title="Edit"></ListViewCommandButton> When it renders, the title attribute is not being added to the button: <button class="float-right mr-1 k-button telerik-blazor k-button-icon" tabindex="0" aria-disabled="false" type="button"> <span class="k-icon k-i-edit"></span> </button>

## Answer

**Svetoslav Dimitrov** answered on 07 Oct 2020

Hello Bob, Thank you for reporting that to us. As a small token of appreciation, I have awarded you with Telerik Points. I have created a Bug Report on our Feedback Portal on your behalf and added your Vote. You can see it from this link. In the bug report, I have posted a workaround solution for the time being. That being said, this fix will be part of our next release, which will hopefully be live by the end of the month. Regards, Svetoslav Dimitrov
