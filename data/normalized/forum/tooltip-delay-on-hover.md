# Tooltip delay on hover

## Question

**Osc** asked on 27 Sep 2021

Is there a way to add some delay to the TelerikTooltip component show event? I would like to force the user to hover in the element for a couple of seconds before he can see the tooltip. Thanks,

## Answer

**Hristian Stefanov** answered on 30 Sep 2021

Hi Oscar, Thank you for the idea. We have opened a feature request on your behalf on our Public Feedback Portal: Expose ShowDelay and AutoCloseDelay properties in the Tooltip This feature will allow you to control the tooltip show and hide delay. Since we created this feature request on your behalf, you are automatically subscribed to receive email notifications for status updates. We prioritize feature requests depending on community interest. This is why I increased the item's popularity by adding your vote there on your behalf. I can confirm that we are not aware of any workarounds in the meantime for setting a delay on hover. The option you can try is to use the standard Task.Delay() to set a delay if you are loading the tooltip data on demand. Please let me know if you have any other questions. Regards, Hristian Stefanov
