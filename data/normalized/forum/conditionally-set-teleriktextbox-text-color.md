# Conditionally set TelerikTextBox text color?

## Question

**RobRob** asked on 14 May 2025

I'm trying to programmatically set the Text color of TelerikTextBox. Problem I'm running into is that the Class being defined for the TelerikTextBox is based on CSS from TailwindCSS. I was hoping I could just add color: as a parameter but that would only work if using a "Style" not "Class" and TelerikTextBox doesn't support Style. <style>.safeText { color: black;
}.warningText { color: red;
} </style> <TelerikTextBox Id="emptyReleaseOn" Class="form-display sm:text-sm sm:leading-5 text-center @(_expireColor)" Size="12" Value="@_currentBookingMTYRelease" ReadOnly="true" Width="6rem"> </TelerikTextBox> Note: the above @(_expireColor) is not valid syntax to be used in Class attribute ... so not really sure how to go about this? Code server-side: private string _expireColor { get; set; }="safeText"; if (DateTime.TryParse(_currentBookingExpiresOn, out var expireDateValue))
{ if (DateTime.Now> expireDateValue)
{
_expireColor="warningText";
}

} I found Telerik sample code here, but that's not what I'm trying to accomplish (need to retain the TailwindCSS). Is there an easy way to accomplish this? Rob.

## Answer

**Will** answered on 14 May 2025

Something I've done to achieve similar results is to use a function that returns a string with all needed css classes concatenated, and consume the function in the Class parameter of the text box. if (DateTime.TryParse(_currentBookingExpiresOn, out var expireDateValue))
{ if (DateTime.Now> expireDateValue)
{
isExpired=true;
}

} string GetClass ( bool isExpired )=> isExpired ? "form-display sm:text-sm sm:leading-5 text-center warningText": "form-display sm:text-sm sm:leading-5 text-center safeText";

<TelerikTextBox Id="emptyReleaseOn" Class="@GetClass(isExpired)" Size="12" Value="@_currentBookingMTYRelease" ReadOnly="true" Width="6rem"></TelerikTextBox>

### Response

**Rob** commented on 14 May 2025

Thank you. That was the next direction I was going to try. Rob.
