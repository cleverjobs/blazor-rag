# Getting validation tooltip in the triggering field with the grid?

## Question

**imw** asked on 12 Jan 2022

Hi, How can I get the tooltips for validation each field displayed at the corresponding field in a Grid Popup form and not just at the summary below the for the Form etc? Also, there is almost no spacing between the last field and the validation summary. Thanks.

## Answer

**Hristian Stefanov** answered on 17 Jan 2022

Hi Patrik, Currently, the built-in validation tooltip in Grid appears only for the inline and incell editing. There is a mistake in our documentation stating that every editing type has a built-in tooltip. We apologize for the mistake and will fix it very shortly. The Popup editing uses only a validation summary by design. That being said, I opened a feature request for a tooltip in Grid Popup on your behalf on our Public Feedback Portal: Built-in validation tooltip for the Popup editing You are automatically subscribed to receive email notifications on status updates. Still, as a side way to achieve the desired result, you can create a custom edit popup with validation. Additionally, if you want to adjust the validation summary of the default popup, use the following CSS selector to apply the desired styles. <style>.validation-message { margin-top: 10px;
}
</style> Thank you. Regards, Hristian Stefanov

### Response

**imwise** commented on 17 Jan 2022

Hi, Thank you and good that you update the documentation here and hopefully add this feature in a future release.

### Response

**ManojKumar** commented on 14 Dec 2022

I'm not sure if its already documented that editor templates disable built-in validation tooltips, at least I had hard time figuring that. Thank for the details and sample.
