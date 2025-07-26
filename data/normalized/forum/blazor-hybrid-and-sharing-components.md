# Blazor Hybrid and sharing components

## Question

**RobRob** asked on 23 Feb 2023

I'm looking in to using Blazor Hybrid (inside a WPF wrapper) as an alternative to full traditional WPF in the next iteration of our software. I have a blazor webassembly site and want to share components etc. within both applications (Blazor Hybrid and Blazor Webassembly). I currently have the following: Software.Client (webassembly) Software.Server (webassembly backend) Software.Local (blazor hybrid wpf) I want to add a component library that both the hybrid and webassembly applications can use to share ui. I have tried a few methods of doing this, using the telerik blazor components, but have ran in to a few road blocks specifically Razor Class Library (couldn't use nuget ui to add the telerik ui blazor library) Before I go much further how supported is the Blazor Hybrid scenario within an WPF wrapper using the telerik blazor library? Are there any examples I can use to move forward? Any advice would be welcome. Many thanks, Rob

## Answer

**Svetoslav Dimitrov** answered on 28 Feb 2023

Hello Rob, You can use the Telerik UI for Blazor suite in a WPF application. On our public GitHub repository, you can see such a demo application. I hope that the configuration and additional information will help you move forward with your implementation. Regards, Svetoslav Dimitrov
