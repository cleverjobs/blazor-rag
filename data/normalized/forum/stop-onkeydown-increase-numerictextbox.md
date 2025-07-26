# Stop OnKeyDown increase NumericTextBox

## Question

**BenBen** asked on 06 Sep 2023

Hi, I would like to stop the incrementing of my NumericTextBox when I use the keyboard arrows. I use preventDefault, but it doesn't work. <div @onkeydown:preventDefault="true"> <TelerikNumericTextBox Id="test" Width="95%" Decimals="2" Format="C2" @bind-Value="@Test" Arrows="false"> </TelerikNumericTextBox> </div> Can anyone help me? Thanks!

## Answer

**Zachary** answered on 06 Sep 2023

Hi Benoit, If you set the Step property of the TelerikNumericTextBox to "0", that should prevent the number from changing with the up/down arrow keys.

### Response

**Ben** commented on 06 Sep 2023

Thank's Zachary. I want to do the same with the TelerikDatePicker. I don't see any option like Step and I don't think PreventDefault will be my solution. So I come back to the same problem for the date.
