# Click area on button

## Question

**Deb** asked on 05 Jul 2022

I have buttons in this app that are wider than the default width. But the entire area of the button does not accept a click. The button is: <div class="col-xl-2 col-md-3 col-sm-12"> <TelerikTooltip TargetSelector="a[title]"> </TelerikTooltip> <a title="Unsubmitting a timesheet will return it to your list of current timesheets."> <TelerikButton IconClass="far fa-undo-alt" OnClick="@(e=> { IsShowPendingConfirmationWindow=true; })" Class="action-button-center">Unsubmit</TelerikButton> </a> </div> The class is: .action-button-center { width: 150px; height: 35px; margin: 0 auto; display: block; text-align: center !important; /* border-radius: 4px;*/ } But only the area indicated in the attached .png is clickable. Is there a way to set the clickable area to the entire button?

### Response

**Dimo** commented on 08 Jul 2022

This looks like HTML/CSS issue. For example, the TelerikButton is wider than its parent and this is what reduces the click area. Or, there is another element over the button. It is not possible for a button to be only partially clickable. The problem must be somewhere else.

### Response

**Debra** commented on 08 Jul 2022

Yes. It was totally my bad and my issue with html. The button was wider than the cell it was contained within. Once I fixed that, that took care of it. Thanks for responding.
