# Inject MediaQuery into code behind

## Question

**RobRob** asked on 14 May 2021

I was using Ed Charbenaeau's BlazorSize, but wanted to remove the extra dependency now that similar functionality is built into UI for Blazor. Is there an analogue to the IResizeListener/ResizeListener class? I have a base class component that's injecting IResizeListener, I didn't see a method to do that with Telerik. Thanks!

## Answer

**Marin Bratanov** answered on 17 May 2021

Hi Rob, The Telerik UI for Blazor suite does not provide a service for the window.resize event the browser raises. If you need that, you can implement your own, or use a third-party library like BlazorSize. Regards, Marin Bratanov

### Response

**Greg** commented on 16 Sep 2021

The BlazorSize site says the exact opposite - that you do NOT need to use it when using Telerik MediaQuery. Which is correct?

### Response

**Rob** commented on 16 Sep 2021

The website is correct for the MediaQuery component. However Blazorsize also has a resizelistener class that triggers events on resize, Telerik Blazor doesn't have an equivalent for this.

### Response

**Greg** commented on 11 May 2022

Can Telerik provide an example of how to implement a ResizeListener that captures the window.resize and works with the Telerik MediaQuery control?

### Response

**Marin Bratanov** commented on 11 May 2022

Hi everyone, it is important to make a distinction between the two "libraries", their purpose and intended use: The TelerikMediaQuery is a wrapper over CSS media queries JS API that is useful for having markup-like declaration for boolean logic in your components. Thus, it is simple to use, but also kind of limited to front-end runtime. It does not intend to provide a listener to the window.resize event. Other event-based approaches (like Ed's BlazorSize) give you an event through DI so you can use it in any way you like - more flexible in some cases, but requires more work in others. Thus, you don't need either if you are using the other, but there is no reason you can't use both, depending on what you need in that particular project/logic/scenario. Greg, the BlazorSize tool can give you that event, and there is no such thing as "make it work with the Telerik MediaQuery component" - these are two different pieces of code that are not intended to integrate with one another, they are intended to give you, the application developer, some flexibility and info around the viewport size.

### Response

**Greg** commented on 11 May 2022

Thanks for the clarification Marin. Unfortunately I have never been able to get the BlazorSize tool to work - I've tried a number of times but have never been able to resolve the numerous exceptions it generates at runtime. If there were some example projects demonstrating it in use in conjunction with Telerik controls that would be great - but I have never seen a working example to help implement it.

### Response

**Marin Bratanov** commented on 11 May 2022

A quick grep in the sample projects repo shows this one and this one use this package, so likely it works there. I am not aware of issues with its integration with the Telerik components, as there is no specific integration between them.
