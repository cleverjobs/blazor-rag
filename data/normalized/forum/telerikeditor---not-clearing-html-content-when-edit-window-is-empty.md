# TelerikEditor - not clearing HTML content when edit window is empty

## Question

**Nic** asked on 14 May 2021

Hi, I'm just playing with the TelerikEditor control and I've noticed that if I type or paste some text into the editor and then delete it all, it's leaving behind some HTML. If just typing text and deleting it, it seems to leave "<p><br></p>" in the bound value. When pasting in some code from stack overflow I've also seen it leave behind this: "<pre><code><br></code></pre>" - this happens when you paste part of a code block and then a combination of "delete" & "backspace" (I haven't quite figured the order of deleting to get this). On a separate note, in an ideal world this control would be functionally similar to the other rich text editors in your suite - I'm trying to find one that behaves the same in Blazor (or the Web) and on WPF, as our application runs on different platforms. Yours seem very different to each other. No rush as for me as I probably won't use it anyway, but I thought I'd mention! Kind Regards, Nick.

## Answer

**Dimo** answered on 18 May 2021

Hi Nick, The empty paragraph ensures seamless and consistent cross-browser behavior of the Editor. For example, some browsers were unable to focus an empty contenteditable element. Even if this is a non-issue for their latest versions, we use a common rich-text editor engine for our different web component suites and support some older versions too. With regard to similar functionality - do you mean the appearance or the ability to produce specific HTML? Generally, the WPF RichTextBox is designed to look like MS Word with a ribbon UI. On the other hand, web editors normally aim to provide a simpler and more responsive layout. Nevertheless, our web editors are quite flexible and can produce pretty much any HTML, even with custom tools if needed. Regards, Dimo Progress Telerik
