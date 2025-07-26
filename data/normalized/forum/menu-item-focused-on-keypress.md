# Menu Item Focused On KeyPress

## Question

**Jus** asked on 03 Oct 2020

Hello, The last menu item clicked seems to be capturing focus after each keypess when typing in a Telerik textbox control or numeric textbox control with two way binding. After each keypress I have to refocus on the textbox control to keep typing. Is there a work around or am I missing an attribute on the textbox control to make this work correctly? Video: [https://drive.google.com/file/d/1XfvnxtkNUSqMW-XLez2HaPtEBB1AAT28/view?usp=sharing](https://drive.google.com/file/d/1XfvnxtkNUSqMW-XLez2HaPtEBB1AAT28/view?usp=sharing) Sample code: [https://drive.google.com/file/d/18z7asESAl74xzDfxBLVV7PDHnQe3wSwU/view?usp=sharing](https://drive.google.com/file/d/18z7asESAl74xzDfxBLVV7PDHnQe3wSwU/view?usp=sharing) Thanks

## Answer

**Svetoslav Dimitrov** answered on 07 Oct 2020

Hello Justin, Thank you for reporting that to us. As a small thank you, I have awarded you with Telerik Points. I have created a Bug Report on our Feedback Portal regarding this issue, you can see it from this link. I have given your Vote for it to raise the popularity of the item and you can Follow it for email notifications on status updates. As of the time of writing this, I cannot offer any workaround solution. Regards, Svetoslav Dimitrov

### Response

**Justin** answered on 03 Nov 2020

For those interested: A work around is to wrap the menu with a boolean if statement and toggle the boolean with the menus onClick event. Example [https://github.com/uteschj/MenuFocused/blob/master/MenuFocused/Pages/Index.razor](https://github.com/uteschj/MenuFocused/blob/master/MenuFocused/Pages/Index.razor) Your mileage may vary!
