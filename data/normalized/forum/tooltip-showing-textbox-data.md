# Tooltip showing textbox data

## Question

**Lar** asked on 06 Feb 2023

I'm using a textbox in a grid and have a real estate issue where text is cut off because I'm limited on the width of the textbox. The end users will typically save special characters (e.g. '@, ( ), etc...'). These cause the tooltip to blow up as it appears to use a Jquery selector which doesn't like special characters. Is there a workaround for this? I don't want to tell the end-users that they can't use characters they're used to using.

### Response

**Nadezhda Tacheva** commented on 09 Feb 2023

Hi Larry, I'd like to first double-check with you to make sure I correctly understand the use case. You are using a custom TextBox in a Grid and as the text in it can be long, you are displaying a Tooltip with the full content. In this case, you are experiencing issues with entering special characters in the TextBox since it affects the Tooltip. Is that correct? Please let me know if I am missing something and if the scenario is different. In general, the Tooltip TargetSelector needs a valid CSS selector and its proper behavior will depend on what one is passing as a selector. I am curious to find out what is causing the issue on your end. I have created a sample that showcases my understanding of the scenario: [https://blazorrepl.telerik.com/QdYwEXPu15cNA53p50.](https://blazorrepl.telerik.com/QdYwEXPu15cNA53p50.) Can you please modify that to showcase the exact problem you are experiencing? Thus, I can review your actual configuration to find the root cause of the problem and suggest further steps. Thank you in advance!

### Response

**Larry** commented on 09 Feb 2023

You understand the issue correctly and your sample solves it, I was using the text itself as part of what the TargetSelector was trying to show.
