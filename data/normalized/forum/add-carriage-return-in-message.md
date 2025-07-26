# Add Carriage Return in Message

## Question

**BobBob** asked on 22 Apr 2021

Is there any way I put a carriage return in the message for the Dialog? I have tried putting <br/> in the string as well as Environment.NewLine and \n\r and nothing seems to work. await Dialogs.ConfirmAsync("There are un-saved changes to the Account Detail. {I want a line break here} Do you want to save them before continuing?", "Un-saved Changes");

## Answer

**Marin Bratanov** answered on 23 Apr 2021

Hello Bob, The dialog uses the best practice from the framework where HTML is encoded and not rendered. This helps a lot in preventing XSS attacks. So, right now it is not possible to add HTML in messages. In a future version where a full-blown Dialog component exists you will be able to set a template for it where you could render the desired content. For the time being, you can consider one of the approaches from these sample projects: [https://github.com/telerik/blazor-ui/tree/master/common/confirm-button.](https://github.com/telerik/blazor-ui/tree/master/common/confirm-button.) Regards, Marin Bratanov Progress Telerik

### Response

**Greg** commented on 04 Jun 2021

Hello Martin, I'm not seeing in the example that you linked to a way to include multiple lines of text in a Dialog. The example given appears to be a custom Dialog component made out of a Telerik Window component. In my case (like the original poster, I think) I would like to include a line break, it doesn't have to HTML. I just need a way to display multiple lines of text in a Dialog Alert box. Is this possible? Thanks, Greg

### Response

**Dimo** commented on 09 Jun 2021

Hi Greg, Your observation is correct - the example shows how to use a TelerikWindow instead of a Dialog for scenarios where you need rich text inside the popup. The Dialog does not support this currently, because any HTML will be encoded. For a new line on a web page, you need a <br /> tag. Plain new lines are ignored by the browser (except in <textarea>s). If you don't need the line break at a specific place, you can set some width constraints to the Dialog and the text will break into multiple lines automatically..k-dialog-content { min-width: 100px; max-width: 300px }

### Response

**Bob** commented on 09 Jun 2021

Since the purpose of not allowing rich text is to prevent XSS attacks, couldn't you just prevent certain html tags (such as script, href, etc..). There is NO harm in allowing <br/> tags.

### Response

**Dimo** commented on 09 Jun 2021

Bob, that is certainly true and when we decide to enhance the Dialog, we will allow more flexibility. There is an open feature request that you can follow for updates: [https://feedback.telerik.com/blazor/1521466-rendering-html-texts-in-header-and-content-custom-dialog-content-html-components](https://feedback.telerik.com/blazor/1521466-rendering-html-texts-in-header-and-content-custom-dialog-content-html-components)

### Response

**Marc Simkin** answered on 26 Aug 2021

I know I'm late to provide an answer. I had a similar issue today, working on a custom message box. After spending too much time experimenting and then googling, I eventually found that the correct approach was to use MarkupString. I found the answer in a KB on a competitor's site and then more detail on Gerald Barre's blog.

### Response

**Dimo** commented on 27 Aug 2021

Hi Marc, You are right that MarkupString is the way to go, when you want to render raw HTML. However, our Dialog methods expect only a String argument and this imposes the discussed limitation.

### Response

**Carter** answered on 13 Sep 2022

I was able to get this working by putting "\n" where I want a newline and adding: .k-dialog-content { white-space: pre-line; } to my css file.

### Response

**Daniel** commented on 06 Oct 2023

A year late, but this worked perfectly for me. Thanks!!

### Response

**Hector** commented on 09 Feb 2024

Slight adjustment from above CSS snippet, but if I noticed that when adding `pre-line`, the dialog has an obscene amount of white space between the top of your text and the dialog title. Making below adjustment will re-align things visually (for me at least): .k-dialog.k-dialog-content { white-space: pre-line; padding-block: 0px 16px; /* realigns text compared to w/o `pre-line` */ }

### Response

**Charles** commented on 29 Oct 2024

This works very well Carter, thank you. I found it doesn't work when \n is embedded in a resource file and referenced as a Localizer. Unsure why... But if you "shift enter" in the resource editor (resx) file to add line breaks, they show up correctly.
