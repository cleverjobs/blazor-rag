# Cannot type in latest VS 2022 razor editor due to snippets

## Question

**Bri** asked on 19 Mar 2024

I find with the latest Telerik extension enabled, I cannot type anything ( even plain text, with no html tags ) in the non-code section of a razor component ( .razor file ) due to excessive snippet activations ( they don't just list, they insert when spacing to the next word ). I have played with the VS Options for both csharp and razor editor advanced settings and nothing seems to work. There are several new settings related to snippets, but the Telerik extension doesn't seem to honor them. For example, there is one that requires a double tab to select a snippet. Instead, tab, space, etc select the first one in the list, meaning I am constantly fighting to remove the inserted snippet on literally every other word. Snippets behave as expected if I disable the Telerik extension and restart VS. And it does it in both the latest Preview and non-Preview versions of Visual Studio ( installed side by side on same machine ). I feel like this may be more related to recent .net 8 era razor editor changes in VS, some of which is experimental, as well as a "new" razor editor. ( i have not tested in the legacy razor editor because i don't want to use the legacy razor editor in general ). I've searched in various ways here and haven't found anyone reporting the same issue, so I'm not sure if it's just me, or if I'm the first to report it. I don't have any other code helpers or extensions installed. Thank you for your time and consideration. I'm happy to jump on a teams call with anyone who might want to see it happening, although it should be easy to replicate on latest VS 2022.

### Response

**Brian** commented on 20 Mar 2024

UPDATE: I at least found a way to exclude all snippets in razor files with Telerik extension still enabled. Tools | Options | Text Editor | Razor | Advanced, changing "Included Snippets" to NONE turns them off entirely so one can work in a razor file. It's extreme, as it means no snippets pop up. So I will probably put a ticket in to make devs aware unless they respond to this forum. I wanted to start here to see if i was crazy / the only one...

### Response

**Nikola** commented on 22 Mar 2024

Hi Brian, I am sorry to hear about the issues you have experienced using our Visual Studio extensions. I have tested the snippet activation and in my experience, the behavior is as follows: With Telerik UI for Blazor extension enabled - Both the built-in snippets and our custom snippets are displayed while typing - Both built-in and our custom snippets are inserted by pressing space/tab - Our custom snippets are listed separately and not side-by-side with the built-in ones With Telerik UI for Blazor extension disabled - Built-in snippets are displayed while typing - Built-in snippets are inserted on space/tab In general, the behavior is the same except that the snippet UI is broken when our extension is enabled. Could you confirm that what you experience is similar and outline any significant differences? The changes in the Razor editor could have affected the snippet integration, so we will explore them and make changes if necessary.

### Response

**Brian** commented on 22 Mar 2024

Thank you for the response. Yes and no. Just in the body of a component, not in @code section, and not in an html tag, try to type the plain text "If you feel this is in error, please contact your supervisor or put in a service ticket requesting access." You should find with Telerik enabled, you cannot. you get <a> <input> <table> etc auto-injecting everytime you press space to go to another word. With Telerik disabled, this does not happen. In testing it again for you, i figured out the diff. With Telerik disabled, you do get the snippet suggestions for a, input, table, etc, but they aren't selected. You click the down arrow to scroll to the one you want and THEN space will insert it. But if you never hit down arrow to select even the first one, then you can click further letters to finish the word, and space does not insert a snippet. With Telerik enabled, as soon as the snippet list appears, it is somehow active even though it doesn't show a selection of the first item. So the next space press will insert it, even if you never hit the down arrow to scroll through the list. I can provide a video or sceenshots if you can't reproduce based on this. Hope that helps, and thank you again very much for your time and consideration! Brian

### Response

**Nikola** commented on 26 Mar 2024

Hello Brian, Thank you for the additional clarification and for the efforts you invested in testing. There were changes made in the new Razor editor that affected the behavior of our snippets. We are still investigating what changes we need to make to improve the experience in general, but one of them would be not considering space as a commit character for the snippets as this changed in the latest version of the Razor editor. Once we have a better idea of the scale of the changes I'll get back to you.

### Response

**Nikola** commented on 27 Mar 2024

Hello Brian, Attached you will find a development version of the Telerik UI for Blazor VS Extension. We have made changes in the commit characters that should improve usability. To install the extension extract the archive and run the.vsix file located within. We'd appreciate it if you could provide feedback on how these changes affect your experience. Thank you in advance.

### Response

**Brian** commented on 02 Apr 2024

Perfect, yes, thank you! I tested with both VS2022 vanilla and Preview installations and it now works as expected again. Thank you for the quick turn-around and attention to my issue. One of the reasons we chose Telerik for this project was because of reviews that said you provide excellent support. That appears to be true - thanks again! Brian

### Response

**Nikola** commented on 03 Apr 2024

Hi Brian, I am glad that everything works as expected and I'd like to thank you for the appreciation of our services. The fix will go live with the next planned release of the Visual Studio extensions at which point you will have to update the one you are using currently. Until that moment you can continue using the development version of the extension. Regards.

### Response

**Brian** commented on 23 May 2024

Heads up the next release of the extension for Blazor ui 6.0 broke it again. In fact, it's not just broken in .razor files now. I have been working in a .net framework 4.8 mvc application... it's doing the same behavior in a .cshtml - auto-injecting snippets instantly as you type anything, even plain text stuff that isn't even in markup tags. I had to disable it just to work. Just wanting to make you aware. I don't need a fix, per se, since i can just disable it when i don't need the functionality of the extension. But if you put out another fix, i'm happy to test it for you again. Brian

### Response

**Nikola** commented on 27 May 2024

Hi Brian, Thank you for letting us know about the problem. The fix that was provided through the custom-built VS Extension was not deployed with the latest release and was postponed. Therefore the issue is still present. We plan to go live with it later this week with the next release. I apologize for any inconvenience this may have caused. Regards. Nikola.
