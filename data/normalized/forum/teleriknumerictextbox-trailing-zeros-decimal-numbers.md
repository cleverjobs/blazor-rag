# TelerikNumericTextBox trailing zeros decimal numbers

## Question

**Alb** asked on 10 Oct 2021

Hello, how can I remove the trailing zeros from the editor? Is possible to use the same format (###,##0.00###) when editing the value? right now when the value of the field is read from the database (is a decimal 18,5) and the value is for example 1,00000 (just one with 5 zero after decimal separator) then the textbox is formatted right (1,00) but when editing it is 1,00000. I hope the question was clear, sorry. thank you <TelerikNumericTextBox Width="100%" @bind-Value="docum.rigadoc.prezzo" Class="rightAlign" Decimals="5" Format="###,##0.00### €" Min="0" Max="99999999"> </TelerikNumericTextBox>

## Answer

**Alberto** answered on 10 Oct 2021

Thanks, for now I resolved normalizing the decimal fields so they display correct

### Response

**Marin Bratanov** answered on 10 Oct 2021

Hi Alberto, You need to set Decimals to 2 - that controls how many decimal symbols you see when editing. Right now it is set to 5 in the provided snippet, so you get 5 decimal places when editing. An extract from the documentation (I marked the key points in bold ): Decimals - how many decimal places will be allowed while the user is typing a new value. Takes effect only while the input is focused. The default value is set from the specified culture. Format - the format with which the number is presented when the input is not focused. Read more in the Standard Numeric Format Strings in .NET article. Regards, Marin Bratanov

### Response

**Alberto** commented on 10 Oct 2021

I wasn't clear, I want the user to be able to input 5 decimals, but the first time the value is assigned there are 5 zero decimals, and after the first edit the unwanted zeros are disappeared, I want that on the first edit the number is formatted right, if it is 1,00000 then should appear 1,00 and not 1,00000. In the example the value of the docum.rigadoc.prezzo is 14,00000m, maybe a video is more clear <blockquote class="imgur-embed-pub" lang="en" data-id="a/C5P4qcN" data-context="false"><a href="//imgur.com/a/C5P4qcN"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>

### Response

**Marin Bratanov** commented on 10 Oct 2021

If you want to guarantee a certain appearance (e.g., certain amount of zeroes), you can use the Masked Textbox component: [https://demos.telerik.com/blazor-ui/maskedtextbox/overview.](https://demos.telerik.com/blazor-ui/maskedtextbox/overview.) The numeric textbox relies on the framework parsing operations and string operations, so once you remove meaningful digits from the actual number, its string representation will no longer contain them either. This is not something we can or should change, as it stems from the framework.
