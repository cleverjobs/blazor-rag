# Confusion from recent press release

## Question

**Ric** asked on 18 Sep 2019

This exert from an email you all sent today mentions 25 controls. Are they saying there will be 25 controls soon? I am seeing 16 right now, are they saying 9 more are ready? What are those 9 that are coming? With this release, we are also announcing the market-first Telerik UI
for Blazor with 25+ native components, support for Angular 8 and latest .NET
Core 3.0 (RC).

## Answer

**Marin Bratanov** answered on 19 Sep 2019

Hello Rick, There has been some slight confusion between the tech teams and the marketing team writing the blog post. The Blazor suite currently has 22 components (chart types are usually counted as different components in marketing, it seems), and we are working on adding more: [https://www.telerik.com/support/whats-new/blazor-ui/roadmap.](https://www.telerik.com/support/whats-new/blazor-ui/roadmap.) Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 19 Sep 2019

Hi again Rick, I wanted to make sure that you know we value your feedback. Should you identify a need for a component we are currently missing, we will appreciate it if you share it with us, so we can have it in mind when we build our future roadmaps. Regards, Marin Bratanov

### Response

**Rick** answered on 19 Sep 2019

Thanks Marin, The ComboBox is a good one, that is one I would have preferred in my current project I am releasing this week at work rather than a dropdown so that it could be easily search. I am about to finish up my own version of a search box to be used in conjunction with it but a combobox might have avoided that. If it were me making the decisions with components, I think i would have looked at a hybrid system. I would have started out by releasing all current jQuery components in wrappers like Syncfusion did, it seems like this wasn't a huge deal, and made it clear these were early version temporary components but would have replaced each component as you go through with native. I fully understand the reasoning of native, I agree with it and like it, but it would have been nice to have the full suite out of the gate, even if it meant that there would be times I would need to update a component.

### Response

**Marin Bratanov** answered on 22 Sep 2019

Hello Rick, Combobox and Multiselect are on our roadmap: [https://www.telerik.com/support/whats-new/blazor-ui/roadmap.](https://www.telerik.com/support/whats-new/blazor-ui/roadmap.) Stay tuned on the release notes for more details - we tend to ship releases pretty often to get features and components out. For example, with the official framework release next week we'll have three more charts coming up (which will, by the way, get the components count to 25). On native vs wrappers - we did initially consider this option, but we chose not to go with it for two primary reasons: What works in jQuery is not very likely to work in Blazor now. While in jQuery you were expected to finish up logic by traversing and modifying the DOM of the components, in Blazor you shouldn't do that. This is a serious paradigm shift and we didn't want to cause confusion in that regard. If people got used to hacking at the DOM, once we switched to native that would cause headaches. Moreover, the current way for implementing custom logic seems to be templates, and you can't have native templates in jQuery wrappers. That switch would actually delay the native components release significantly, and would introduce a great many breaking changes - just about every release would be full of them once we gut out a wrapper and replace it with a native component. Breaking changes are very painful to our customers and we strive to avoid them as much as possible. We realize that a full component suite would be nice, and we are working hard to get there. For example, in about half a year we have a grid that has all the main features a grid needs. Right now we're comparing suites that have been in production for a decade (like jQuery, MVC) or even more (WebForms, WinForms), while Blazor as a framework is not even out of the oven yet. With all the breaking changes that come into the framework, we still have to invest a sizeable portion of our time into reworking things and not only on new development. I hope this explain out point of view and reasoning. If you need more detail on some point, just let me know. Regards, Marin Bratanov

### Response

**Rick** answered on 22 Sep 2019

Thank you for the detailed response Marin, I appreciate it. I did not realize some of the difficulties the hybrid approach would have caused and long term I prefer the native. At-least in the short term there can be work arounds. For example you don't have an auto complete and I needed a search box so I took a input box and a telerik grid, wired in the value changed event on the input box to update the grid and wired in the selected items event on the grid. While I would have preferred the auto complete this is a solution that I can leave in the project as is and never update or update to your auto complete if one is made down the road. So it's workable, again thank you.

### Response

**Marin Bratanov** answered on 22 Sep 2019

That's how I would have approached that scenario with the current toolset, Rick. --Marin
