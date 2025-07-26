# Appearance of standard html elements with a Telerik's theme

## Question

**NiV** asked on 11 May 2025

Good evening. I implemented Telerik's themes switching at runtime in my Blazor Server app by following this guide: [https://www.telerik.com/blazor-ui/documentation/knowledge-base/change-theme-runtime](https://www.telerik.com/blazor-ui/documentation/knowledge-base/change-theme-runtime) So far it seems to be working fine, as I can see the Telerik components change their appearance based on the chosen theme. I'd like to also apply the theme to other standard html elements in the DOM. For example, even after setting a Telerik's "dark" theme: The body of the page is still white The <label> tags are still black What is the correct and best approach to change the appearance of the above elements so that they are coherent with the chosen Telerik theme?

### Response

**Hristian Stefanov** commented on 14 May 2025

Hi Roberto, Make sure you’ve added the k-body class to the <body> element, as shown in the Knowledge Base article about the wrapping <div>. <body class="k-body"> If you're still running into issues, let me know. Kind regards, Hristian

### Response

**NiV-L-A** commented on 15 May 2025

Solved like you have indicated. Thank you very much.
