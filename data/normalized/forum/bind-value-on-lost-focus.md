# Bind value on lost focus

## Question

**Rob** asked on 23 Nov 2019

How can I change the default binding event? Currently the value is bound on every keystroke which can cause some problems (like losing charachters) where the user types fast on a slow connection. I would like to change the binding in a way that it would occur on lost focus? Thank you

## Answer

**Robert** answered on 23 Nov 2019

After a bit of investigation I have figured it out that losing charachters when typing fast has nothig to do with binding. Even if the value is not bound the same thing happens. Is there any workaround?

### Response

**Marin Bratanov** answered on 25 Nov 2019

Hi, This behavior is observed because of the latency of the SignalR connection and its async nature. Every keystroke goes to the server for processing (such as validation), and before a response comes back, another keystroke happens, and this causes such confusion. We are aware of this and we will see if anything can be done, and you can Follow the status of this task here (I have added your Vote for it): [https://feedback.telerik.com/blazor/1422019-unable-to-show-all-typed-characters-in-textbox.](https://feedback.telerik.com/blazor/1422019-unable-to-show-all-typed-characters-in-textbox.) The MS Issue linked from the article explains the situation in much more detail. At the moment, there is no feature I can offer that will work around this. Changing the binding event is not available now, perhaps it might become possible through attribute splatting in the future (although I am not sure that it could be done, I have not tried), and the server code needs to execute for a variety of reasons. A WASM app would not have this issue, though. The only other idea I can offer right now is to use a standard input and our styling for it: [https://docs.telerik.com/blazor-ui/themes/form-elements#inputs.](https://docs.telerik.com/blazor-ui/themes/form-elements#inputs.) Regards, Marin Bratanov

### Response

**Robert** answered on 25 Nov 2019

Hi Marin, thanks for the answer. Linked MS github issues is not fixed and using a standard html input I'm not seeing this behaviuor so there must be something inside a TelerikTextBox that is causing the problem. I hope for a soon fix Best regards, Robert

### Response

**Robert** answered on 25 Nov 2019

I can't edit my post. I had a typo.. MS github issus IS FIXED :) [https://github.com/aspnet/AspNetCore/issues/8204](https://github.com/aspnet/AspNetCore/issues/8204)

### Response

**Marin Bratanov** answered on 25 Nov 2019

Hi Robert, Our components do more than just @bind-Value and in their fix they also exposed the @bind:event, which is not available on ours (yet). Our components need to execute server code when ValueChanged is to fire, which requires the C# code execution, which in a Server app has the latency and async nature described in the issue. Regards, Marin Bratanov

### Response

**Alan** answered on 04 Nov 2020

Has there been any progress on this? Requiring server trips for every key stroke seems to rule out using the Telerik components for a lot of scenarios. Which input components does this affect?

### Response

**Marin Bratanov** answered on 04 Nov 2020

Hello Alan, The issue with the lost characters has been fixed a long time ago: [https://feedback.telerik.com/blazor/1422019-unable-to-show-all-typed-characters-in-textbox](https://feedback.telerik.com/blazor/1422019-unable-to-show-all-typed-characters-in-textbox) If you do experience it again with the latest version, please open a ticket and send us a reproducible. Regards, Marin Bratanov

### Response

**Alan** answered on 04 Nov 2020

The issue I was interested in was not having the option available to change the binding to only require communication with the server when the control lost focus. Our application provides it own ViewModel for dealing with things like validation so we don't really need the overhead of communicating with the server on every keypress

### Response

**Marin Bratanov** answered on 04 Nov 2020

Hello Alan, The following article treats this, if reviewing it and the feature request it links, you have any questions, let me know: [https://docs.telerik.com/blazor-ui/knowledge-base/textbox-validate-on-change](https://docs.telerik.com/blazor-ui/knowledge-base/textbox-validate-on-change) Generally, the server-side Blazor flavor is suitable for environments with very low latency, so this will not be an overhead. For other cases where lag is noticeable, WebAssembly is the better flavor. Regards, Marin Bratanov
