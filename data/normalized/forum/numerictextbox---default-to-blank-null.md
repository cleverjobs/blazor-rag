# NumericTextBox - Default to blank/null

## Question

**Cod** asked on 29 Mar 2022

I am attempting to utilize TelerikNumericTextBox, rather than TelerikTextBox, in order to take advantage of the Min, Max, Format, and other features available. However, upon making the switch I am no longer able to display a blank/null value in the textbox. I don't see any mention of this in the TelerikNumericTextBox docs ( [https://docs.telerik.com/blazor-ui/components/numerictextbox/overview](https://docs.telerik.com/blazor-ui/components/numerictextbox/overview) ) and I assume this behavior is by design. Is there a way to allow a TelerikNumericTextBox to have a blank/null value? Perhaps a TelerikMaskedTextBox would work?

## Answer

**Marin Bratanov** answered on 29 Mar 2022

Hello Cody, You can use a nullable number, here's a basic example: [https://blazorrepl.telerik.com/QckdwNFZ370XdMPV03](https://blazorrepl.telerik.com/QckdwNFZ370XdMPV03) Regards, Marin Bratanov Progress Telerik

### Response

**Cody** commented on 29 Mar 2022

Fantastic, Marin - Thank you! One "?" is all I was missing ... great catch.
