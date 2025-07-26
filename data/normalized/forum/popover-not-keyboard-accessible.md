# Popover not keyboard accessible

## Question

**Ric** asked on 24 Sep 2024

I am having to do an analysis on the website I am building using your controls and found that the popover control cannot be triggered using the keyboard only (it must be triggered using mouse events, hover or click). Are there any plans to adjust the functionality of this control to bring it into WCAG compliance?

### Response

**Rick** commented on 25 Sep 2024

For additional context, please refer to the following demo: [https://demos.telerik.com/blazor-ui/popover/overview](https://demos.telerik.com/blazor-ui/popover/overview) Use the keyboard to move to a date that has a popup, using the "Enter" key, you will notice that the date gets selected, but the popover does not trigger.

### Response

**Hristian Stefanov** commented on 26 Sep 2024

Hi Rick, I can confirm that the Popover can be triggered by pressing the Enter key on a button by setting its ShowOn parameter to PopoverShowOn.Click. You can try it out with this example: REPL link. Test it by focusing on the button using the Tab key and press Enter to see the result. As for the Calendar example you mentioned, it's an exception because the popover is toggled using the standard onclick event attached to an inner HTML element within the cell. In this case, the focus remains on the outer wrapper (the <td> element), preventing the Enter key from triggering the click event on the child element. This behavior is expected. Kind Regards, Hristian
