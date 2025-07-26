# Why is OnChanged event fired when no change occured?

## Question

**Jef** asked on 04 Mar 2021

Seems to me the OnChanged event should probably be called something else since it fires when no change occurred. What's the best way to implement a true OnChange event?

## Answer

**Svetoslav Dimitrov** answered on 04 Mar 2021

Hello Jeffrey, As an attached file I have added a demo project. It implements a very basic scenario of a TextBox with the onchange event set up. The OnChange event should fire when the user presses enter or focus away from the component. Could you modify the application so that the issue is reproducible and we can further investigate it? Regards, Svetoslav Dimitrov

### Response

**Jeffrey** answered on 04 Mar 2021

The OnChanged event is firing as documented. My issue is that it makes no sense to fire the CHANGE event, when no change occured! Every other component I've ever used fires the change event when the value in the field changes. The OnChanged event for the Blazor controls is really no different than the Blur event except it also fires when the user hits the Enter key. Is it really on me to track the before/after values on every field to see if something changed? I've got a rather sophisticated application with dozens and dozens of fields and a complex grid that I'm having to track every single before/after and it's getting to be a lot of code. Is there any plan on having a true OnChange event?

### Response

**Svetoslav Dimitrov** answered on 05 Mar 2021

Hello Jeffrey, Our components are data agnostic, which means that they are not reliant or aware of the data you pass to them. This provides great flexibility while using them, for example - you can provide different data types, collections, or structures of data. We provide UI components and so the events we provide should be used to respond to different user actions as hooks. Validation, such as comparing the old to new value is up to the application to implement - the domain of our components is to give users UI to interact with, and appropriate events to the application upon that interaction. That said, a way to achieve tracking for when model properties change is by taking advantage of the INotifyPropertyChanged interface in your models. Regards, Svetoslav Dimitrov

### Response

**Jeffrey** answered on 05 Mar 2021

Thanks for the detailed explanation. However, I would still assert that calling it OnChange is confusing. I've used your ASP.NET controls for years and with those OnChange fires only when the field value has changed. This behavior is a change in your UI paradigm.

### Response

**Marin Bratanov** answered on 06 Mar 2021

Hi Jeffrey, If I may jump in this discussion since I've also been supporting our WebForms components for years. The executive summary of this post is that you should use ValueChanged to try to do things like in WebForms. I'd encourage you to review this article for some more details on the way things work in Blazor. The first thing I must note is that there is a serious paradigm shift between Blazor and WebForms. While there are some things that they share (like the ability to be kind of stateful, the ability to have a "code-behind" for a page, the presence of events), there are also many things that are extremely different - such as the way two-way binding works in blazor (Parameter+ParameterChanged event), lack of HTTP requests for actually posting values to the backend, lack of direct DOM manipulations. This means that there cannot be complete parity in the way code is written in both frameworks, attempting to do that would be a disservice to the new framework and to all our other customers who expect things to be done in the way suitable for that framework. To finally get to the particular question - while I agree that this event could have had a slightly different name, there aren't many to choose from that can actually describe what it does, and we went with the one that matches the DOM event we use for it - @onchange. What is most relevant, though, is that in Blazor there are no valueChangING + valueChangED combinations of client-side events and then a server-side ValueChanged event like you had seen in our components in WebForms. It is all one event now - ValueChanged (or, to be more generic, <ParameterName>Changed). The way you cancel an event is by NOT updating the view-model with the new value that comes in. The way you let it propagate is by actually updating the view-model. The way you change what the user did is by updating the viewmodel with a value different than what the user chose and you got in the event handler. By default two-way binding always updates the view-model with what was supplied, so handling the event yourself lets you prevent that and to implement custom logic. The key thing here is updating the viewmodel. The other important bit is that this is done for the event tied to the parameter. The OnChange event we have is not tied to a property for two-way binding (the Value parameter). Actually, one of its main goals is to let you have an event to do things like load data on demand, while still being able to benefit from two-way binding because handling the ParameterChanged event does not let you do that in Blazor, and without two-way binding handling things like forms can become very cumbersome when you have to set the ValueExpression parameters yourself. I hope this clarified the major differences and how things work in Blazor, and why. If you have any outstanding questions, let me know. Regards, Marin Bratanov

### Response

**Jeffrey** answered on 06 Mar 2021

Marin, That was very helpful... I appreciate the in-depth explanation. One last question. You stated this: "To finally get to the particular question - while I agree that this event could have had a slightly different name, there aren't many to choose from that can actually describe what it does, and we went with the one that matches the DOM event we use for it - @onchange." With that said, the DOM @onchange event does not fire unless the value changed. The OnChange event will fire just by leaving the field...even if the user did nothing but click into the field and then click out. Why not limit that to the OnBlur event?

### Response

**Marin Bratanov** answered on 06 Mar 2021

Hello Jeffrey, If you need an OnBlur event, the inputs now have that as well: [https://docs.telerik.com/blazor-ui/components/textbox/events#onblur](https://docs.telerik.com/blazor-ui/components/textbox/events#onblur) There are many caveats with adding many events to components (mostly related to performance) which is why we were rather wary of exposing too many. Changing the way OnChange works now will be a breaking change for people who have had apps in production for over a year and a half. So, we have documented how it works so people can read it in the documentation and intellisense. Regards, Marin Bratanov

### Response

**Jeffrey** answered on 07 Mar 2021

Thanks Marin... and to be clear, the only difference between OnChange and OnBlur is that OnChange fires when the user hits the Enter key?

### Response

**Rune** commented on 28 Feb 2024

Hi Jeffrey! This is an older post but still relevant. I react to the exact same issue. If you leave the naming of the event outside the equation there is another perspective to the problem which I think Telerik should strongly consider; the fact that the most natural use-case of the component is not covered in a good way. In most cases you do not want the event handler to go crazy on some "Change" event inside a specific component based on clicking around the UI outside or inside any component at all. For a desktop UX this is hardly ever the expected behavior but on mobile it is more to the point. 3 desktop user scenarios when the input is in focus: Hit Enter and stays inside the input but fires a change event Hit Tab to fire a change or blur event Clicking outside and inside the input - no events fired. Different behaviours could easily be achieved through e.g. an enum parameter to reduce the amount of events fired and plumbing code outside the component.

### Response

**Marin Bratanov** answered on 08 Mar 2021

Yes. And the event arguments type. --Marin
