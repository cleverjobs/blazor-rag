# In the Prompt dialog, difference between clicking Cancel and OK with nothing entered

## Question

**Dou** asked on 20 Sep 2021

The documentation states, " The prompt dialog returns a string that the user enters when they press OK, and null when they press Cancel." However I've discovered that null is returned when the user clicks cancel, and also when they click OK without entering anything. So I can't tell whether they clicked OK or cancel. If they click OK without entering anything, that's not valid in my scenario but I can't tell whether to validate it because maybe they clicked cancel. Any way to determine which button was clicked?

## Answer

**Nadezhda Tacheva** answered on 22 Sep 2021

Hello Doug, Indeed, at this stage pressing Cancel or OK with an empty textbox cannot be differentiated as the returned result is null in both cases. OK with an empty textbox should return string.Empty. The following bug report in our public feedback portal covers this scenario - Differentiate Cancel and OK with an empty textbox. I see you already voted for it, you may also follow it to keep in track with its progress. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva Progress Telerik
