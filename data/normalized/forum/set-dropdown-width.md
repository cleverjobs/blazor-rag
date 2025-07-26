# Set DropDown Width

## Question

**Cam** asked on 26 Feb 2021

Is there a way to set the size of the dropdown for the datetime picker? I have complaints from users where when they are changing between different months and the position of the arrows move due to different lengths of month names. This causes them to accidently click the "Today" button and lose their selection. Any help is appreciated.

## Answer

**Marin Bratanov** answered on 26 Feb 2021

Hi Cameron, You can use the PopupWidth and PopupHeight parameters, for example: <TelerikDatePicker @bind-Value="@TheDate" PopupWidth="400px"> </TelerikDatePicker> @code{
DateTime TheDate { get; set; }=DateTime.Now;
} Regards, Marin Bratanov

### Response

**Cameron** answered on 26 Feb 2021

Marin, Thanks for the quick and helpful response, as always! Missed that on the docs page the first time, but I see it now.
