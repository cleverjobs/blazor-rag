# Exclude characters?

## Question

**Jas** asked on 07 Jan 2021

I typically use the mask to prevent the user from entering in "bad" characters. Is this possible with MaskTextBox? I only saw a handful of predefined rules. I know I can use validation too. Perhaps the best method is to notify the user their input is bad AND not allow it to be inputted...

## Answer

**Marin Bratanov** answered on 07 Jan 2021

Hello Jason, At the moment, the only way to do that would be through a data annotation validation - e.g., a regex (you can find a couple of examples here ). Would the ability to define custom rules solve your case? You can see how that would work in our Reach suite that already has this capability here (see the second example). If yes, we could open up a feature request page for you to monitor this on our

### Response

**Jason** answered on 07 Jan 2021

Yes the feature like Reach would be perfect. The MaskedTextBox is great for numbers like date and phone, but apostrophe is very common in names, as well as some extended ascii for accented letters. Annotation/validation is working out fine for us as an alternative.

### Response

**Marin Bratanov** answered on 07 Jan 2021

Hi Jason, I made this page where you can click the Follow button to get email notifications for status updates: [https://feedback.telerik.com/blazor/1501432-custom-rules-in-the-masked-textbox.](https://feedback.telerik.com/blazor/1501432-custom-rules-in-the-masked-textbox.) I've added your Vote on your behalf to raise its priority. Regards, Marin Bratanov
