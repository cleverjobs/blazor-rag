# Adding a Table of Contents - TelerikEditor

## Question

**Jus** asked on 19 Jan 2025

On my previous site, I used the TinyMCE editor, which had a useful feature that allowed me to add and update a Table of Contents (TOC) at the top of the text I entered. I wonder if there is similar support for adding a TOC when using the TelerikEditor with Telerik UI for Blazor. The link title and indentation level were based on the heading type (H1, H2, H3, etc.). I am using the Telerik Editor for a Knowledgebase creation page, and having a TOC would be very useful. Also, I'm trying to avoid the need to create a custom tool to do this :-) Justin

## Answer

**Hristian Stefanov** answered on 20 Jan 2025

Hi Justin, Currently, the Telerik UI for Blazor Editor does not have built-in support for automatically generating a Table of Contents (TOC) based on the heading structure of the content. For a potential approach, you can consider manually creating a TOC by inserting links to different sections of your content. This would require manually updating the TOC whenever you update your content by using the Editor's tools. If this functionality is crucial for your application and manually creating a table does not work for you, I recommend submitting a feature request on our public feedback portal. There, you can describe your expectations of such potential functionality and share your ideas for enhancement. The feature requests logged in the portal are reviewed and evaluated by the Telerik Blazor team weekly. If their status changes to "Unplanned," they are considered valid, and based on the community's interest, they may be planned for implementation in subsequent releases. Regards, Hristian Stefanov Progress Telerik
