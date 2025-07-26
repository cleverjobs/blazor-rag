# Set the value attribute for a Submit ButtonType

## Question

**BobBob** asked on 08 Nov 2024

Is there a way to set the value attribute for a submit button when using the TelerikButton. For example, this is the button markup I am currently using: <button type="submit" class="login100-form-btn" name="provider" value="@provider.Name" title="Log in using your @provider.DisplayName account"> <TelerikSvgIcon Icon="@GetExternalIcon(provider.Name)" Size="@ThemeConstants.SvgIcon.Size.ExtraExtraLarge" Class="me-3" /> Login using @provider.DisplayName </button> I want to convert this to using a TelerikButton but I cannnot figure out how to set the value attribute when doing that.

## Answer

**Nansi** answered on 13 Nov 2024

Hi Bob, Currently, the TelerikButton component does not support setting a value attribute. Can you share a bit more details on how do you currently consume the <button> value? What is the use case? Do you use the <button> in TelerikForm? Our TelerikForm doesn't do a classic POST request and I am not sure how do you consume the value from the <button> you are currently using. This can help me to provide an alternative solution. I am looking forward to hearing from you. Regards, Nansi Progress Telerik
