# On Clicking Space Button click event

## Question

**Vis** asked on 24 Aug 2021

Hi, On Clicking Space from Keyboard need to perform Button click event. <EditForm OnValidSubmit="@OnFormValidSubmit" Model="@Model"> <TelerikButton Icon="save" ButtonType="@ButtonType.Submit" Primary="true">Upgrade</TelerikButton> <TelerikButton Icon="cancel" ButtonType="@ButtonType.Button" OnClick="@OnCancelClick">Cancel</TelerikButton> </EditForm> Thanks, Vishnu Vardhanan H

### Response

**Vishnu** commented on 25 Aug 2021

Could you please update on the same

## Answer

**Nadezhda Tacheva** answered on 27 Aug 2021

Hello Vishnu, As per the keyboard navigation configuration of the TelerikButton, once the button is focused, pressing Space or Enter will click it. You can also test that in our live demo - Button - Keyboard Navigation. That being said, with your current configuration, using a TelerikButton in a form, you need to navigate through the form elements (with Tab) to focus the button and then press Space to click it. I hope you will find the above information useful. If you have any other questions, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva
